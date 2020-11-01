require 'open3'

class SSHCertificateGenerator
  attr_reader :ca_private_key

  def initialize(ca_private_key)
    @ca_private_key = ca_private_key
  end

  def generate(options)
    # Validate our mandatory fields are present
    %i[username user_public_key].all? { |o| options.include? o }

    # For optional fields, set default values if they aren't present
    certificate_id = options.fetch('certificate_id') { 'no-id' }

    # Write a users key to a file
    keyfile_name = 'key.pub'
    user_public_key = options['user_public_key']
    key = File.open(keyfile_name, 'w')
    key << user_public_key
    key.rewind

    cmd = "ssh-keygen -s #{ca_private_key} -I #{certificate_id} -n #{options['username']}"
    cmd += " -V #{options['validity_period']}" if options.include? 'validity_period'
    cmd += " -O #{options['forced_command']}" if options.include? 'forced_command'
    cmd += ' -O no-pty' if options.include? 'deny_pty'
    cmd += ' -O no-port-forwarding' if options.include? 'deny_port_forwarding'

    cmd += " #{keyfile_name}"

    `#{cmd}`

    File.read('key-cert.pub')
  end
end

require 'sinatra'
require_relative 'ssh_certificate_generator'

post '/' do
  data = JSON.parse(request.body.read)
  generator = SSHCertificateGenerator.new('ca.key')
  generator.generate(data)
end

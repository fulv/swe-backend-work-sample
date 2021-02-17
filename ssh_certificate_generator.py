import subprocess


class SSHCertificateGenerator(object):
    def __init__(self, ca_private_key):
        self.ca_private_key = ca_private_key

    def generate(self, options):
        if 'username' not in options:
            raise Exception('Missing username')

        if 'user_public_key' not in options:
            raise Exception('Missing public key')

        certificate_id = options.get('certificate_id', 'no-id')

        keyfile_name = 'key.pub'
        user_public_key = options['user_public_key']
        with open(keyfile_name, 'w') as key:
            key.write(user_public_key)

        cmd = "ssh-keygen -s %s -I %s -n %s" % \
              (self.ca_private_key, certificate_id, options['username'])

        if 'validity_period' in options:
            cmd = cmd + ' -V %s' % options['validity_period']
        if 'forced_command' in options:
            cmd = cmd + ' -O %s' % options['forced_command']
        if 'deny_pty' in options:
            cmd = cmd + ' -O no-pty'
        if 'deny_port_forwarding' in options:
            cmd = cmd + ' -O no-port-forwarding'

        cmd = cmd + ' %s' % keyfile_name

        print(cmd)

        subprocess.call(cmd, shell=True)

        return open('key-cert.pub').read()

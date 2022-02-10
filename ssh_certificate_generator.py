# https://docs.python.org/3/library/subprocess.html#security-considerations
# Security Considerations
# Unlike some other popen functions, this implementation will never implicitly
# call a system shell.  This means that all characters, including shell
# metacharacters, can safely be passed to child processes. If the shell is
# invoked explicitly, via shell=True, it is the application's responsibility
# to ensure that all whitespace and metacharacters are quoted appropriately to
# avoid shell injection vulnerabilities.  On some platforms, it is possible to
# use shles.quote() for this escaping.
from shlex import quote
# This only works on UNIX-like platforms.  Do not
# run this docker-compose on Windows.

import logging
import subprocess


#logger = logging.getLogger(__name__).addHandler(logging.NullHandler())
# https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library


class SSHCertificateGenerator(object):
    def __init__(self, ca_private_key):
        # Is there any way a hacker could monkeypatch ca_private_key?
        # If this service is only invoked via RESTapi, probably not.
        self.ca_private_key = ca_private_key

    # Can the generate() method or the class itself be monkeypatched?
    # Double check that the docker container's python import path machinery
    # can not be messed with.
    def generate(self, options):
        if 'username' not in options:
            raise Exception('Missing username')

        if 'user_public_key' not in options:
            raise Exception('Missing public key')

        certificate_id = quote(options.get('certificate_id', 'no-id'))

        keyfile_name = 'key.pub'
        user_public_key = quote(options['user_public_key'])
        with open(keyfile_name, 'w') as key:
            key.write(user_public_key)

        cmd = "ssh-keygen -s %s -I %s -n %s" % \
              (self.ca_private_key, certificate_id, quote(options['username']))

        if 'validity_period' in options:
            cmd = cmd + ' -V %s' % quote(options['validity_period'])
        if 'forced_command' in options:
            cmd = cmd + ' -O %s' % quote(options['forced_command'])
        if 'deny_pty' in options:
            cmd = cmd + ' -O no-pty'
        if 'deny_port_forwarding' in options:
            cmd = cmd + ' -O no-port-forwarding'

        cmd = cmd + ' %s' % keyfile_name

        # Instead of outright printing cmd and ret, I would log them.
        # That way, users of this package have a chance of overriding
        # the desired log level.
        #logger.info(cmd)

        # The return value of subprocess.call was not checked.
        # See:
        #   - test_empty_username
        #   - test_empty_public_key
        # I could not find a spec of known error return values,
        # however, in UNIX-fashion, a value of 0 denotes success.
        ret = subprocess.call(cmd, shell=True)

        if ret:
            raise Exception(f'Command returned value {ret}')

        #logger.info(ret)

        return open('key-cert.pub').read()

        # The files generated during the course of this method are left behind
        # until the next invocation.  In the best case, they are overwritten
        # next time, but I would clean them up before returning.

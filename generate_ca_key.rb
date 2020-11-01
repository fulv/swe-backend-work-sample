require 'openssl'

ca = File.open('ca.key', 'w')
ca << OpenSSL::PKey::RSA.new(2048)

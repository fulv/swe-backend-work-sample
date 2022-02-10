from flask import Flask
from flask import request
from ssh_certificate_generator import SSHCertificateGenerator
import json

#config = {
#    "DEBUG": True
#}

app = Flask(__name__)
#app.config.from_mapping(config)


@app.route('/', methods=['POST'])
def generate():
    generator = SSHCertificateGenerator('ca.key')
    pub = generator.generate(request.json)
    return json.dumps({'key': pub})

from flask import Flask
from flask import request
from ssh_certificate_generator import SSHCertificateGenerator
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def generate():
    generator = SSHCertificateGenerator('ca.key')
    pub = generator.generate(request.json)
    return json.dumps({'key': pub})

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

with open('ca.key', 'wb') as ca:
    key = rsa.generate_private_key(65537, 2048)
    key = key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.TraditionalOpenSSL,
        serialization.NoEncryption()
    )
    ca.write(key)

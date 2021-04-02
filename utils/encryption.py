from django.conf import settings
import hashlib

def generate_password(password):
    # dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
    key = str(settings.SECRET_KEY)
    result = hashlib.pbkdf2_hmac('sha256', str(password).encode('utf-8'), key.encode('utf-8'), 100000)
    return result.hex()

def verify_password(password, chiper):
    generated = generate_password(password)
    return generated == chiper
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


def get_user_key(username, password):
    username_encoded = username.encode()
    password_encoded = password.encode()
    salt = b'\xdd{\x12\x86\xa8\xb8}\x94EK\x06\xad\x89sx\x01'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(username_encoded))
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=key,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_encoded))
    return key


def encrypt_user_data(username, password, msg):
    user_key = get_user_key(username, password)
    f_obj = Fernet(user_key)
    return f_obj.encrypt(msg.encode())


def decrypt_user_data(username, password, msg):
    user_key = get_user_key(username, password)
    f_obj = Fernet(user_key)
    return f_obj.decrypt(msg).decode()

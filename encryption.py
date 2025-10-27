from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password: str):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_data(data: str, password: str) -> str:
    key = generate_key(password)
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data: str, password: str) -> str:
    key = generate_key(password)
    f = Fernet(key)
    return f.decrypt(encrypted_data.encode()).decode()

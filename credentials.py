from cryptography.fernet import Fernet

def encrypt_password(password):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    token = cipher.encrypt(password.encode())
    return key, token

def decrypt_password(key, token):
    cipher = Fernet(key)
    return cipher.decrypt(token).decode()
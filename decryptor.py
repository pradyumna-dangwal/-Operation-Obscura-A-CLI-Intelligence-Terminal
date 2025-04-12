from utils.cipher import caesar_decrypt

def decrypt_mission_file(file_path, shift):
    with open(file_path, 'r') as f:
        encrypted = f.read()
    return caesar_decrypt(encrypted, shift)
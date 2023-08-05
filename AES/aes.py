import os
from Crypto.Random import get_random_bytes 
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(file_path, key):
    salt = get_random_bytes(32)
    key = str(key).encode()
    key = PBKDF2(key, salt, dkLen=32)
    output_file_path = file_path + '.enc'
    
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    
    cipher = AES.new(key, AES.MODE_CBC)
    ciphered_data = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(output_file_path, 'wb') as f:
        f.write(salt)
        f.write(cipher.iv)
        f.write(ciphered_data)

def aes_decrypt(file_path, key):
    with open(file_path, 'rb') as f:
        salt = f.read(32)
        iv = f.read(16)
        ciphered_data = f.read()

    key = str(key).encode()
    key = PBKDF2(key, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)

    with open(file_path[:-4], 'wb') as f:
        f.write(original_data)


import rsa

def rsa_encrypt(file_path, key):

    with open(key, "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    with open(file_path, "rb") as f:
        data = f.read()
    encrypted_data = rsa.encrypt(data, public_key)
    with open(file_path + ".enc", "wb") as f:
        f.write(encrypted_data)

def rsa_decrypt(file_path, key):

    with open(key, "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    with open(file_path, "rb") as f:
        data = f.read()
    decrypted_data = rsa.decrypt(data, private_key)
    with open(file_path[:-4], "wb") as f:
        f.write(decrypted_data)

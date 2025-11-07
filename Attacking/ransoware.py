from cryptography.fernet import Fernet

def genarate_key():
    return Fernet.generate_key()

def encrypt_file(file_name, key):
    f = Fernet(key)

    with open(file_name, "rb") as file:
        original_data = file.read()

    encrypt_data = f.encrypt(original_data)

    with open(file_name + ".encrypted", "wb") as file:
        file.write(encrypt_data)
    
    print(f"File {file_name} successufully encrypted")

def decrypt_file(file_encrypt,  key):
    f = Fernet(key)

    try:
        with open(file_encrypt,  "rb") as file:
            encypt_data = file.read()

        decrypt_data = f.decrypt(encypt_data)
        original_file = file_encrypt.replace(".encrypted", "")

        with open(original_file, "wb") as file:
            file.write(decrypt_data)

        print(f"File {original_file} decrypt successufuly")
    except Exception as e:
        print(f"Decrypt error\n Incorrect key or corrupted data: {e}")

from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Generate a key (do this only once and keep it secure)
def generate_key():
    return Fernet.generate_key()

# get key
def get_key(keyname):
    cipher_key = os.getenv(keyname)
    return cipher_key

# Encrypt data
def encrypt_data(key, data):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Decrypt data
def decrypt_data(key, encrypted_data):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

# Example usage
if __name__ == "__main__":
    # Generate and print a key (store this securely)
    # key = generate_key()
    # print(f"Key: {key.decode()}")
    key = get_key("secure_key")
    print(f"Key: {key}")

    # Replace these with your actual message
    message = "[sample encrypted message]"

    # Encrypt message
    encrypted_message = encrypt_data(key, message)

    print(f"Encrypted message: {encrypted_message}")

    # Decrypt message
    decrypted_message = decrypt_data(key, encrypted_message)

    print(f"Decrypted message: {decrypted_message}")

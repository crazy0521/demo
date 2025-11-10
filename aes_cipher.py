# 🔧 Step 1: Install the library

# Run this command in your VS Code terminal first:

# pip install cryptography
# or pip install cryptography==41.0.3


# run file python aes_cipher.py

# AES Encryption and Decryption Program using Python
# --------------------------------------------------

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Function to encrypt text using AES
def aes_encrypt(plaintext, key):
    # Convert text and key to bytes
    plaintext = plaintext.encode()
    key = key.encode()

    # Ensure key length is 16, 24, or 32 bytes (AES standard)
    if len(key) not in [16, 24, 32]:
        raise ValueError("Key must be 16, 24, or 32 bytes long!")

    # Generate a random Initialization Vector (IV)
    iv = os.urandom(16)

    # Add padding to the plaintext (AES works on blocks of 16 bytes)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # Create AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return (iv, ciphertext)

# Function to decrypt text using AES
def aes_decrypt(iv, ciphertext, key):
    key = key.encode()
    if len(key) not in [16, 24, 32]:
        raise ValueError("Key must be 16, 24, or 32 bytes long!")

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()

    return decrypted_data.decode()

# ------------------------------
# MAIN PROGRAM
# ------------------------------
if __name__ == "__main__":
    plaintext = input("Enter text to encrypt: ")
    key = input("Enter key (16/24/32 chars): ")

    iv, ciphertext = aes_encrypt(plaintext, key)
    print("\n--- AES ENCRYPTION ---")
    print("IV:", iv.hex())
    print("Encrypted Text:", ciphertext.hex())

    decrypted_text = aes_decrypt(iv, ciphertext, key)
    print("\n--- AES DECRYPTION ---")
    print("Decrypted Text:", decrypted_text)

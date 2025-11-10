


# pip install pycryptodome


# RSA Encryption and Decryption in Python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Step 1: Generate RSA keys (Public and Private)
key = RSA.generate(2048)  # 2048-bit key
public_key = key.publickey()
print("Public Key:", public_key.export_key().decode())
print("\nPrivate Key:", key.export_key().decode())

# Step 2: Create cipher using public key for encryption
cipher_encrypt = PKCS1_OAEP.new(public_key)

# Step 3: Input message
message = input("\nEnter message to encrypt: ").encode()

# Step 4: Encrypt the message
encrypted_msg = cipher_encrypt.encrypt(message)
print("\nEncrypted Message:", encrypted_msg)

# Step 5: Create cipher using private key for decryption
cipher_decrypt = PKCS1_OAEP.new(key)

# Step 6: Decrypt the message
decrypted_msg = cipher_decrypt.decrypt(encrypted_msg)
print("\nDecrypted Message:", decrypted_msg.decode())

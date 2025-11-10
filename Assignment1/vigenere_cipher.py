# VIGENERE CIPHER ENCRYPTION AND DECRYPTION

def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper()
    ciphertext = ""
    for i in range(len(plaintext)):
        c = (ord(plaintext[i]) + ord(key[i % len(key)]) - 2*65) % 26
        ciphertext += chr(c + 65)
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")
    key = key.upper()
    plaintext = ""
    for i in range(len(ciphertext)):
        c = (ord(ciphertext[i]) - ord(key[i % len(key)]) + 26) % 26
        plaintext += chr(c + 65)
    return plaintext

# MAIN
text = input("Enter text: ")
key = input("Enter key: ")

enc = vigenere_encrypt(text, key)
print("Encrypted:", enc)
print("Decrypted:", vigenere_decrypt(enc, key))

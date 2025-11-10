def encrypt_caesar(plaintext, shift):
    """
    Encrypts plaintext using the Caesar cipher.
    Handles both uppercase and lowercase letters.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Determine the base (ASCII value for 'A' or 'a')
            base = ord('A') if char.isupper() else ord('a')
            # Apply the shift, wrap around 26, and convert back to char
            ciphertext += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Keep non-alphabetic characters as they are
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext, shift):
    """
    Decrypts ciphertext from the Caesar cipher.
    It's the same as encrypting with a negative shift.
    """
    return encrypt_caesar(ciphertext, -shift)

message = input("Enter your message: ")

# Get user input for the shift and convert to an integer
# Note: This will show an error if you don't enter a number.
shift_str = input("Enter the shift value : ")
shift = int(shift_str)

# Perform encryption and decryption
encrypted = encrypt_caesar(message, shift)
decrypted = decrypt_caesar(encrypted, shift)

print("\n--- Results ---")
print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
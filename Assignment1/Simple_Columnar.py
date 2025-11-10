# --- 3. Simple Columnar Transposition (User Input) ---

def columnar_encrypt(text, key):
    """
    Encrypts text using Simple Columnar Transposition.
    """
    # Prepare text: uppercase and letters only
    text = "".join(c for c in text.upper() if 'A' <= c <= 'Z')
    key = key.upper()
    
    num_cols = len(key)
    
    # Get column read order from the key
    # This creates a list of column indexes in the order they should be read
    # e.g., key "CIPHER" (2,1,5,3,0,4) -> read_order [4, 1, 0, 3, 5, 2]
    read_order = [i[0] for i in sorted(enumerate(key), key=lambda x:x[1])]
    
    # Pad the text with 'X' so it fits the grid perfectly
    text += "X" * (-len(text) % num_cols)
    num_rows = len(text) // num_cols

    # Create the grid by splitting text into rows
    grid = [text[i*num_cols : (i+1)*num_cols] for i in range(num_rows)]

    # Read out the ciphertext column by column based on read_order
    ciphertext = ""
    for col_index in read_order:
        for row_index in range(num_rows):
            ciphertext += grid[row_index][col_index]
            
    return ciphertext

def columnar_decrypt(cipher, key):
    """
    Decrypts text from Simple Columnar Transposition.
    """
    key = key.upper()
    num_cols = len(key)
    num_rows = len(cipher) // num_cols

    # Get the column order (same as in encrypt)
    read_order = [i[0] for i in sorted(enumerate(key), key=lambda x:x[1])]
    
    # Create an empty grid
    grid = [["" for _ in range(num_cols)] for _ in range(num_rows)]

    # Fill the grid column by column in the key order
    cipher_iter = iter(cipher)
    for col_index in read_order:
        for row_index in range(num_rows):
            grid[row_index][col_index] = next(cipher_iter)
            
    # Read out the plaintext row by row
    return "".join("".join(row) for row in grid)

# --- Main execution with User Input ---

# Get user input for the message and key
message = input("Enter your message: ")
key = input("Enter the key (e.g., CIPHER): ")

# Perform encryption and decryption
encrypted = columnar_encrypt(message, key)
decrypted = columnar_decrypt(encrypted, key)

print("\n--- Results ---")
print("Original:", message)
print(f"Key: {key}")
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
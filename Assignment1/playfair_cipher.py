# PLAYFAIR CIPHER ENCRYPTION AND DECRYPTION

def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = []
    for ch in key:
        if ch not in used and ch.isalpha():
            used.append(ch)
    for ch in range(65, 91):  # A-Z
        if chr(ch) not in used and chr(ch) != 'J':
            used.append(chr(ch))
    matrix = [used[i:i+5] for i in range(0, 25, 5)]
    return matrix

def find_position(matrix, ch):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == ch:
                return i, j
    return None, None

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    i = 0
    pairs = []
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i+1] if i+1 < len(plaintext) else 'X'
        if a == b:
            pairs.append((a, 'X'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2

    ciphertext = ""
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            ciphertext += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            ciphertext += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            ciphertext += matrix[r1][c2] + matrix[r2][c1]
    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    ciphertext = ciphertext.upper()
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            plaintext += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            plaintext += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            plaintext += matrix[r1][c2] + matrix[r2][c1]
    return plaintext

# MAIN
text = input("Enter text: ")
key = input("Enter key: ")

enc = playfair_encrypt(text, key)
print("Encrypted:", enc)
print("Decrypted:", playfair_decrypt(enc, key))

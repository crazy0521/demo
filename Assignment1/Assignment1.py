# 1.Write a Python program to encrypt and decrypt text using the Play fair Cipher, Vignere Cipher, Simple columnar technique and Rail fence technique


import math

# -------------------------------------------
# PLAYFAIR CIPHER
# -------------------------------------------

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

# -------------------------------------------
# VIGENERE CIPHER
# -------------------------------------------

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

# -------------------------------------------
# SIMPLE COLUMNAR CIPHER
# -------------------------------------------

def columnar_encrypt(plaintext, key):
    col = len(key)
    row = math.ceil(len(plaintext) / col)
    matrix = [['' for _ in range(col)] for _ in range(row)]
    k = 0
    for i in range(row):
        for j in range(col):
            if k < len(plaintext):
                matrix[i][j] = plaintext[k]
                k += 1
    order = sorted(list(key))
    ciphertext = ""
    for ch in order:
        j = key.index(ch)
        for i in range(row):
            ciphertext += matrix[i][j]
    return ciphertext

def columnar_decrypt(ciphertext, key):
    col = len(key)
    row = math.ceil(len(ciphertext) / col)
    order = sorted(list(key))
    matrix = [['' for _ in range(col)] for _ in range(row)]
    k = 0
    for ch in order:
        j = key.index(ch)
        for i in range(row):
            if k < len(ciphertext):
                matrix[i][j] = ciphertext[k]
                k += 1
    plaintext = ""
    for i in range(row):
        for j in range(col):
            plaintext += matrix[i][j]
    return plaintext

# -------------------------------------------
# RAIL FENCE CIPHER
# -------------------------------------------

def rail_fence_encrypt(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0

    for ch in text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = ch
        col += 1
        row += 1 if dir_down else -1

    ciphertext = ""
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                ciphertext += rail[i][j]
    return ciphertext

def rail_fence_decrypt(ciphertext, key):
    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(key)]
    dir_down = None
    row, col = 0, 0

    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        result.append(rail[row][col])
        col += 1
        row += 1 if dir_down else -1

    return "".join(result)

# -------------------------------------------
# MAIN FUNCTION FOR DEMO
# -------------------------------------------

if __name__ == "__main__":
    text = "HELLO WORLD"
    key_playfair = "MONARCHY"
    key_vigenere = "KEY"
    key_columnar = "ZEBRA"
    key_rail = 3

    print("\n--- PLAYFAIR CIPHER ---")
    enc = playfair_encrypt(text, key_playfair)
    print("Encrypted:", enc)
    print("Decrypted:", playfair_decrypt(enc, key_playfair))

    print("\n--- VIGENERE CIPHER ---")
    enc = vigenere_encrypt(text, key_vigenere)
    print("Encrypted:", enc)
    print("Decrypted:", vigenere_decrypt(enc, key_vigenere))

    print("\n--- COLUMNAR CIPHER ---")
    enc = columnar_encrypt(text.replace(" ", ""), key_columnar)
    print("Encrypted:", enc)
    print("Decrypted:", columnar_decrypt(enc, key_columnar))

    print("\n--- RAIL FENCE CIPHER ---")
    enc = rail_fence_encrypt(text.replace(" ", ""), key_rail)
    print("Encrypted:", enc)
    print("Decrypted:", rail_fence_decrypt(enc, key_rail))

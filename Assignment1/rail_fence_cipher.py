






# RAIL FENCE CIPHER ENCRYPTION AND DECRYPTION

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

# MAIN
text = input("Enter text: ").replace(" ", "")
key = int(input("Enter key (number of rails): "))

enc = rail_fence_encrypt(text, key)
print("Encrypted:", enc)
print("Decrypted:", rail_fence_decrypt(enc, key))














# RSA Algorithm for Text Encryption and Decryption

import random
from math import gcd

# Function to check prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate random prime number
def generate_prime():
    while True:
        num = random.randint(100, 300)
        if is_prime(num):
            return num

# Step 1: Generate p and q
p = generate_prime()
q = generate_prime()

while p == q:
    q = generate_prime()

print("Generated Prime Numbers:")
print("p =", p)
print("q =", q)

# Step 2: Calculate n
n = p * q

# Step 3: Calculate phi
phi = (p - 1) * (q - 1)

# Step 4: Choose e
e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

# Step 5: Calculate d
d = 1
while (d * e) % phi != 1:
    d += 1

print("\nPublic Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Input text message
message = input("\nEnter message: ")

# Encryption
encrypted = []

for char in message:
    cipher = (ord(char) ** e) % n
    encrypted.append(cipher)

print("\nEncrypted Message:")
print(encrypted)

# Decryption
decrypted = ""

for cipher in encrypted:
    plain = (cipher ** d) % n
    decrypted += chr(plain)

print("\nDecrypted Message:")
print(decrypted)
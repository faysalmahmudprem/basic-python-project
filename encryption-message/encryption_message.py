import random
import string

# 1. Prepare characters
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)  # Shuffle for secret mapping

# 2. ENCRYPTION
plain_text = input("Enter a message to encrypt: ")
encrypted_text = ""

for letter in plain_text:
    if letter in chars:  # Only encrypt known characters
        index = chars.index(letter)
        encrypted_text += key[index]
    else:
        encrypted_text += letter  # Keep unknown characters as-is

print(f"\nOriginal message  : {plain_text}")
print(f"Encrypted message : {encrypted_text}")

# 3. DECRYPTION
cipher_input = input("\nEnter a message to decrypt: ")
decrypted_text = ""

for letter in cipher_input:
    if letter in key:
        index = key.index(letter)
        decrypted_text += chars[index]
    else:
        decrypted_text += letter  # Keep unknown characters as-is

print(f"\nEncrypted message : {cipher_input}")
print(f"Decrypted message : {decrypted_text}")

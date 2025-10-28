"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""

def caesar_cipher(message:str, shift:int) -> str:
    result = ""

    for c in message:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            coded_char = chr((ord(c) - base + shift) % 26 + base)
            result += coded_char
        else:
            result += c
    
    return result

def decipher(message:str, shift:int) -> str:
    return caesar_cipher(message, -shift)

def main():
    print("-----Welcome-----")

    choice = input("Please enter E for encrypt or D for decrypt: ").strip().upper()

    while choice != 'E' and choice != 'D':
        choice = input("Please chose E or D only: ").strip().upper()
    
    encrypt_template = 'Encrypted' if choice == 'E' else 'Decrypted'

    message = input(f"Please enter message to be {encrypt_template}: \n")

    while True:
        try:
            key = int(input("Enter the key to encrypt in the range of 0 - 25: ").strip())
            break
        except ValueError:
            print("Enter a valid integer")
    
    print(f"Here's your {encrypt_template} message: ")
    if choice == 'E':
        print(caesar_cipher(message, key))
    else:
        print(decipher(message, key))

main()
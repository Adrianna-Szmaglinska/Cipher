import random

def simple_substitution_cipher_encrypt(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shuffled_alphabet = ''.join(random.sample(alphabet, len(alphabet)))
    mapping = {alphabet[i]: shuffled_alphabet[i] for i in range(len(alphabet))}
    encrypted_text = ''.join(mapping.get(char, char) for char in text)
    return encrypted_text

while True:
    text = input("Enter the message to encrypt (or type 'exit' to quit): ")
    if text.lower() == 'exit':
        print()
        print("Goodbye! :)")
        break
    encrypted_text = simple_substitution_cipher_encrypt(text)
    print("Encrypted message:", encrypted_text)
    print()

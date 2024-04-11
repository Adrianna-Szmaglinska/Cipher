def vigenere_cipher_encrypt(text, key):
    encrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text

while True:
    text = input("Enter the message to encrypt (or type 'exit' to quit): ")
    if text.lower() == 'exit':
        print("Goodbye! :)")
        break
    key = input("Enter the key: ")
    encrypted_text = vigenere_cipher_encrypt(text, key)
    print("Encrypted message:", encrypted_text)
    print()

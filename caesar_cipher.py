def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

while True:
    text = input("Enter the message to encrypt (or type 'exit' to quit): ")
    if text.lower() == 'exit':
        print()
        print("Goodbye! :)")
        break
    shift = int(input("Enter the shift value: "))
    encrypted_text = caesar_cipher_encrypt(text, shift)
    print("Encrypted message:", encrypted_text)
    print()

<!DOCTYPE html>
<html>

<head>
    <title>Python Cipher Library</title>
</head>

<body>

    <h1>Python Cipher Library</h1>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#introduction">Introduction</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#roadmap">Roadmap</a></li>
        <li><a href="#contribution">Contribution</a></li>
        <li><a href="#phase-2-decryption-algorithms">Phase 2: Decryption Algorithms</a></li>
    </ul>

    <h2 id="introduction">Introduction</h2>

    <p>Welcome to the Python Cipher Library! This project aims to provide a collection of encryption algorithms implemented
        in Python. Currently, the library supports the following ciphers:</p>

    <ul>
        <li>Caesar Cipher</li>
        <li>Vigenère Cipher</li>
        <li>Simple Substitution Cipher</li>
    </ul>

    <h2 id="installation">Installation</h2>

    <p>You can install the library using pip:</p>

    <pre><code>pip install python-cipher-library</code></pre>

    <h2 id="usage">Usage</h2>

    <h3>Caesar Cipher</h3>

    <p>Here's an example demonstrating how to use the Caesar Cipher:</p>

    <pre><code>def caesar_cipher_encrypt(text, shift):
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
</code></pre>

    <h2 id="roadmap">Roadmap</h2>

    <p>We are planning to add more encryption algorithms to this library in the future. Here's what you can expect in
        upcoming releases:</p>

    <ul>
        <li>Atbash Cipher</li>
        <li>ROT13</li>
        <li>Rail Fence Cipher</li>
        <li>Playfair Cipher</li>
        <li>Hill Cipher</li>
        <li>Enigma Machine</li>
        <li>RSA Algorithm</li>
    </ul>

    <h2 id="contribution">Contribution</h2>

    <p>Contributions are welcome! If you have suggestions for new features or find any issues, please open an issue or
        submit a pull request.</p>

    <h2 id="phase-2-decryption-algorithms">Phase 2: Decryption Algorithms</h2>

    <p>In Phase 2 of this project, we will focus on implementing decryption algorithms to complement our existing
        encryption algorithms. Stay tuned for updates!</p>

</body>

</html>

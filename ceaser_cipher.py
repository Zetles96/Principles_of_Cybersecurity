def encrypt(plain_text: str, shift: int) -> str:
    cipher_text = ""
    for char in plain_text:
        if not char.isalpha():
            cipher_text += char
            continue
        if char.isupper():
            shift_char = chr((ord(char) + shift - 65) % 26 + 65)
        else:
            shift_char = chr((ord(char) + shift - 97) % 26 + 97)
        cipher_text += shift_char

    return cipher_text


def decrypt(cipher_text: str, shift: int) -> str:
    plain_text = ""
    for char in cipher_text:
        if not char.isalpha():
            plain_text += char
            continue
        if char.isupper():
            shift_char = chr((ord(char) - shift - 65) % 26 + 65)
        else:
            shift_char = chr((ord(char) - shift - 97) % 26 + 97)
        plain_text += shift_char

    return plain_text


def decrypt_all(cipher_text: str) -> None:
    for i in range(26):
        decrypted = decrypt(cipher_text, i)
        print(f"{i}:\t{decrypted}")


if __name__ == '__main__':
    text = "Jmpwfzpv4111"
    decrypt_all(text)

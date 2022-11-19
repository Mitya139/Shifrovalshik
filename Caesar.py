def encrypt_caesar_text_eng(text, key):
    first_ord = ord('a')
    last_ord = ord('z')
    text = text.lower()
    text_encrypt = ''
    n = 26
    for ch in text:
        if 'z' >= ch >= 'a':
            text_encrypt += chr((ord(ch) - last_ord - 1 + key) % n + first_ord)
        else:
            text_encrypt += ch
    return text_encrypt


def decrypt_caesar_text_eng(text, key):
    return encrypt_caesar_text_eng(text, -key)


def encrypt_caesar_text_rus(text, key):
    first_ord = ord('а')
    last_ord = ord('я')
    text = text.lower()
    text_encrypt = ''
    n = 32
    for ch in text:
        if 'я' >= ch >= 'а':
            text_encrypt += chr((ord(ch) - last_ord - 1 + key) % n + first_ord)
        else:
            text_encrypt += ch
    return text_encrypt


def decrypt_caesar_text_rus(text, key):
    return encrypt_caesar_text_rus(text, -key)


def encrypt_caesar_file(way_to_file, key):
    f = open(way_to_file, 'rb')
    n = 256
    bs = f.read()
    encrypt_bs = []
    for bit in bs:
        encrypt_bs.append((bit + key) % n)
    f.close()
    f = open(way_to_file, 'wb')
    f.write(bytes(encrypt_bs))
    f.close()


def decrypt_caesar_file(way_to_file, key):
    encrypt_caesar_file(way_to_file, -key)


encrypt_caesar_file('abc.docx', 9)

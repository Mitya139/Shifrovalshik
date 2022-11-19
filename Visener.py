def encrypt_visener_text_eng(text, key_word, mult=1):
    first_ord = ord('a')
    last_ord = ord('z')
    text = text.lower()
    key_word = key_word.lower()
    text_encrypt = ''
    n = 26
    index_of_key = 0
    for ch in text:
        if 'z' >= ch >= 'a':
            key = ord(key_word[index_of_key % len(key_word)]) - first_ord
            index_of_key += 1
            text_encrypt += chr((ord(ch) - last_ord - 1 + key * mult) % n + first_ord)
        else:
            text_encrypt += ch
    return text_encrypt


def decrypt_visener_text_eng(text, key_word):
    return encrypt_visener_text_eng(text, key_word, -1)


def encrypt_visener_text_rus(text, key_word, mult=1):
    first_ord = ord('а')
    last_ord = ord('я')
    text = text.lower()
    key_word = key_word.lower()
    text_encrypt = ''
    n = 32
    index_of_key = 0
    for ch in text:
        if 'я' >= ch >= 'а':
            key = ord(key_word[index_of_key % len(key_word)]) - first_ord
            text_encrypt += chr((ord(ch) - last_ord - 1 + key * mult) % n + first_ord)
        else:
            text_encrypt += ch
        index_of_key += 1
    return text_encrypt


def decrypt_visener_text_rus(text, key_word):
    return encrypt_visener_text_rus(text, key_word, -1)


def encrypt_visener_file(way_to_file, key_word, mult=1):
    f = open(way_to_file, 'rb')
    n = 256
    bs = f.read()
    key_word = key_word.lower()
    encrypt_bs = []
    index_of_key = 0
    for bit in bs:
        key = ord(key_word[index_of_key % len(key_word)])
        encrypt_bs.append((bit + key*mult) % n)
        index_of_key += 1
    f.close()
    f = open(way_to_file, 'wb')
    f.write(bytes(encrypt_bs))
    f.close()


def decrypt_visener_file(way_to_file, key_word):
    encrypt_visener_file(way_to_file, key_word, -1)

import Visener


def encrypt_vernam_text_rus(text, key_text):
    if len(text) == len(key_text):
        Visener.encrypt_visener_text_rus(text, key_text)


def encrypt_vernam_text_eng(text, key_text):
    if len(text) == len(key_text):
        Visener.encrypt_visener_text_eng(text, key_text)


def decrypt_vernam_text_eng(text, key_text):
    if len(text) == len(key_text):
        Visener.encrypt_visener_text_eng(text, key_text, mult=-1)


def decrypt_vernam_text_rus(text, key_text):
    if len(text) == len(key_text):
        Visener.encrypt_visener_text_rus(text, key_text, mult=-1)

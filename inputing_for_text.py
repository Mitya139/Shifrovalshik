import Outputing
import Caesar
import Visener


def caesar_cipher_end(language, text, key, decrypt=False):
    print('\033[32m\033[01mЗашифрованный текст:')
    if language == 'eng':
        if decrypt:
            print(Caesar.decrypt_caesar_text_eng(text, key))
        else:
            print(Caesar.encrypt_caesar_text_eng(text, key))
    elif language == 'rus':
        if decrypt:
            print(Caesar.decrypt_caesar_text_rus(text, key))
        else:
            print(Caesar.encrypt_caesar_text_rus(text, key))


def visener_cipher_end(language, text, key, decrypt=False):
    print('\033[32m\033[01mЗашифрованный текст:')
    if language == 'eng':
        if decrypt:
            print(Visener.decrypt_visener_text_eng(text, key))
        else:
            print(Visener.encrypt_visener_text_eng(text, key))
    elif language == 'rus':
        if decrypt:
            print(Visener.decrypt_visener_text_rus(text, key))
        else:
            print(Visener.decrypt_visener_text_rus(text, key))


def caesar_text_input(language, decrypt=False):
    print('\033[35m\033[01mВведите текст:')
    text = input()
    key_input_caesar_text(language, text, decrypt)


def visener_text_input(language, decrypt=False):
    print('\033[35m\033[01mВведите текст:')
    text = input()
    print('\033[35m\033[01mВведите ключ:')
    key = input()
    visener_cipher_end(language, text, key, decrypt)


def key_input_caesar_text(language, text, decrypt=False):
    Outputing.key_output()
    key = input()
    try:
        key = int(key)
        caesar_cipher_end(language, text, key, decrypt)
    except ValueError:
        print('\033[31mНекорректный ключ')
        key_input_caesar_text(language, text, decrypt)


def cipher_text_choice(language, decrypt=False):
    Outputing.output_text()
    cipher_text_in = input()
    if cipher_text_in == '1':
        caesar_text_input(language, decrypt)
    elif cipher_text_in == '2':
        visener_text_input(language, decrypt)
    elif cipher_text_in == '3':
        visener_text_input(language, decrypt)
    else:
        print('\033[31mНекорректный ввод')
        cipher_text_choice(language, decrypt)


def language_in_out(decrypt=False):
    Outputing.language_choice()
    language_in = input()
    if language_in == '1':
        cipher_text_choice('rus', decrypt)
    elif language_in == '2':
        cipher_text_choice('eng', decrypt)
    else:
        print('\033[31mНекорректный ввод')
        language_in_out(decrypt)

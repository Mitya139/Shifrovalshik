import Outputing
import Caesar
import Visener


def caesar_cipher_end(language, text, key):
    print('Зашифрованный текст:')
    if language == 'eng':
        print(Caesar.encrypt_caesar_text_eng(text, key))
    elif language == 'rus':
        print(Caesar.encrypt_caesar_text_rus(text, key))


def visener_cipher_end(language, text, key):
    print('Зашифрованный текст:')
    if language == 'eng':
        print(Visener.encrypt_visener_text_eng(text, key))
    elif language == 'rus':
        print(Visener.decrypt_visener_text_rus(text, key))


def caesar_text_input(language):
    print('Введите текст:')
    text = input()
    key_input_caesar_text(language, text)


def visener_text_input(language):
    print('Введите текст:')
    text = input()
    print('Введите ключ:')
    key = input()
    visener_cipher_end(language, text, key)


def key_input_caesar_text(language, text):
    Outputing.key_output()
    key = input()
    try:
        key = int(key)
        caesar_cipher_end(language, text, key)
    except ValueError:
        print('Некорректный ключ')
        key_input_caesar_text(language, text)


def cipher_text_choice(language):
    Outputing.output_text()
    cipher_text_in = input()
    text_for_encryption = ''
    if cipher_text_in == '1':
        caesar_text_input(language)
    elif cipher_text_in == '2':
        visener_text_input(language)
    elif cipher_text_in == '3':
        visener_text_input(language)
    else:
        print('Некорректный ввод')
        cipher_text_choice(language)


def language_in_out():
    Outputing.language_choice()
    language_in = input()
    if language_in == '1':
        cipher_text_choice('rus')
    elif language_in == '2':
        cipher_text_choice('eng')
    else:
        print('Некорректный ввод')
        language_in_out()
import Outputing
import Caesar
import Visener


def end_way_to_file_in(decrypt=False):
    print('Введите путь к файлу:')
    way_to_file = input()
    try:
        f = open(way_to_file, 'rb+')
        f.close()
        cipher_file_choice(way_to_file, decrypt)
    except PermissionError:
        print('\033[31mНет доступа')
        end_way_to_file_in(decrypt)
    except FileNotFoundError:
        print("\033[31mФайл не найден")
        end_way_to_file_in(decrypt)
    except OSError:
        print('\033[31mВведите что-то адекватное')
        end_way_to_file_in(decrypt)


def caesar_cipher_file_end(way_to_file, key, decrypt=False):
    if decrypt:
        Caesar.decrypt_caesar_file(way_to_file, key)
        print('\033[32m\033[01mРасшифровка удалась :)))')
    else:
        Caesar.encrypt_caesar_file(way_to_file, key)
        print('\033[32m\033[01mШифрование завершено :)')


def caesar_key_files(way_to_file, decrypt=False):
    Outputing.key_output()
    key = input()
    try:
        key = int(key)
        caesar_cipher_file_end(way_to_file, key, decrypt)
    except ValueError:
        print('\033[31mНекорректный ключ')
        caesar_key_files(way_to_file, decrypt)


def visener_cipher_file_end(way_to_file, decrypt=False):
    Outputing.key_output()
    key = input()
    if decrypt:
        Visener.decrypt_visener_file(way_to_file, key)
        print('\033[32m\033[01mРасшифровка удалась :)))')
    else:
        Visener.encrypt_visener_file(way_to_file, key)
        print('\033[32m\033[01mШифрование завершено :)')


def cipher_file_choice(way_to_file, decrypt=False):
    Outputing.output_files()
    cipher_files_in = input()
    if cipher_files_in == '1':
        caesar_key_files(way_to_file, decrypt)
    elif cipher_files_in == '2':
        visener_cipher_file_end(way_to_file, decrypt)
    else:
        print('\033[31mНекорректный ввод')
        cipher_file_choice(way_to_file, decrypt)

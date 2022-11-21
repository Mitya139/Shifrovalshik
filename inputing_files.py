import Outputing
import Caesar
import Visener


def end_way_to_file_in():
    print('Введите путь к файлу:')
    way_to_file = input()
    try:
        f = open(way_to_file, 'rb+')
        f.close()
        cipher_file_choice(way_to_file)
    except PermissionError:
        print('Нет доступа')
        end_way_to_file_in()
    except FileNotFoundError:
        print("Файл не найден")
        end_way_to_file_in()
    except OSError:
        print('Введите что-то адекватное')
        end_way_to_file_in()


def caesar_cipher_file_end(way_to_file, key):
    Caesar.encrypt_caesar_file(way_to_file, key)
    print('Шифрование завершено :)')


def caesar_key_files(way_to_file):
    Outputing.key_output()
    key = input()
    try:
        key = int(key)
        caesar_cipher_file_end(way_to_file, key)
    except ValueError:
        print('Некорректный ключ')
        caesar_key_files(way_to_file)


def visener_cipher_file_end(way_to_file):
    Outputing.key_output()
    key = input()
    Visener.encrypt_visener_file(way_to_file, key)


def cipher_file_choice(way_to_file):
    Outputing.output_files()
    cipher_files_in = input()
    if cipher_files_in == '1':
        caesar_key_files(way_to_file)
    elif cipher_files_in == '2':
        visener_cipher_file_end(way_to_file)
    else:
        print('Некорректный ввод')
        cipher_file_choice(way_to_file)
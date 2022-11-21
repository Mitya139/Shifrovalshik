import Outputing
import Caesar
import Visener
import inputing_for_text


def end_way_to_file_in():
    print('Введите путь к файлу:')
    way_to_file = input()
    try:
        f = open(way_to_file, 'rb+')
        f.close()
    except PermissionError:
        print('Нет доступа')
        end_way_to_file_in()
    except FileNotFoundError:
        print("Файл не найден")
        end_way_to_file_in()
    except OSError:
        print('Введите что-то адекватное')
        end_way_to_file_in()
    return way_to_file


def cipher_file_choice():
    Outputing.output_files()
    cipher_files_in = input()
    if cipher_files_in == '1':
        pass
    elif cipher_files_in == '2':
        pass
    else:
        print('Некорректный ввод')
        cipher_file_choice()


def start_in_out():
    Outputing.start_output()
    first_in = input()
    if first_in == '1':
        inputing_for_text.language_in_out()
    elif first_in == '2':
        cipher_file_choice()
    else:
        print('Некорректный ввод')
        start_in_out()


start_in_out()

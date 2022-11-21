import Outputing


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


def cipher_text_choice(language):
    Outputing.output_text()
    cipher_text_in = input()
    text_for_encryption = ''
    if cipher_text_in == '1':
        pass
    elif cipher_text_in == '2':
        pass
    elif cipher_text_in == '3':
        pass
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
        language_in_out()
    elif first_in == '2':
        cipher_file_choice()
    else:
        print('Некорректный ввод')
        start_in_out()


start_in_out()

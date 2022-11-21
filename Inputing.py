import Outputing
import inputing_for_text
import inputing_files


def start_in_out():
    Outputing.start_output()
    first_in = input()
    if first_in == '1':
        inputing_for_text.language_in_out()
    elif first_in == '2':
        inputing_files.end_way_to_file_in()
    elif first_in == '3':
        inputing_for_text.language_in_out(True)
    elif first_in == '4':
        inputing_files.end_way_to_file_in(True)
    else:
        print('\033[31mНекорректный ввод')
        start_in_out()


def end_in_out():
    Outputing.end_output()
    end_in = input()
    if end_in == '1':
        start_in_out()
        end_in_out()
    if end_in == '2':
        pass

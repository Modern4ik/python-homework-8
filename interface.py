import os
import msvcrt as ms
import operation as oper

def get_value_from_user(message):
    flag = True

    while flag:
        try:
            os.system('cls')

            print_menu()

            print()
            print(message)
            user_input = int(ms.getch())

            if 1 <= user_input <= 7:
                flag = False
            else:
                raise ValueError

        except ValueError:
            os.system('cls')

            print('Вы должны выбрать номер пункта из меню!')

            print()
            print('Нажмите любую кнопку для возврата к меню...')
            ms.getch()

    return user_input

def print_menu():
    print('1 - Показать контакты', '\n'
          '2 - Добавить контакт', '\n'
          '3 - Найти контакт', '\n'
          '4 - Изменить контакт', '\n'
          '5 - Удалить контакт', '\n'
          '6 - Удалить все контакты', '\n'
          '7 - Выход')
    
def make_operation_with_file(user_input):
    match user_input:
        case 1:
            oper.show_contacts()
            return True
        case 2:
            oper.add_contact()
            return True
        case 3:
            oper.find_contact()
            return True
        case 4:
            oper.change_contact()
            return True
        case 5:
            oper.remove_contact()
            return True
        case 6:
            oper.remove_all_contacts()
            return True
        case 7:
            os.system('cls') 
            return False
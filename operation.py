import os
import msvcrt as ms
import string


def show_contacts():
    os.system('cls')

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        print(file.read())
    
    print()
    print('Файл "phonebook.txt" успешно прочтён!')

    print()
    print('Нажмите любую кнопку для возврата к меню...')
    ms.getch()

def add_contact():
    os.system('cls')

    name = input('Введите Имя(ФИО): ').capitalize()
    phone = input('Введите номер телефона(+7): ').capitalize()
    comment = input('Введите комментарий: ').capitalize()

    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(name)
        file.write(" - " + phone)
        file.write(" - " + comment + '\n')

    print()
    print(f'Контакт успешно добавлен!')

    print()
    print('Нажмите любую кнопку для возврата к меню...')
    ms.getch()

def find_contact():
    flag = True
    
    while flag:
        os.system('cls')

        check = input('Введите ключевое слово/числа для поиска, длина которого больше или равна двум: ').lower()

        if len(check) >= 2 and check.replace(" ", "") != '':
            flag = False
        else:
            print()
            print('Длина ключевого слово/числа для поиска должна быть больше или равна двум!')

            print()
            print('Нажмите Enter для повтора попытки...')
            ms.getch()


    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        print()
        flag = False

        for i in file.readlines():
            if check in i.lower():
                print(i)
                flag = True
            else:
                continue
    
    if flag:
        print()
        print('По данному ключевому слову/числу были найдены вышеперечисленные контакты!')
    else:
        print('По данному ключевому слову/числу не найдено совпадений!')

    print()
    print('Нажмите любую кнопку для возврата к меню...')
    ms.getch()

def change_contact():
    os.system('cls')

    with open('phonebook.txt', 'r' , encoding='UTF-8') as file:
        print(file.read())

    with open('phonebook.txt', 'r' , encoding='UTF-8') as file:   
        strings_lst = file.readlines()
    
    input_flag = True

    while input_flag:
        print()
        user_input = input('Введите полное имя контакта из списка, который вы хотите заменить: ').capitalize()

        if user_input.replace(' ', '') != '':
            input_flag = False
        else:
            print()
            print('Введите искомое имя контакта!')

    with open('phonebook.txt', 'w' , encoding='UTF-8') as file:
        flag = True

        for i in range(0, len(strings_lst)):
            for word in strings_lst[i].split(' - '):
                if user_input == word:
                    flag = False

                    name = input('Введите новое Имя(ФИО): ')
                    phone = input('Введите новый номер телефона(+7): ')
                    comment = input('Введите новый комментарий: ')

                    strings_lst[i] = name + ' - ' + phone + ' - ' + comment + '\n'

                    print()
                    print(f'Контакт успешно добавлен!')

                    print()
                    print('Нажмите любую кнопку для возврата к меню...')
                    ms.getch()
        
        file.writelines(strings_lst)

    if flag:
        print()
        print('Контакт с таким именем для изменения не найден!')

        print()
        print('Нажмите любую кнопку для возврата к меню...')
        ms.getch()
        
def remove_contact():
    os.system('cls')

    with open('phonebook.txt', 'r' , encoding='UTF-8') as file:
        print(file.read())

    with open('phonebook.txt', 'r' , encoding='UTF-8') as file:   
        strings_lst = file.readlines()

    input_flag = True

    while input_flag:
        print()
        user_input = input('Введите полное имя контакта из списка, который вы хотите удалить: ').capitalize()

        if user_input.replace(' ', '') != '':
            input_flag = False
        else:
            print()
            print('Введите искомое имя контакта!')

    with open('phonebook.txt', 'w' , encoding='UTF-8') as file:
        flag = True

        for i in range(0, len(strings_lst)):
            for word in strings_lst[i].split(' - '):
                if user_input == word:
                    flag = False

                    strings_lst.remove(strings_lst[i])

                    print()
                    print(f'Контакт успешно удалён!')

                    print()
                    print('Нажмите любую кнопку для возврата к меню...')
                    ms.getch()
                    break
        
        file.writelines(strings_lst)

    if flag:
        print()
        print('Контакт с таким именем для изменения не найден!')

        print()
        print('Нажмите любую кнопку для возврата к меню...')
        ms.getch()

def remove_all_contacts():
    os.system('cls')

    print('Вы уверены, что хотите удалить ВСЕ контакты?')

    print()
    user_input = input('Если "Да" - введите цифру "9", если "Нет" - введите цифру "1": ')
                       
    input_flag = True

    while input_flag:
        if user_input == '9':
            with open('phonebook.txt', 'w', encoding='UTF-8') as file:
                print('Вы успешно удалили все контакты!')
            
            input_flag = False
        elif user_input == '1':
            return
        else:
            print('Вы должны ввести "9"(Да) или "1"(Нет)')
            
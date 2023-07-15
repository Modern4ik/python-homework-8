import interface as inter
import operation as oper

flag = True

while flag:
    user_value = inter.get_value_from_user('Выберите пункт меню: ')

    flag = inter.make_operation_with_file(user_value)
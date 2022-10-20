def print_data(data):
    print(data)

def input_data(data):
    print(f'{data}')



def check_phone():
    flag = False
    while flag == False:
        phone = input("Телефон: +7 ")
        if phone.isdigit():
            flag = True
            return phone
        else:
            print("Некорректный ввод, повторите попытку.")

def input_name_directory():
    phone = check_phone()
    surname = input("Фамилия: ")
    name = input("Имя: ")
    patronymic = input("Отчество: ")
    return f'Телефон: +7{phone}, Фамилия: {surname} Имя: {name} Отчество: {patronymic}'

def input_check_choice(text):
    flag = False
    while flag == False:
        user_answer = input(text)
        try:
            int(user_answer)
            if 0 < int(user_answer) < 6:
                return int(user_answer)
            else:
                flag == False
        except ValueError:
            flag == False

def find_data():
    f_data = input("Введите данные человека для поиска: ")
    return f_data
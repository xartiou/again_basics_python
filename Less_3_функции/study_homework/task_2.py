"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
        имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def data_user(f_name, l_name, b_day, city, email, num_phone):
    return f'Имя: {f_name}, Фамилия: {l_name}, Дата рождения: {b_day}, Город проживания: {city}, Email:{email}, ' \
           f'Телефон: {num_phone} '


print(data_user(f_name=input("Введите ваше имя: "),
                l_name=input("Введите вашу фамилию: "),
                b_day=input("Введите дату рождения: "),
                city=input("Введите город проживания: "),
                email=input("Введите ваш email: "),
                num_phone=input("Введите ваш номер телефона: ")))


# ещё вариант

def print_data(**kwargs):
    return ' '.join(kwargs.values())


print(print_data(name=input('Enter your name: '),
                 surname=input('Enter your surname: '),
                 birth_year=input('Enter you birth year: '),
                 city=input('Enter your city: '),
                 email=input('Enter your email: '),
                 phone=input('Enter your phone number: ')))

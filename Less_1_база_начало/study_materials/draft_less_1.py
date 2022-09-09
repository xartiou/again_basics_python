# Знакомство с ветвлениями

orig_password = 'x973'  # правильный пароль хранится в программе
password = input('Введите пароль: ')  # Просим пользователя ввести пароль
access = False  # переменная хранит разрешение на доступ
# один вариант
if password == orig_password:  # если при вводе правильный пароль
    print("Пароль принят, заходи!")
    access = True

if password != orig_password:  # если введен не правильный пароль
    print("Пароль не верный! Стреляю!")

# другой вариант
if password == orig_password:  # если при вводе правильный пароль
    print("Пароль принят, заходи!")
    access = True
else:  # иначе если введен не правильный пароль
    print("Пароль не верный! Стреляю!")


# вложенные инструкции
color = 'red'
if color == 'blue':
    print('синий')
elif color == 'red':
    print('красный')
elif color == 'green':
    print('зелёный')
else:
    print('Неизвестный цвет')


numb_1 = int(input('Введите первое целое число: '))
numb_2 = int(input('Введите второе целое число: '))

if numb_1 != numb_2:
    print('Числа не равны.')
    if numb_1 > numb_2:
        print("Первое число больше")
    else:
        print("Второе число Больше")
else:
    print("Введенные числа равны")

# Знакомство с циклами
# Цикл - многократное выполнение оператора

number = int(input('Введите целое число от 0 до 9: '))

while number < 10:
    print(number)
    number = number +1
print("Программа завершена успешно")


# break & continue

i = 0
while True:
    i += 1
    if i >= 10:
        break
    if i % 2 == 0:
        continue
    print(i)


# форматирование строк
# оператор форматирования %
name = input('Enter your name:')
print('Hello, %s!' % name)


# метод format()
print('{:>20} {:>20} {:>20}'.format('my_param_1', 'my_param_2', 'my_param_3'))

# f-string
ip = '192.168.1.4'
mask = 10
print(f"ip-params: {ip}, mask: {mask}.")

oct_1, oct_2, oct_3, oct_4 = [10, 15, 16, 9]
print(f'''IP-address: {oct_1:>4}.{oct_2:>4}.{oct_3:>4}.{oct_4:>4}.''')

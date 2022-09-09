"""
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""
n = input('Введите целое число n: ')
nn = n + n
nnn = n + n + n

sum_n = int(n) + int(nn) + int(nnn)
print(f"nn = {nn}")
print(f"nnn = {nnn}")
print(f"Сумма чисел n + nn + nnn = {sum_n}")
print(n.__class__)
print(sum_n.__class__)

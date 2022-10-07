"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

"""
with open('task_5.txt', 'w', encoding='utf8') as new_file:
    new_file.write(f"{' '.join([str(i) for i in range(1, 21)])}")

with open('task_5.txt', 'r', encoding='utf8') as task_file:
    numbers = [int(i) for i in task_file.read().split()]
    print(f"Сумма чисел в файле равна : {sum(numbers)}")
"""


with open("text_5.txt", "w+", encoding="utf-8") as f:
    f.write(" ".join([str(randint(1, 1000)) for _ in range(10000)]))
    f.seek(0)  # перемещаем офсет в начало файла
    # при помощи map() читаем и суммируем каждый объект
    print(f"Сумма чисел в файле равна : {sum(map(int, f.readline().split()))}")

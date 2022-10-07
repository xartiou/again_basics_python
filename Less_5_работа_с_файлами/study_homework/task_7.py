"""
7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

my_task = dict()
average_profit = 0
num = 1

with open('task_7.txt', 'r', encoding='utf8') as read_file:
    for line in read_file:
        name, forma, income, cost = line.split()
        profit = int(income) - int(cost)
        if profit >= 0:
            average_profit += profit
            num += 1
            my_task[name] = profit
average_profit /= num

with open('json_7.json', 'w', encoding='utf8') as write_json:
    json.dump([my_task, {'Средняя прибыль': average_profit}], write_json, ensure_ascii=False)


"""
# Вариант решения

with open("my_ex7.json", "w", encoding="utf-8") as write_file:
    with open("text_7.txt", encoding="utf-8") as read_file:
        dictionary = {string.split()[0]: int(string.split()[2]) - int(string.split()[3]) for string in read_file}
        average_profit_lst = []
        for n in dictionary.values():
            if n > 0:
                average_profit_lst.append(n)
        dump([dictionary, {"average_profit": sum(average_profit_lst) / len(average_profit_lst)}], write_file,
             ensure_ascii=False, indent=4)
"""
"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

file_salary = open('salary_worker.txt', 'w', encoding='utf8')
salary_list = [
    'Иванов 23500\n',
    'Петров 19700\n',
    'Сидоров 18400\n',
    'Ерёменко 21200'
]
file_salary.writelines(salary_list)
file_salary.close()


def task_3():
    salary = {}
    try:
        with open('salary_worker.txt', 'r', encoding='utf8') as f:
            for line in f:
                salary[line.split()[0]] = float(line.split()[1])
        print("Меньше 20000 получают: ")
        for name, sal in salary.items():
            if sal < 20000:
                print(name)
        print(f'Средняя зарплата всех рабочих равна {sum(salary.values()) / len(salary)}')
    except IOError:
        print('Бухгалтер сбежал с ведомостью.')
    except:
        print('Что-то пошло не так')


task_3()

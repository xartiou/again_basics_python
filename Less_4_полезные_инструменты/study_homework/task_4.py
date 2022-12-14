"""
4. Представлен список чисел.
Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
# через for для тренировки и понимания генератора
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
task_list = []
for i in my_list:
    if my_list.count(i) == 1:
        task_list.append(i)
print(task_list)

# и через генератор
print([i for i in my_list if my_list.count(i) == 1])

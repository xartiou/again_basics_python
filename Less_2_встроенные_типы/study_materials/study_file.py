""" Тип данных str """

my_str = "simple string"
print(my_str)
print(type(my_str))

'''конкатенация'''
string_1 = 'cadabra'
string_2 = 'abra'
print(string_2 + string_1)

'''взятие по индексу'''
print(string_2[1])

'''Извлечение среза'''
s = 'abracadabra'

print(s[2:6:2])
print(s[:])
print(s[:-1])
print(s[::-1])

'''Реверс на месте'''
s_reverse = ''
symbols = list(s)  # функция переводит в список символов ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']
# print(len(s))
for el in range(len(s) // 2):
    tmp = symbols[el]
    symbols[el] = symbols[len(s) - el - 1]
    symbols[len(s) - el - 1] = tmp
s_reverse = ''.join(symbols)
print(s_reverse)

'''Таблица методов строк'''
len(s)
s.join('')
s.split()
s.title()
s.upper()
s.lower()
s.istitle()
s.isupper()
s.islower()
s.count('a')
s.capitalize()
s.startswith('ab')

'''Тип данных: список'''
# result_list.append(el)        Добавить элемент el в конец списка result_list
# result_list.extend(my_list)   Расширить список result_list — добавить в конец элементы списка my_list
# result_list.insert(pos, el)   Разместить на позиции pos (индекс элемента списка) элемент el
# result_list.remove(el)        Удалить из списка первый элемент со значением el
# result_list.pop(pos)          Удалить элемент с индексом pos
# result_list.index(el)         Получить позицию (индекс) первого элемента со значением el
# result_list.count(el)         Возвращает количество элементов списка со значением el
# result_list.sort([key=функция]) Выполнить сортировку списка на основе указанной функции
# result_list.reverse()         Выполнить реверс списка (развернуть список)
# result_list.copy()            Вернуть копию списка
# result_list.clear()           Очистить список


'''Тип данных: словарь'''

# .keys() Возвращает список ключей словаря
# .values() Возвращает список значений
# .items() Возвращает список кортежей (ключ, значение)
# .get(key) Возвращает значение, соответствующее ключу key. Если ключ отсутствует, возвращает значение None
# .popitem() Удаляет элемент словаря и возвращает пару (ключ, значение). Если элементы отсутствуют- KeyError
# .setdefault(key) Возвращает значение, соответствующее ключу. Если ключ отсутствует, создаётся элемент  None
# .pop(key) Удаляет ключ и возвращает значение, соответствующее ключу
# .update(new_dict) Добавляет пары (ключ, значение) в текущий словарь из словаря new_dict и перезаписываются
# .copy() Возвращает копию словаря
# .clear() Очищает словарь

my_dict = {'title': 'Samsung Galaxy', 'price': 20000, 'country': 'China', 'year': '2016'}
for key, value in my_dict.items():
    print(f"{key} - {value}")

'''Тип данных: NoneType'''

my_dict = {'name': 'Ivan', 'surname': 'Ivanov', 'age': 40, 'position': None}
for el in my_dict:
    if my_dict[el] is None:
        print(f"Для сотрудника пока не определён параметр: {el}")


'''Десятка лучших трюков в Python'''

# Объединение списков без цикла
my_list = [[10, 20, 30], [40, 50], [60], [70, 80, 90]]
print(sum(my_list, []))
# Поиск уникальных элементов в списке
my_list = [10, 10, 3, 4, 5, 9, 30, 30]
print(list(set(my_list)))
# Обмен значениями через кортежи
var_1, var_2 = 20, 30
print(var_1, var_2)
var_1, var_2 = var_2, var_1
print(var_1, var_2)
# Вывод значения несуществующего ключа в словаре, воспользоваться методом get().
my_dict = {'k_1': 20, 'k_2': True, 'k_3': 'text'}
print(my_dict.get('k_4'))
# Поиск самых часто встречающихся элементов списка
my_list = [10, 20, 20, 20, 30, 50, 70, 30]
print(max(set(my_list), key=my_list.count))
# Распаковка последовательностей при неизвестном количестве элементов
my_list = [20, 30, 40, 50]
*el_1, el_2, el_3 = my_list
print(el_1, el_2, el_3)
el_1, *el_2, el_3 = my_list
print(el_1, el_2, el_3)
el_1, el_2, *el_3 = my_list
print(el_1, el_2, el_3)
el_1, el_2, el_3, *el_4 = my_list
print(el_1, el_2, el_3, el_4)
el_1, el_2, el_3, el_4, *el_5 = my_list
print(el_1, el_2, el_3, el_4, el_5)

# Вывод с помощью функции print() без перевода строки
for el in ["ab", "ra", "kada", "bra"]:
    print(el, end="")

print()

# Сортировка словаря по значениям
# ключей
my_dict = {'python': 1991, 'java': 1995, 'c++': 1983}
print(sorted(my_dict))
# значений элементов
my_dict = {'python': 1991, 'java': 1995, 'c++': 1983}
print(sorted(my_dict, key=my_dict.get))

# Нумерованные списки
for ind, el in enumerate(['one', 'two', 'three']):
    print(ind, el)
for ind, el in enumerate(['one', 'two', 'three'], 1):
    print(ind, el)

# Транспонирование матрицы
old_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
new_list = zip(*old_list)
print(list(new_list))

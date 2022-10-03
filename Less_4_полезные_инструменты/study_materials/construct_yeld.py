# Пример:
generator = (param * param for param in range(5))

for el in generator:
    print(el)
# Важно, что пройтись по генератору можно только один раз, данные в памяти не хранятся. При
# повторной попытке возникнет ошибка StopIteration
# print(next(generator))


# Оператор yield по назначению похож с оператором return, но возвращает генератор вместо значения
def generator():
    for el in (10, 20, 30):
        yield el


g = generator()
print(f"{g} - возвращает генератор вместо значения")
for el in g:
    print(el)

"""
При вызове функции с оператором yield функция не выполняется. 
Она возвращает объект-генератор, с которым далее можно выполнять нужные действия.
"""


# Обычный yield
def numbers_range(n):
    for i in range(n):
        yield i


# yield from
def numbers_range(n):
    yield from range(n)


"""
Конструкция позволяет «вкладывать» один генератор в другой, то есть создавать субгенераторы.
"""


def subgenerator():
    yield 'World'
def generator():
    yield 'Hello'
    yield from subgenerator() #Запрашиваем значение из субгенератора
    yield '!'
for i in generator():
    print(i, end = ' ')

"""
Вывод
Hello World !
"""
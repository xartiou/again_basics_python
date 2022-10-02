# example 1
my_list = [2, 4, 6]
new_list = [el + 10 for el in my_list]

print(f"Исходный список: {my_list}")
print(f"Новый сгенерированный список: {new_list}")
# Важно! Генератор создаёт новый список, а не изменяет текущий.

# example 2

my_list_1 = [2, 4, 6]
print(f"Исходный список: {my_list_1}")

new_list_1 = []
for el in my_list_1:
    new_list_1.append(el + 10)
print(f"Новый сгенерированный список: {new_list_1}")

# В цикле for возможен перебор не только элементов списка, но и строк файла.
lines = [line.strip() for line in open('text.txt')]
print(lines)

# В генератор допускается добавление условия.
my_list = [10, 21, 30, 45, 50]
print(my_list)
new_list = [el for el in my_list if el % 2 == 0]
print(new_list)

# Допустимо использовать вложенные циклы.
str_1 = "abc"
str_2 = "dy"
str_3 = "efg"
sets = [i + j + k for i in str_1 for j in str_2 for k in str_3]
print(sets)
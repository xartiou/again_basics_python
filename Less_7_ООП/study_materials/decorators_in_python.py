# функция в python

def my_sum(a, b):
    return a + b


print(my_sum(3, 5))

# в python функции - это тоже объекты
my_function_object = my_sum
print(my_function_object)  # <function my_sum at 0x7f059e9bfd90>
print(my_function_object(4, 7))
del my_sum
print(my_function_object(5, 8))


# в python функции можно объявлять внутри другой функции


def say_me_hello():
    # внутри определим новую функцию
    def hello():
        return "Hello World!"

    return hello()


# print(say_me_hello())


# в python функции может вернуть другую функцию
def my_calculation(operator):
    def my_sum(first=7, second=5):
        return first + second

    def my_diff(first=7, second=5):
        return first - second

    if operator == "+":
        return my_sum
    elif operator == "-":
        return my_diff


calc_sum = my_calculation("+")
print(calc_sum())
print(my_calculation("-")())


# если можно возвращать, то и можно передавать функцию как объект

def say_me():
    def h_w():
        return "Hello World!"

    return h_w()


def do_something_with_hello(function):
    print("Здесь выполняется другой код")
    print(function())


do_something_with_hello(say_me)


# создадим вручную простой декоратор
print('создадим вручную простой декоратор')


def my_simple_decorator(function_to_decorate):
    def wrapper_around_our_function():
        print('Я код, который выполнится до function_to_decorate')
        function_to_decorate()
        print('Я код, который выполнится после function_to_decorate')

    return wrapper_around_our_function


@my_simple_decorator
def stable_function():
    print("Hello World!")


# stable_function_decorated = my_simple_decorator(stable_function) = @my_simple_decorator
print(stable_function())


print("пробрасываем аргументы в декоратор")


def decorator_with_arguments(function):
    def wrapper_with_arguments(*args, **kwargs):
        print("мы получили: ", args)
        function(*args, **kwargs)

    return wrapper_with_arguments


@decorator_with_arguments
def print_full_name(first_name, last_name):
    print("Меня зовут:", first_name, last_name)


print_full_name('Василий', 'Тёркин')

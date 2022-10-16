"""
__init__
Выполним перегрузку конструктора. Напомним, что конструктор класса отвечает за создание объекта
класса.
"""


class MyClass:
    def __init__(self, param):
        self.param = param


mi = MyClass('text')
print(mi.param)

"""
__del__
В Python разработчик может участвовать как в создании, так и в удалении объекта.
"""


class MyClass:
    def __init__(self, param):
        self.param = param

    def __del__(self):
        print(f"Удаляем объект {self.param} класса MyClass")


md = MyClass('text_2')
del md


"""__str__"""


class MyClass:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def __str__(self):
        return f"Объект с параметрами ({self.param_1}, {self.param_2})"


ms = MyClass('s_1', 's_2')
print(ms)


"""__add__"""


class MyClass:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        return MyClass(self.width + other.width, self.height + other.height)

    def __str__(self):
        return f"Объект с параметрами ({self.width}, {self.height})"


mad_1 = MyClass(72, 26)
mad_2 = MyClass(25, 63)
print(mad_1 + mad_2)


"""__setattr__"""


class MyClass:
    def __setattr__(self, key, value):
        if key == "width":
            self.__dict__[key] = value
        else:
            print(f"Атрибут {key} недопустим")


msa = MyClass()
msa.height = 40
msa.width = 40
print(msa.width)


"""
__getitem__
Рассмотрим два примера
"""
# Пример 1:


class Class1:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return str(self.param)


class Class2:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.append(Class1(el))


my_obj = Class2(10, True, "text")
print(my_obj.my_list[1])


# Пример 2:


class Class12:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return str(self.param)


class Class22:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.append(Class12(el))

    def __getitem__(self, item):
        return self.my_list[item]


my_obj = Class22(10, True, "text")
print(my_obj.my_list[0])
print(my_obj[1])
print(my_obj[2])


"""__call__"""


class MyClass:
    def __init__(self, param):
        self.param = param

    def __call__(self, new_param):
        self.param = new_param

    def __str__(self):
        return f"Значение параметра - {self.param};"


obj_1 = MyClass("width")
obj_2 = MyClass("height")
obj_1("length")
obj_2("square")
print(obj_1, obj_2)


"""__eq__"""


class MyEq:
    def __init__(self):
        self.param = 40

    def __eq__(self, other):
        return self.param == other


me = MyEq()
print("Eq" if me == 40 else "No Eq")
print("Eq" if me == 41 else "No Eq")

"""__lt__"""


class Salary:
    val = 50000

    def __lt__(self, other):
        print("Оклад меньше премии?")
        return self.val < other.val


class Bonus:
    val = 10000

    def __lt__(self, other):
        print("Премия меньше оклада?")
        return self.val < other.val


s = Salary()
b = Bonus()
check = (s < b)
print(check)


"""__iadd__"""


class MyIa:
    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):
        self.val += other
        return self


mia = MyIa(100)
print(mia.val)
mia += 200
print(mia.val)






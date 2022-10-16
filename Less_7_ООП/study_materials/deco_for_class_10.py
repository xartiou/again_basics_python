
def my_decorator(person):
    def new_display(self):
        print("Name: ", self.name)
        print("Function decorator for class")

    person.display = new_display

    return person


@my_decorator
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name: ", self.name)


a = Person("Nikola")
a.display()

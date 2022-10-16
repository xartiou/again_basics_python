class MyDecorator:
    # accept the class as argument
    def __init__(self, name):
        self.person = name

    # accept the class's __init__ method arguments
    def __call__(self, name):
        # define a new display method
        def new_display(self):
            print("Name: ", self.name)
            print("Class decorator for class")

        # replace display with new_display
        self.person.display = new_display

        # return the instance of the class
        obj = self.person(name)
        return obj


@MyDecorator
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name: ", self.name)


a = Person("Ivanov")
a.display()

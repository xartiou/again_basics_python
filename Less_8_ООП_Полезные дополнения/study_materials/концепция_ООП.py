"""
1. Сформулировать задачу.
2. Определить объекты предметной области, участвующие в решении задачи.
3. Выделить классы, на основе которых генерируются объекты. При необходимости определить
базовые классы и классы-потомки.
4. Установить основные атрибуты и методы объектов.
5. Создать классы, их атрибуты и методы.
6. Создать объекты классов.
7. Выполнить итоговое решение задачи, организовав взаимодействие объектов.
"""


class Person:
    """ общий класс для Преподавателя(Teacher)и Студента(Student)"""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя и Фамилия: {self.name} {self.surname}"


class Teacher(Person):

    def to_teach(self, subj, *students):
        for student in students:
            student.to_take(subj)


class Student(Person):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.list_study = []

    def to_take(self, subj):
        self.list_study.append(subj)


class SubjectStudy:

    def __init__(self, *subjects):
        self.subjects = list(subjects)

    def my_list(self):
        return self.subjects


s = SubjectStudy("maths", "physics", "chemistry")
t = Teacher("Ivan", "Ivanov")
print(t)
print(s.subjects)

stud_1 = Student('Alfred', 'Nobel')
stud_2 = Student('Nikola', 'Tesla')
stud_3 = Student('Dmitry', 'Mendeleev')
print(f"{stud_1},\n{stud_2},\n{stud_3}")
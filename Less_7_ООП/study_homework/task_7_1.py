"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка:
сложение элементов матриц выполнять поэлементно
 — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, ll):
        """Данные (список списков) для формирования матрицы"""
        self.ll = ll

    def __str__(self):
        """Вывод матрицы в привычном виде"""
        return '\n'.join(map(str, self.ll))

    def __add__(self, other):
        """
        Сложения двух объектов класса Matrix (двух матриц).
        Результатом сложения должна быть новая матрица.
        """
        sum_l = []
        for i in range(len(self.ll)):
            sum_l.append([])
            for j in range(len(self.ll[0])):
                sum_l[i].append(self.ll[i][j] + other.ll[i][j])
        return '\n'.join(map(str, sum_l))


# вариант с безымянной функцией


# class MatrixL:
#
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __str__(self):
#         return '\n'.join(map(lambda r: '   '.join(map(str, r)), self.matrix)) + '\n'
#
#     def __add__(self, other):
#         return MatrixL(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))


a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]

matrix_1 = MatrixL(a)
matrix_2 = MatrixL(b)
print(f"Matrix 1\n{matrix_1}\n{'-' * 20}")
print(f"Matrix 2\n{matrix_2}\n{'-' * 20}")
print(f"matrix 1 + matrix 2\n{matrix_1 + matrix_2}")
# sum_m = matrix_1 + matrix_2
# print(sum_m)

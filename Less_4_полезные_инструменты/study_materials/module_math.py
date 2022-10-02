"""
ceil(N)      Округлить число N до ближайшего большего числа
fabs(N)      Определить модуль числа N
factorial(N) Найти факториал числа N
floor(N)     Округлить число вниз
fmod(a, b)   Получить остаток от деления a на b

isfinite(N)  Является ли N числом
modf(N)      Определить дробную и целую часть числа N
sqrt(N)      Определить квадратный корень числа N
sin(N)       Определить синус для N-радианов
cos(N)       Определить косинус для N-радианов
tan(N)       Определить тангенс для N-радианов
degrees(N)   Перевести радианы в градусы
radians(N)   Перевести градусы в радианы
"""

from math import ceil, fabs, factorial, floor, \
fmod, isfinite, modf, sqrt, sin, cos, tan, degrees, radians

print(f"ceil() -> {ceil(6.75)}")
print(f"fabs() -> {fabs(-4)}")
print(f"factorial() -> {factorial(5)}")
print(f"floor() -> {floor(4.34)}")
print(f"fmod() -> {fmod(9, 4)}")
print(f"isfinite() -> {isfinite(10)}")
print(f"modf() -> {modf(10.5)}")
print(f"sqrt() -> {sqrt(16)}")
print(f"sin() -> {sin(1.5708)}")
print(f"cos() -> {cos(1.5708)}")
print(f"tan() -> {tan(1.5708)}")
print(f"degrees() -> {degrees(1.5708)}")
print(f"radians() -> {radians(90)}")
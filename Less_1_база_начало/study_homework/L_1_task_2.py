"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

time_in_seconds = int(input("Введите время в секундах: "))
time_in_hours = time_in_seconds // 3600
time_in_minutes = (time_in_seconds - time_in_hours * 3600) // 60
rest_of_seconds = (time_in_seconds % 3600) - (time_in_minutes * 60)

print(f"Вы ввели секунд {time_in_seconds}- это {time_in_hours} часа, {time_in_minutes} минут, {rest_of_seconds} секунд")

"""
JSON (Java Script Object Notation) — стандарт обмена информацией.
Он может, например,применяться при получении данных через API и необходимости их хранения в документной базе данных.
Работать с данными в JSON-формате можно средствами языка Python.
JSON — универсальная нотация, и она напоминает Python-словарь.
"""
import json

"""
Сериализация – это процесс преобразования объектов App-уровня в примитивные типы, такие как словарь, текст, строка, …

Python          JSON

dict            object
list,tuple      array
str             string
int,long,float  number
True            true
False           false
None            null
"""

data = {
    "income": {
        "salary": 50000,
        "bonus": 20000
    }
}
# Через контекстный мессенджер Python создадим файл my_file.json и откроем его в режиме записи:
with open("my_file.json", "w", encoding="utf8") as write_f:
    json.dump(data, write_f)

json_str = json.dumps(data)
print(json_str)
print(type(json_str))

"""
Десериализация – это обратный процесс сериализации, в котором данные, как правило, словари или объекты JSON, 
преобразуются обратно в объекты уровня APP.
JSON        Python
object      dict
array       list
string      str
number(int) int
number(real) float
true        True
false       False
null        None
"""

with open("my_file.json") as read_f:
    data = json.load(read_f)

print(data)
print(type(data))

json_str = """{"income": {"salary": 50000, "bonus": 20000}}"""
data = json.loads(json_str)
print(data)
print(type(data))
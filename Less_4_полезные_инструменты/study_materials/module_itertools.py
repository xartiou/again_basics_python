# count()
from itertools import count

for el in count(7, 2):
    if el > 15:
        break
    else:
        print(el)

# cycle()

from itertools import cycle

c = 0
for el in cycle("ABC"):
    if c > 10:
        break
    print(el)
    c += 1

program_lang = ["python", "java", "perl", "javascript"]
iter = cycle(program_lang)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

# repeat (<Объект>, <Количество повторений>)

# combinations (<Объект>,<Количество значений>)
# combinations('ABCD', 2) --> AB AC AD BC BD CD
# combinations(range(4), 3) --> 012 013 023 123
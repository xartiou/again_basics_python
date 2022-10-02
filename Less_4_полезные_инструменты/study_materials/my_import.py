import my_function

my_function.show_message()
print(my_function.simple_calc())


from my_function import show_message
from my_function import simple_calc

show_message()

print(simple_calc())

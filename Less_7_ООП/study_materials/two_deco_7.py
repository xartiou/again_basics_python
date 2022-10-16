

def make_ext(func):
    """First decorator"""
    return lambda: "(<ext_tag> " + func() + " </ext_tag>)"


def make_int(func):
    """Second decorator"""
    return lambda: "(<int_tag> " + func() + " </int_tag>)"


@make_ext
@make_int
def my_func():
    """any logic"""
    return "Any text"


print(my_func())

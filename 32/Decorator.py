"""
Do czego w Pythonie służą dekoratory? Napisz
dekorator, który będzie dodawał trzy gwiazdki przed i po
efekcie działania udekorowanej funkcji.
"""


def dec_function(fun):
    def wrap_the_function():
        print("work before")
        fun()
        print("work after")
    return wrap_the_function


@dec_function
def some_function():
    print("EBEBEBE!")


some_function()
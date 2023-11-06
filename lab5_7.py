# Zadanie 7

# Stwórz dekorator cached służący do cachowania wywołań dowolnej funkcji, 
# tzn. chcemy by:
# - wywołanie funkcji z określonymi argumentami miało miejsce tylko raz
# - funkcja mogła przyjmować dowolną liczbę nazwanych i nienazwanych argumentów
# - nie musi reagować poprawnie na domyślne argumenty, tzn. wywołanie funkcji z 
#   domyślnymi argumentami a podanie dokładnie takich samych może być traktowane 
#   jako dwa różne wywołania
# - na opakowanej funkcji można wywołać .cache_reset(), który usunie cache z pamięci
# - wywołanie .cache_status() zwraca string z opisem w postaci:
#   Function FUNCTION_NAME called X times, evaluated Y times

from functools import wraps
from random import random


def cached(func):
    pass


@cached
def foo(x, y=1, z=4):
    return random()
        
print(foo(3) == foo(3))
print(foo(4) == foo(4))
print(foo(3, z=-1, y=3) == foo(3, y=3, z=-1))
print(foo(3) != foo(x=3))
a = foo(3)
print(foo.cache_status() == 'Function foo called 9 times, evaluated 4 times')
foo.cache_reset()
print(a != foo(3))
print(foo.cache_status() == 'Function foo called 1 times, evaluated 1 times')
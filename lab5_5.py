# Zadanie 5
# Napisz dekorator 'accepts', który sprawdza czy argumenty przekazane do funkcji
# (zarówno pozycyjne jak i nazwane) są odpowiedniego typu.
# Typy argumentów są przekazywane jako argumenty dekoratora w kolejności
# odpowiadającej parametrom dekorowanej funkcji.
#
# Przykład:
# @accepts(float, int)
# def func(x, y):  # x musi być float, y musi być int
#     return x + y
#
# Wywołania poprawne:
# - func(1.0, 2)
# - func(x=1.0, y=2)
# - func(1.0, y=2)
def accepts(*types):
    """Sprawdza czy udekorowanej funckji zostały podane odpowiednie parametry zdefiniowane 
       w argumentach dekoratora"""
    pass


@accepts(str)
def capitalize(word):
    return word[0].upper() + word[1:]

print(capitalize('ola') == 'Ola')

try:
    capitalize(2)
except TypeError:
    print(True)

@accepts(float, int)
def static_pow(base, exp):
    return base ** exp 

print(static_pow(2., 2) == 4.)
print(static_pow(2., exp=2) == 4.)
print(static_pow(base=2., exp=2) == 4.)

try:
    static_pow('x', 10)
except TypeError:
    print(True)
    
try:
    static_pow(2, 2.2)
except TypeError:
    print(True)
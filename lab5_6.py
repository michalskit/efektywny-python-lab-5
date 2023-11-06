# Zadanie 6
def returns(*types):
    """Sprawdza czy udekorowana funkcja zwraca poprawne argumenty, zdefiniowane w parametrach dekoratora"""
    pass

@returns(str)
def str_only_identity(word):
    return word

print(str_only_identity('hello') == 'hello')

try:
    str_only_identity(10)
except TypeError:
    print(True)
    
@returns(int, int)
def split_indices(x):
    return x[0], x[1]

print(split_indices(x=[6,9]) == (6,9))

try:
    split_indices('AB')
except TypeError:
    print(True)

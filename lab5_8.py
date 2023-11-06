# Zadanie 8
def zlozenie(n):
    """
    Dekorator, który przyjmuje liczbę całkowitą n i zwraca nowy dekorator, który
    wykonuje dekorowaną funkcję n razy.
    """
    pass

@zlozenie(3)
def f1(x):
    return x + 1

@zlozenie(2)
def f2(x):
    return x * x

@zlozenie(5)
def f3(word):
    return "".join(chr(ord(l) + 1) for l in word)

# Test the functions
results = {
    'f1(2) == 5': f1(2) == 5,
    'f2(3) == 81': f2(3) == 81,
    'f3("alamakota") == "fqfrfptyf"': f3("alamakota") == "fqfrfptyf"
}

print(results)

# Zadanie 3

from time import time

def timeit(func):
    """
    Dekorator funkcji `timeit` mierzy i wypisuje czas wykonania dekorowanej funkcji. 
    Wewnątrz znajduje się zagnieżdżona funkcja `wrapper`, która wykonuje 
    pomiar czasu, wywołuje dekorowaną funkcję oraz wypisuje wynik pomiaru.
    """
    def wrapper(*args, **kwargs):
        """
        Funkcja opakowująca `wrapper` rozpoczyna pomiar czasu, wywołuje 
        dekorowaną funkcję z jej argumentami, kończy pomiar czasu,
        a następnie wypisuje czas wykonania funkcji i zwraca jej wynik.
        """
        pass
        # print(f"Czas wykonania funkcji {func.__name__}: {end_time - start_time} sekund")
        # return result
    return wrapper

@timeit
def squares_list(n):
    """
    Funkcja `squares_list` tworzy listę kwadratów liczb od 0 do n-1 
    za pomocą pętli for.
    """
    squares = []
    for i in range(n):
        squares.append(i ** 2)
    return squares

@timeit
def squares_comprehension(n):
    """
    Funkcja `squares_comprehension` tworzy listę kwadratów liczb od 0 do n-1 
    za pomocą składni list comprehension.
    """
    return [i ** 2 for i in range(n)]

@timeit
def squares_map(n):
    """
    Funkcja `squares_map` tworzy listę kwadratów liczb od 0 do n-1 
    za pomocą funkcji `map` i wyrażenia lambda.
    """
    return map(lambda x: x**2, range(n))

n = 1000000
l = squares_list(n)  # Pomiar czasu dla funkcji generującej listę przez pętlę
c = squares_comprehension(n)  # Pomiar czasu dla list comprehension
m = list(squares_map(n))  # Pomiar czasu dla map (konwersja na listę)


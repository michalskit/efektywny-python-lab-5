# Zadanie 1
def podziel_liczby(licznik, mianownik):
    """
    Funkcja próbuje podzielić dwie liczby przekazane jako argumenty.

    Args:
    licznik (int/float): Liczba, która będzie dzielona.
    mianownik (int/float): Liczba, przez którą licznik zostanie podzielony.

    Returns:
    float: Wynik dzielenia licznika przez mianownik jeśli dzielenie jest możliwe.
    None: Jeśli dzielenie nie jest możliwe (dzielenie przez zero lub inny wyjątek).

    Obsługuje dwa typy wyjątków:
    - ZeroDivisionError: Zwraca None i drukuje "Dzielenie przez zero jest niemożliwe",
      gdy mianownik jest równy zero.
    - Exception: Zwraca None i drukuje "Wystąpił nieznany błąd" wraz z informacją o wyjątku,
      dla wszystkich innych wyjątków.

    Przykłady:
    print(podziel_liczby(10, 2))  # Powinno zwrócić 5.0
    print(podziel_liczby(5, 0))   # Powinno wydrukować "Dzielenie przez zero jest niemożliwe" i zwrócić None
    print(podziel_liczby('5', '2'))  # Powinno wydrukować "Wystąpił nieznany błąd" i zwrócić None
    """
    try:
        pass
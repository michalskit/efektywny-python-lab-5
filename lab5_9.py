# Zadanie 9
# Python nie ma wbudowanej instrukcji switch. Ale posiada anonimowe 
# funkcje oraz słowniki. Zaimplementuj poniższy switch w postaci 
# słownika funkcji. 
# int my_function(x, y) {
#
#   switch(x) {
#       case 1: return y*y;
#       case 2: return x+y;
#       case 3: return x*y;
#       case 4: return 0;
#   }
# }

# PS. Nigdy nie róbcie tego w faktycznym kodzie :)

def my_function(x, y):
    """
    Funkcja symulująca instrukcję switch, zwracająca różne wyniki w zależności od wartości x.

    Parametry:
    x (int): Wartość, która decyduje o wyborze operacji.
    y (int): Wartość używana w operacji.

    Zwraca:
    int: Wynik operacji zdefiniowanej przez wartość x:
         - Dla x=1: zwraca kwadrat wartości y.
         - Dla x=2: zwraca sumę wartości x i y.
         - Dla x=3: zwraca iloczyn wartości x i y.
         - Dla x=4: zwraca 0.
         - Dla innych wartości x: zwraca None.
    """
    pass


print(my_function(1,3)==9)
print(my_function(2,4)==6)
print(my_function(3,1)==3)
print(my_function(4,9)==0)
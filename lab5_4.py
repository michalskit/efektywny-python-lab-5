# Zadanie 4
import sys
sys.float_info.epsilon # epsilon maszynowy


def derivate(epsilon=None):
    """
    Zwraca pochodną funkcji w punkcie, wg. wzoru f'(x) = [f(x+h) - f(x)]/h, 
    gdzie h jest parametrem dekoratora, jeśli nie zostanie podany, należy przyjąć 1000 * epsilon maszynowy
    """
    pass


@derivate(0.01)
def f(x):
    return x*x

@derivate(0.00001)
def g(x):
    return x*x*x+3

def test(a, b, eps=1):
    return abs(round(a)-round(b)) < eps

print(test(f(100), 200.0))
print(round(f(0)) == 0.0)

print(test(g(100), 30000.0))
print(round(g(0)) == 0.0)

from random import random
for x in [random()*1000. for _ in range(20)]:
    print(f(x), 2*x, '\t', test(f(x), 2*x))
    print(g(x), 3*x**2, '\t', test(g(x), 3*x**2))
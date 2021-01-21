'''
1. Las funciones son 1st class citizens
    Se pueden pasar por referencia
2. Las operaciones con listas son terriblemente relevantes, poderosas y eficientes
    * map
    * reduce
'''

# enfoque 1
def factorial(n):
    m = 1
    for i in range(1, n+1):
        m *= i

    return m

# print(factorial(5))


# enfoque 2
from functools import reduce
factorial2 = lambda n: reduce(lambda acc, val: acc * val, range(2, n+1), 1)

print(factorial2(5))
    
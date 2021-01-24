# problema 1 ---------------------------------------------------------
triangle = lambda n : '\n'.join([
    f"{'  ' * (0 if i==n else (n-i))} {'* ' * (2*i-1)}"
    for i in range(n, 0, -1)
])

heights = map(triangle, [4, 5, 6]) # alturas 4, 5 y 6

# for i in heights: print(i) # descomentar para ejecutar instrucción

# problema 2 ---------------------------------------------------------
cache = {}
def eq(n: int, m: int):
    if f'{n,m}' in cache:
        return cache[f'{n,m}']

    # reglas
    result = 1;
    if m==n:
        return 1

    if m==0:
        return 1

    result = cache[f'{n,m}'] = eq(n-1, m) + eq(n-1, m-1)
    return result

# # descomentar para ejecutar instrucciones
# print(eq(50, 35))
# print(eq(100, 85))

# problema 3 ---------------------------------------------------------
import math 

diamond = lambda n : '\n'.join([
    f"{' ' * ((n-i)-1)} {'* ' * (i+1)}" if i<math.ceil(n/2) else f"{' ' * (i)} {'* ' * (n-i)}"
    for i in range(n)
])

diamonds = map(diamond, [7, 9, 11]) # alturas 7, 9 y 11

# for i in diamonds: print(i) # descomentar para ejecutar instrucción

# problema 4 ---------------------------------------------------------
import time

def primes(n):
    begin = time.time()
    prime = [True] * n
    for i in range(3, n, 2):
        if prime[i]:
            prime[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return ([2] + [i for i in range(3, n, 2) if prime[i]], "Tiempo de ejecución " + str(time.time() - begin))

# print(primes(100000)) # descomentar para ejecutar instrucción
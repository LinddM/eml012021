'''
Triangle
    * Map * range to range of strings

    Analysis:

    // i for index inside loop
    // n for number of levels

    Formula for spaces
        (n-1)-i
    
    Formula for stars
        2*i+1

Fibonacci
    Pure functions
        1. Depends only in params
        2. No random
        3. No colateral efects
    Pure functions are memorable *if a value was calculated, we don´t have to calculate again

'''

triangle = lambda n : '\n'.join([
    f"{' ' * ((n-1)-i)} {'*' * (2*i+1)}"
    for i in range(n) # comprehension
])


# print(triangle(4))

def fibonacci(n):
    # xn = xn−1 + xn−2
    if n > 0:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        if n == 0:
            return 0
        else:
            return 1

# print(fibonacci(8))

cache ={}
def cache_fibo(n):
    if n in cache:
        return cache[n]

    result = 1
    if n < 2:
        return 1
    result = cache[n] =  cache_fibo(n-1) + cache_fibo(n-2)
    return result

# print(cache_fibo(5))
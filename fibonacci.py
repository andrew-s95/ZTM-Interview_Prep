from functools import lru_cache
@lru_cache(maxsize = 1000)
def fibonnaci(num):
    if num < 2:
        return num
    return fib(num-1) + fib(num-2)

cache = {}
def fibonacciCache(num):
    if n in cache:
        return cache[n]
    elif n < 2:
        cache[n] = n
        return cache[n]
    else:
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]

x = fibonacciCache(8)
print(cache)
    
fibonacci_cache = {}
def fibonacci(i):
    #if we have the cached value, then return it
    if i in fibonacci_cache:        return fibonacci_cache[i]

    # compute the Nth term
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
      value = fibonacci(i-1) + fibonacci(i-2)
        
    #cache the value and return it
    fibonacci_cache[i] = value
    return value

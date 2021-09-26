from functools import cache
import time

@cache
def fibonacci_cache(n):
    if n == 1 or n==2:
        return 1
    else:
        return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)

def fibonacci(n):
    if n == 1 or n==2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

start = time.time()
fibonacci_cache(35)
end= time.time()
print ("Time Elapsed (Cached Process): {}".format((end-start)))

start = time.time()
fibonacci(35)
end= time.time()
print ("Time Elapsed (Without Cache): {}".format((end-start)))
import time 

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


nthTerm = 36

start_time = time.time()
print(fibonacci(nthTerm))
end_time = time.time()
print(f"Execution Time: {end_time-start_time}")



# Recursive Fibonacci Function
def dyna_fib(n, lookup):
    if n <= 2:
        lookup[n] = 1
    
    if lookup[n] is None:
        lookup[n] = dyna_fib(n-1, lookup) + dyna_fib(n-2, lookup)
    
    return lookup[n]

fibonacci_values = [None] * (10000)
nthTermTwo = 36
start_time = time.time()
print(dyna_fib(nthTermTwo, fibonacci_values))
end_time = time.time()
print(f"Execution Time: {end_time-start_time}")
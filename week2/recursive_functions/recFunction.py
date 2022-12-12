def factorialLoop(x):
    retVal = x
    for i in reversed(range(1,x)):
        retVal *= i
    return retVal


def factorial(x):
    if x == 1:
        return 1
    else:
       return x * factorial(x-1)


n = 5
print(factorialLoop(n))
print(factorial(n))

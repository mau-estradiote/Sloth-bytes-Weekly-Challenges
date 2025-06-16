import math

def fact_of_fact(x: int):
    l = []
    for n in range(x):
        l.append(math.factorial(n+1))
    print(l)
    return math.prod(l)
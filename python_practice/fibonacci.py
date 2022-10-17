#!/usr/bin/python3


"""
fibonacci series
the sum of two elements defines the next
"""
def fib(n):
    a, b = 0, 1

    while a < n:
        print(a, end=", ")
        a, b = b, a + b
    print()

fib(20)
f = fib
f(20)
print(id(fib))
print(id(f))
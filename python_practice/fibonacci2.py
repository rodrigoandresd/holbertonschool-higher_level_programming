#!/usr/bin/python3


"""
fibonacci series
the sum of two elements defines the next
"""
def fib2(n):
    listfb = []
    a, b = 0, 1

    while a < n:
        listfb.append(a)
        a, b = b, a + b
    return listfb

f = fib2(20)
print(f)
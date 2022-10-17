#!/usr/bin/python3


"""
for in  + range (if  and else)
"""

for num in range(2, 10):
    for i in range(2, num):
        if num % i == 0:
            print(num, 'equals', i, '*', num//i)
            break
    else:
        print(num, 'is a prime number')

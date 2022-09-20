#!/usr/bin/python3
import random
from sys import last_traceback
number = random.randint(-10000, 10000)
last = number % 10
if number < 0:
    n = number * -1
    last = (n % 10) * -1
if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last < 6 and last != 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
elif number < 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last} and is 0")

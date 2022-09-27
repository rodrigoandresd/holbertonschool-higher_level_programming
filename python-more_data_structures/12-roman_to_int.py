#!/usr/bin/python3


def roman_to_int(roman_string):
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string and type(roman_string) == str:
        sum = 0
        for i in roman_string:
            if i == 'V' and roman_string[:-1] == 'I':
                sum -= 2
            sum += roman_d.get(i)
        return sum
    else:
        return 0

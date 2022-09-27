#!/usr/bin/python3


def roman_to_int(roman_string):
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string and type(roman_string) == str:
        sum = 0
        for i in roman_string:
            if i == 'V' and roman_string[:-1] == 'I':
                sum -= 2
            elif i == 'V' and roman_string[3:-1] == 'I':
                sum -= 2
            elif i == 'X' and roman_string[1:-2] == 'C':
                sum -= 11
            elif i == 'X' and roman_string[3:-2] == 'X':
                sum -= 1/2
            sum += roman_d.get(i)
        return int(sum)
    else:
        return 0

#!/usr/bin/python3


def roman_to_int(roman_string):
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string and type(roman_string) == str:
        sum = 0
        for i in roman_string:
            sum += roman_dic.get(i)
        return sum
    else:
        return 0

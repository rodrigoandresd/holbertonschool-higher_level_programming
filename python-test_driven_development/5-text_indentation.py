#!/usr/bin/python3

"""module that contain the funtion text_indentation"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of
    these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_str = ""
    for i in text:
        new_str += i
        if i == '.' or i == '?' or i == ':':
            print(new_str.strip() + "\n")
            new_str = ""
    print(new_str.strip(), end="")

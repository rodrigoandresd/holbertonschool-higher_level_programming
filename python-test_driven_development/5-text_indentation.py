#!/usr/bin/python3

"""module that contain the funtion text_indentation"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of 
    these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print(i + "\n")
        else:
            print(i, end="")

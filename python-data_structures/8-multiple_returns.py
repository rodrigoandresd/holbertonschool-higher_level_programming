#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if sentence == 0:
        first = None
    tuple = (length, first)
    return tuple

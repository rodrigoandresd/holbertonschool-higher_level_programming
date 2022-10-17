#!/usr/bin/python3


def concat(*args, sep="/"):
    return sep.join(args)

planets = concat("earth", "mars", "venus")
print(planets)

planets2 = concat("earth", "mars", "venus", sep=".")
print(planets2)
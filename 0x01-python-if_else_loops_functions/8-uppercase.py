#!/usr/bin/python3

def to_upper(character):
    if 97 <= ord(character) <= 122:
        return ord(character) - 32
    else:
        return ord(character)

def uppercase(input_str):
    new_str = ""
    for character in input_str:
        new_str += "%c" % to_upper(character)
    print("{:s}".format(new_str))

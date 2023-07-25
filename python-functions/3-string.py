#!/usr/bin/python3

""" A function that reverses a string """

def reverse_string(string):
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
    return reversed_string

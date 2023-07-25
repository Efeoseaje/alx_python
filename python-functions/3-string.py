#!/usr/bin/python3

""" A function that reverses a string """

def reverse_string(string):
    for i in string:
        string = i + string
        return string

#!/usr/bin/python3

""" A function that takes a number and returns a list of fibonacci sequence """

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
        
    fibonacci_list = [0, 1]
    while len(fibonacci_list) < n:
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)

    return fibonacci_list

    
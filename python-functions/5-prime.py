#!/usr/bin/python3

""" Returns True if it is a prme number else false"""

def is_prime(number):
    if number <= 1:
        return False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
    return True

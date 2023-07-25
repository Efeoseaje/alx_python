#!/usr/bin/python3

""" Password validation """

def validate_password(password):
    if len(password) < 8:
        return False

    char_digit = False
    char_lowercase = False
    char_uppercase = False
    
    for char in password:
        if char.isupper():
            char_uppercase = True
        elif char.islower():
            char_lowercase = True
        elif char.isdigit():
            char_digit = True

    if not (char_uppercase and char_lowercase and char_digit):
        return False
    
    if " " in password:
        return False
    
    return True
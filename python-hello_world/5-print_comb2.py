#!/usr/bin/python3

""" Print numbers from 00 to 99"""

for num in range(0, 99):
    print("{:02d}".format(num), end=", ")
print(99)

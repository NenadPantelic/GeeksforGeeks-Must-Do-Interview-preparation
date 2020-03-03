#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:07:20 2020

@author: nenad
"""


def atoi(string):
    num = 0
    # if formed number is negative
    neg = False
    for i in range(len(string)):
        char = string[i]
        if char == "-":
            if i  == 0:
                neg = True
                continue
            else:
                return -1
        # char is not digit - so whole string is not valid number
        if not char.isdigit():
            return -1
        num = num * 10 + int(char)
        
    return num if not neg else -num
        


# Test 1
string = "-2"
print(atoi(string))

# Test 2
string = "21a"
print(atoi(string))


# Test 3
string = "123"
print(atoi(string))


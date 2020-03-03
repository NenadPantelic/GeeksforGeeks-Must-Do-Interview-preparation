#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:17:43 2020

@author: nenad
"""
"""
Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.

"""

def reverse_str(string):
    return ".".join(string.split(".")[::-1])


## Test 1
# Testing
t = int(input())
for i in range(t):
    str = input()
    print(reverse_str(str))
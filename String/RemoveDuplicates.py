#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:37:56 2020

@author: nenad
"""

from collections import Counter

def remove_duplicates(string):
    counter = Counter()
    for char in string:
        counter[char] += 1
    
    print(counter)
    char_list = []
    for char in string:
        if counter[char] == 1:
            char_list.append(char)
    
    return "".join(char_list)


# Test 1
s = "geeksforgeeks"
print(remove_duplicates(s))
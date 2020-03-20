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
    
    char_list = []
    for char in string:
        if counter[char] >= 1:
            char_list.append(char)
            # 0 means char is used, do not use it again
            counter[char] = 0
    
    return "".join(char_list)
    
t = int(input())
for i in range(t):
    string = input()
    print(remove_duplicates(string))


# Test 1
s = "geeksforgeeks"
print(remove_duplicates(s))

# Test 2
s = "geeks for geeks"
print(remove_duplicates(s))
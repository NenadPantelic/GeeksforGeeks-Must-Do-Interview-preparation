#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:32:30 2020

@author: nenad
"""


def remove_adj_duplicates(string, res=""):
    print(string)
    if len(string) == 1:
        return res + string 
    if string[0] == string[1]:
        return remove_adj_duplicates(string[2:], res)
    else:
        return remove_adj_duplicates(string[1:], res = res + string[0])
    
    
# Test 1
s = "geeksforgeeks"
print(remove_adj_duplicates(s))

# Test 2
s = "acaaabbbacdddd"
print(remove_adj_duplicates(s))
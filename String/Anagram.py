#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:13:57 2020

@author: nenad
"""


def anagram(str1, str2):
    return "YES" if sorted(str1) == sorted(str2) else "NO"

# Test 1
str1, str2 = "geeksforgeeks forgeeksgeeks".split()
print(anagram(str1,str2))


# Test 2
str1, str2 = "allergy allergic".split()
print(anagram(str1,str2))


# Testing
t = int(input())
for i in range(t):
    str1, str2 = input().split()
    print(anagram(str1, str2))
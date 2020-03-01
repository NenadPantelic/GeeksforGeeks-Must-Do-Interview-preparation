#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 12:34:22 2020

@author: nenad
"""

from collections import Counter

def majority_element(arr):
    n = len(arr)
    maj = n//2
    counter = Counter()
    for el in arr:
        val = counter.get(el, 0)
        if val >= maj:
            return el
        counter[el] += 1
    return -1


# Test 1
    
arr = [3,1,3,3,2]
print(majority_element(arr))

# Test 2
    
arr = [1,2,3]
print(majority_element(arr))

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(majority_element(arr))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:33:36 2020

@author: nenad
"""

# minimize the dot product of two arrays if shuffling is allowed
def minimize_sum_of_product(a,b):
    dot_product = 0
    # to minimize the dot product, sort one array decreasing and one increasing, so you make balanced weight
    # of a[i] * b[i] product - it will minimize it
    a.sort(reverse = True)
    b.sort()
    
    for i in range(len(a)):
        dot_product += a[i] * b[i]
    return dot_product

# Test 1
a = [3,1,1]
b = [6,5,4]
print(minimize_sum_of_product(a,b))


# Test 2
a = [6,1,9,5,4]
b = [3,4,8,2,4]
print(minimize_sum_of_product(a,b))

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(minimize_sum_of_product(a, b))
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:13:14 2020

@author: nenad
"""

# form a largest number of n digits which is equal to s
def largest_number_possible(n, s, number):
    # impossible to handle - sum of values must be greater than zero; other case is 
    # when we demanded sum is geeater than n * 9 (max number that we can make with n digits) 
    if s < 1 or n * 9 < s:
        return -1
    # if s is in range [0,9]
    if n == 0:
        return number
    # shift number for n places in left and s for n-1 places
    if s < 10:
        return number * 10 ** n + s * 10 ** (n-1)
    #number = number * 10 + 9 
    return largest_number_possible(n-1, s-9, number * 10 + 9)


# Test 1
n = 4
s = 12
number = 0
print(largest_number_possible(n, s, number))
                
            
# Test 1
n = 2
s = 18
number = 0
print(largest_number_possible(n, s, number))
                
# Test 1
n = 5
s = 1
number = 0
print(largest_number_possible(n, s, number))

t = int(input())
for i in range(t):
    n, s = list(map(int, input().split()))
    print(largest_number_possible(n, s, 0))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:31:54 2020

@author: nenad
"""


def kadane(arr):
    max_ending_here = 0
    max_total = 0
    for i in range(len(arr)):
        # cumsum in this point, if sum is neg, reset to zero
        max_ending_here += arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
        # update max
        if max_total < max_ending_here:
            max_total = max_ending_here
    # in case that all of the elements are negative
    if max_total == 0:
        max_total = max(arr)
    return max_total


# Test 1
arr = [-2,-3,4,-1,-2,1,5,-3]
print(kadane(arr))


# Test 2
arr = [1,2,3,-2,5]
print(kadane(arr))

arr = [-1,-2,-3,-4]
print(kadane(arr))
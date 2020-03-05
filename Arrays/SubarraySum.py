#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:59:40 2020

@author: nenad
"""


def subarray_sum(arr, total):
    n = len(arr)
    i = 0
    # sum of subarray
    sumval = 0
    # start index of wanted subarray
    start = 0
    while i < n:
        sumval += arr[i]
        # remove elements from window - subarray until we reach condition sumval <= total, move start point of 
        # the subarray
        while sumval > total:
            sumval -= arr[start]
            start += 1
        # condition met
        if sumval == total:
            return (start+1, i+1)
        i += 1
    # there is no subarray which sum is equal to total
    return -1


# Test 1
arr = [1,2,3,7,5]
s = 12
print(subarray_sum(arr, s))


# Test 1
arr = list(range(1,11))
s = 15
print(subarray_sum(arr, s))
        
t = int(input())
for i in range(t):
    n,s = map(int, input().split())
    arr = list(map(int, input().split()))
    res = subarray_sum(arr,s)
    print (res if isinstance(res, int) else "{} {}".format(res[0], res[1]))
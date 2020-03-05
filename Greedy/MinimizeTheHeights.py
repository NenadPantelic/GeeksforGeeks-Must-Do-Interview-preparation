#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:21:57 2020

@author: nenad
"""

def minimize_the_heights(arr, k):
    n = len(arr)
    maxx = max(arr)
    minn = min(arr)
    if maxx - minn < k:
        return maxx - minn
    avg = (maxx + minn) // 2
    maxx = 0
    minn = 500
    for i in range(n):
        # if value is greater than avg - decrease it by k
        if arr[i] > avg:
            arr[i] -= k
        # else increase it by k
        else:
            arr[i] += k
        if arr[i] < minn:
            minn = arr[i]
        if arr[i] > maxx:
            maxx = arr[i]
    return maxx - minn

# Test 1
arr = [1,15,10]
print(minimize_the_heights(arr, 6))

# Test 2
arr = [1,5,8,10]
print(minimize_the_heights(arr, 2))


t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    arr = list(map(int, input().split()))
    print(minimize_the_heights(arr, k))
    
            
        
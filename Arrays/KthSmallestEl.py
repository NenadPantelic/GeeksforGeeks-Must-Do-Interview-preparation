#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:14:24 2020

@author: nenad
"""



def kth_smallest_element(arr, k):
    maxx = max(arr)
    # counting array
    els = [0] * (maxx + 1)
    # counting sort idea
    for val in arr:
        els[val] += 1
    #print(els)
    pos = 0
    for i in range(maxx+1):
        if els[i] >= 1:
            if pos + els[i] >= k or i == maxx:
                return i
            pos += els[i]
            

t = int(input())         
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    print(kth_smallest_element(arr,k))
    
# Test 1   
arr = [7,10,4,3,20,15]
k  = 3
print(kth_smallest_element(arr, k))


# Test 2  
arr = [7,10,4,20,15]
k  = 4
print(kth_smallest_element(arr, k))


# Test 3   
arr = [7,10,4, 20, 15]
k  = 4
print(kth_smallest_element(arr, k))


# Test 4
arr = list(map(int,"4 25 24 12 22 5 25 12 41".split()))
print(kth_smallest_element(arr, 4))

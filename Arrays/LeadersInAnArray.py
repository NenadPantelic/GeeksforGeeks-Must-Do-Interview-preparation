#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:06:22 2020

@author: nenad
"""


def leaders_in_array(arr):
    n = len(arr)
    maxx = arr[-1]
    #counter = 1
    leaders = [arr[-1]]
    for i in range(n-2, -1, -1):
        # only elements which have property that all the elements right to them are smaller than themselves are leaders
        if arr[i] >= maxx:
            maxx = arr[i]
            leaders.append(maxx)
    for i in range(len(leaders)-1,-1,-1):
        print(leaders[i], end=" ")
    print()
    
    
# Test 1
arr = [16,17,4,3,5,2]
leaders_in_array(arr)

# Test 2
arr = [1,2,3,4,0]
leaders_in_array(arr)

# Test 3
arr = [7,4,5,7,3]
leaders_in_array(arr)



t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    leaders_in_array(arr)
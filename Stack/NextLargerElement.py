#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:59:25 2020

@author: nenad
"""


def next_larger_element(arr):
    n = len(arr)
    positions = [None] * n
    values = [-1] * n
    for i in range(n-1, -1, -1):
        # last element has no element greater than hime
        if i == n-1: continue
        # check next element
        if arr[i] < arr[i+1]:
            positions[i] = i + 1
            values[i] = arr[i+1]
        # search for larger element
        else:
            # check greater values of previous element
            next_position = positions[i+1]
            while next_position:
                # check  larger element of the next element in sequence
                value = arr[next_position]
                # larger element found
                if arr[i] < value:
                    positions[i] =  next_position
                    values[i] = value
                    break
                # go further
                else:
                    next_position = positions[next_position]
    for val in values:
        print(val, end=" ")
    print() 
        
        
# # Test 1                    
# arr = [1,3,2,4]
# next_larger_element(arr)



# # Test 2                    
# arr = [4,3,2,1]
# next_larger_element(arr)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    next_larger_element(arr)
        
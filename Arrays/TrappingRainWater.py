#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:50:11 2020

@author: nenad
"""


def trappingWater(arr, n):
    total = 0
    # left pointer
    left = 0
    # right pointer
    right = n-1
    
    left_max = right_max = 0
    while left < right:
        
        if arr[left] < arr[right]:
            # update left max
            if arr[left] > left_max:
                left_max = arr[left]
            # add this difference to total - water will fill this gap
            else:
                total += left_max - arr[left]
            # move left pointer to the right                
            left += 1
        else:
            # update right max
            if arr[right] > right_max:
                right_max = arr[right]
            # add this difference to total - water will fill this gap
            else:
                total += right_max - arr[right]
               # move right pointer to the right 
            right -= 1
    return total


# Test 1
arr = [3,0,0,2,0,4]
print(trappingWater(arr, 6))

# Test 2
arr = [7,4,0,9]
print(trappingWater(arr, 4))

        
# Test 3
arr = [6,9,9]
print(trappingWater(arr, 3))

# Test 4
arr = [5,4,6, 3,2,1]
print(trappingWater(arr,6))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:05:06 2020

@author: nenad
"""

# apply bubble sort and count no of inversions
def counting_inversions(arr):
    n = len(arr)
    inversion_no = 0
    for i in range(n):
        # last i element are sorted
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                inversion_no += 1
    return inversion_no
    #return arr
                

arr = [2,4,1,3,5]
print(counting_inversions(arr))


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(counting_inversions(arr))
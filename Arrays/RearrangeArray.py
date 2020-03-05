#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:56:39 2020

@author: nenad
"""


def rearrange_arr(arr):
    n = len(arr)
    # n/2 iterations
    for i in range(n//2):
        # next max element
        tmp = arr[-1]
        # we traverse backward and shift all elements for one place to the right; we move only those elements that
        # are not positioned well (elements starting from 2*i index)
        for j in range(n-2, 2*i-1, -1):
            arr[j+1] = arr[j]
            #print(arr[j])
        arr[2*i] = tmp
            

def rearrange_arr(arr):
    n = len(arr)
    i, j = 0, n-1
    while i <= j:
        if (i != j):
            print(arr[j], end=" ")
            print(arr[i], end=" ")
        else:
            print(arr[i], end=" ")
        i += 1
        j -= 1
    print()

arr = [1,2,3,4,5,6]
rearrange_arr(arr)

arr = [1,2,3,4,5,6, 7]
rearrange_arr(arr)


def print_arr(arr):
    for val in arr:
        print(val, end=" ")
    print()

# Testing
t = int(input())
for i in range(t):
    n= int(input())
    arr = input().split()
    rearrange_arr(arr)
    #print_arr(arr)
    
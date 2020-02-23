#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:21:57 2020

@author: nenad
"""


def minimize_the_heights(arr, k):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0] - k
    
    for i in range(n-1):
        if arr[i] < arr[i+1]:
            arr[i] += k
        else:
            arr[i] -= k
    if arr[n-1] > arr[n-2]: arr[n-1] -= k
    else: arr[n-1] += k
    
    minn = 500
    for i in range(n-1):
        
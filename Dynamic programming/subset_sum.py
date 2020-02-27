#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:56:38 2020

@author: nenad
"""


def subset_sum(arr, sum_val):
    n = len(arr)
    dp = [[False for i in range(sum_val+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1,n+1):
        for j in range(1,sum_val+1):
            # element is greater than sum 
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]] 
                
    #print(dp)
    print(get_numbers(arr, dp))
    return dp[n][sum_val]

def get_numbers(arr, dp):
    if not dp[-1][-1]:
        return []
    i = len(dp)-1
    j = len(dp[0])-1
    #print(dp)
    numbers = []
    while j > 0 and i > 0:
        while dp[i-1][j]:
            i -= 1  
        else:
            numbers.append(arr[i-1])
            j -= arr[i-1]
    return numbers

# Test 1
arr = [3,34,4,12,5,2]
sum_val = 9
print(subset_sum(arr, sum_val))
print()

# Test 2
sum_val = 12
print(subset_sum(arr, sum_val))
print()

# Test 3
sum_val = 40
print(subset_sum(arr, sum_val))
print()

# Test 3
sum_val = 200
print(subset_sum(arr, sum_val))
print()

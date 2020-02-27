#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:44:18 2020

@author: nenad
"""


def longest_increasing_subsequence(arr):
    n = len(arr)
    # dp array - stores length of lic so far, to that element (lic = longest incr. subseq.)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            # if there is increasing order - update length, if it is better than current state
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], 1 + dp[j])
    # search for max value in dp
    return max(dp)



# Test 1
arr = [5,8,3,7,9,1]
print(longest_increasing_subsequence(arr))

# Test 2
arr = list(map(int, "0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15".split()))
print(longest_increasing_subsequence(arr))

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(longest_increasing_subsequence(arr))

    
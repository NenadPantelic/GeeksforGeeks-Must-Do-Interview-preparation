#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:30:48 2020

@author: nenad
"""


def rod_cutting(n, values):
    # n x n+1 matrix
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    # length of 0th item is 1 - so profit is equal to i * profit[0]
    for i in range(n+1):
        dp[1][i] = i * values[0]
        
    for i in range(1,n+1):
        for j in range(1, n+1):
            # piece is longer than rod - use previous piece result
            if i > j:
                dp[i][j] = dp[i-1][j]
            else:
                print(i,j)
                # take maximum of previous piece result and sum of value of current part and state of
                # remaining length after we cut the current part from rod
                dp[i][j] = max(dp[i-1][j], values[i] + dp[i][j-i])
    return  dp[n][n]

# Test 1
n = 8
#lengths = list(range(1,n+1))
values = [1,5,8,9,10,17,17,20]

print(rod_cutting(n, values))

t = int(input())
for i in range(t):
    n = int(input())
    values = list(map(int, input().split()))
    print(rod_cutting(n, values))

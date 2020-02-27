#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:33:56 2020

@author: nenad
"""
# raise TLE

def knapsack_01(values, weights, W):
    '''
    

    Parameters
    ----------
    values : list of ints
        value of every item.
    weights : list of ints
        weight of item.
    W : int
        total weight of knapsack.
    - all int values are >= 0
    Returns int
    -------
    Returns maximum possible value of subset which total weight should be <= W.

    '''
    n = len(values)
    dp = [[0 for i in range(W+1)] for j in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(W+1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
    #print(dp)
    return dp[n][W]


def knapsack_01_optim(values, weights, W):
    '''
    

    Parameters
    ----------
    values : list of ints
        value of every item.
    weights : list of ints
        weight of item.
    W : int
        total weight of knapsack.
    - all int values are >= 0
    Returns int
    -------
    Returns maximum possible value of subset which total weight should be <= W.

    '''
    n = len(values)
    # vector instead of matrix
    dp = [0 for i in range(W+1)]
    
    # update just positions (items)  which weights can fit into the particular weight (<= W)
    for i in range(n):
        j = W
        while j >= weights[i]:
            dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
            j -= 1
    #print(dp)
    return dp[W]

# # Testing
# t = int(input())
# for i in range(t):
#     n = int(input())
#     W = int(input())
#     weights = list(map(int, input().split()))
#     values = list(map(int, input().split()))
#     print(knapsack_01(values, weights, W))
    
# Test 1
W = 4
values = [1,2,3]
weights = [4,5,1]
print(knapsack_01(values, weights, W))
print(knapsack_01_optim(values, weights, W))


# Test 2
W = 4
values = [1,2,3]
weights = [4,5,6]
print(knapsack_01(values, weights, W))
print(knapsack_01_optim(values, weights, W))


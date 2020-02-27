#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:11:15 2020

@author: nenad
"""


def min_coins(amount, values):
    n = len(values)
    # dp table - stores number of coins required to make amount
    dp = [[0 for i in range(amount+1)] for j in range(n)]
    # set base case for value of coin = 1
    for i in range(amount+1):
        dp[0][i] = i
    for i in range(1,n):
        for j in range(1, amount+1):
            # value of coin is greater than amount
            if values[i] > j:
                # if i==0 set zero
                dp[i][j] = dp[i-1][j]# if i > 0 else 0
            else:
                # better state - number of coins we need for the amount if we don't use this value or
                # or use this coin and check the number of coins we used to form the remaining
                # e.g  j = 7, values[i] = 3 -> use 3, remaining is 4, check how we got 4 previously
                # if i==0
                #dp[i][j] = min(dp[i-1][j] if i > 0 else float("inf"), 1 + dp[i][j-values[i]])
                dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-values[i]])
                
    #print(dp)
    return  dp[n-1][amount]


    
# Test 1
amount = 43
values = [1,2,5,10,20,50,100,200,500,2000]
print(min_coins(amount, values))

# Test 2
amount = 200
values = [1,2,5,10,20,50,100,200,500,2000]
print(min_coins(amount, values))
    


# Test 3
amount = 8
values = [1,2,5,10,20,50,100,200,500,2000]
print(min_coins(amount, values))

t = int(input())
values = [1,2,5,10,20,50,100,200,500,2000]
for i in range(t):
    amount = int(input())
    print(min_coins(amount, values))
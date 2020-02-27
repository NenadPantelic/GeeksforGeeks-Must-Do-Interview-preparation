#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:53:41 2020

@author: nenad
"""

# Count minimum number of edit operations to convert s1 to s2
def edit_distance(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    # dp table - store min number od edit operations
    dp = [[0 for i in range(len1+1)] for j in range(len2+1)]
    # case - empty s1 (we need to insert chars to form s2 then)
    for i in range(len2+1):
        dp[i][0] = i
    # case - empty s2 (we need to remove chars to get s2 then)
    for i in range(len1+1):
        dp[0][i] = i
        
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            # current chars are the same
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # we need an edit (1+ term) and we choose the best previous state 
                # i-1,j insert
                # i, j-1 remove
                # i-1, j-1 replace
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])
    return dp[len2][len1]

# Test 1
s1 = "geek"
s2 = "gesek"
print(edit_distance(s1, s2))

t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    s1, s2 = input().split()
    print(edit_distance(s1, s2))
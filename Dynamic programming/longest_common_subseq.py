#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:40:25 2020

@author: nenad
"""

# Longest Common Subsequence
def lcs(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[0 for i in range(n2+1)] for j in range(n1+1)]
    
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            # if chars are equal, observe value of previous substring without last char of current substrings
            # e.g. ABCD, AGD, we are on D on both substrings, we check ABD and AG and add 1 because "D's" are equal
            if s1[i-1] == s2[j-1]:
                # +1 - because chars are equal
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                # e.g. AFG and ACB, G and B are not equal, so we get max from comparisons: {AFG, AC} and {AF, ACB}
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n1][n2]



def lcs_rec(s1, s2):
    # one string is empty
    if len(s1) == 0 or len(s2) == 0:
        return 0
    
    # first char is equal, check other chars -> ABCD, AFCG -> 1 + lcs_rec*BCD, FCG)
    if s1[0] == s2[0]:
        return 1 + lcs_rec(s1[1:], s2[1:])
    # get the better result - ABFG, SEGA -> max(lcs_rec(ABFG, EGA), lcs_rec(BFG, SEGA))
    else:
        return max(lcs_rec(s1, s2[1:]), lcs_rec(s1[1:], s2))

# Test 1
s1 = "ABCDGH"
s2 = "AEDFHR"
print(lcs(s1, s2))
print(lcs_rec(s1, s2))   



# Test 2
s1 = "ABC"
s2 = "AEC"
print(lcs(s1, s2))
print(lcs_rec(s1, s2))   


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    s1 = input()
    s2 = input()
    print(lcs(s1, s2))
    # TLE
    print(lcs_rec(s1, s2))
 
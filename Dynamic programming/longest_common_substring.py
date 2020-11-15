#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:25:45 2020

@author: nenad
"""


"""
URL: https://practice.geeksforgeeks.org/problems/longest-common-substring/0
"""
# Time and space: O(m*n)
def longestCommonSubstring(s1, s2):
    m, n = len(s1), len(s2)
    if m == 0 or n == 0:
        return 0
    maxLen = 0
    dp = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                maxLen = max(maxLen, dp[i][j])
    
    return maxLen

s1 = "abcdgh"
s2 = "acdghr"

print(longestCommonSubstring(s1, s2))

s1 = "abc"
s2 = "ac"

print(longestCommonSubstring(s1, s2))

s1 = "abac"
s2 = "abba"

print(longestCommonSubstring(s1, s2))



s1 = "CHZVFRKMLNOZJK"
s2 = "PQPXRJXKITZYXACBHHKICQCOENDTOMFGDWDWFCGPXIQVKUYTDLCGDEWHTACI"

print(longestCommonSubstring(s1, s2))



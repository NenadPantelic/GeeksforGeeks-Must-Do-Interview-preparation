#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:49:14 2020

@author: nenad
"""

# Complexity - Time: O(eggs*floors^2); Space (eggs*floors)
def egg_dropping(eggs, floors):
    """
    

    Parameters
    ----------
    eggs : int (>0)
        Number of eggs.
    floors : int (>0)
        Number of floors.

    Returns int
    -------
    Minimal number of attempts.

    """
    
    dp=[[0 for i in range(floors+1)] for j in range(eggs+1)]
    
    for i in range(1, eggs+1):
        for j in range(floors+1):
            # for one e.g. and j floors we must check all of j possibilities
            if i == 1:
                dp[i][j] = j
                continue
            # number of eggs is greater than number of floors
            if i > j:
                # same as less number of eggs and the same number of floors
                dp[i][j] = dp[i-1][j]
            else:
                # check on every floor
                best_res = floors
                # we traverse over j subfloors
                for k in range(1, j+1):
                    #  one egg less, observe only floors below current one
                    egg_cracked = dp[i-1][k-1]
                    # the same number of eggs, check only floors above j-k of them)
                    egg_n_cracked = dp[i][j-k]# 1 attempt plus
                    tmp_res = max(egg_cracked, egg_n_cracked)
                    if tmp_res < best_res:
                        best_res = tmp_res
                dp[i][j] = 1+best_res
    #print(dp)
    return dp[eggs][floors]

# Test 1
n = 3
k = 5
print(egg_dropping(n,k))


# Test 2
n = 2
k = 10
print(egg_dropping(n,k))


# t = int(input())
# for i in range(t):
#     n,k = list(map(int, input().split()))
#     print(egg_dropping(n,k))
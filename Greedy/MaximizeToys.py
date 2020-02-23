#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:03:51 2020

@author: nenad
"""

def maximize_toys(toys, amount):
    toys.sort()
    for i in range(len(toys)):
        if amount < toys[i]:
            break
        amount -= toys[i]
    # number of toys that were bought
    return i
    
t = int(input())
for i in range(t):
    n, amount = list(map(int, input().split()))
    toys = list(map(int, input().split()))
    print(maximize_toys(toys, amount))

amount = 50
toys = [1, 12, 5, 111, 200, 1000, 10]
print(maximize_toys(toys, amount))
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 22:02:55 2020

@author: nenad
"""


def candy_shop(candies, k):
    min_money = 0
    max_money = 0
    # min case
    # sort candies cost
    candies.sort()
    n = len(candies)
    i = 0 # number of bought candies
    j = n-1 # expensive cakes - k of them per one bought
    
    # max case
    # until indices meet, then all of the candies are bought
    while i <= j:
        min_money += candies[i]
        i += 1
        j -= k
    
    candies.sort(reverse = True)
    i = 0
    j = n-1
    # until indices meet, then all of the candies are bought
    while i <= j:
        max_money += candies[i]
        i += 1
        j -= k
    return (min_money, max_money)
    
    
    

# Test 1
arr = [3, 2, 1, 4]
k  = 2
money = candy_shop(arr,k)
print("{} {}".format(money[0], money[1]))
t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    candies = list(map(int, input().split()))
    money = candy_shop(candies,k)
    print("{} {}".format(money[0], money[1]))

        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:49:50 2020

@author: nenad
"""


def min_coins_greedy(amount, values):
    while amount != 0:
        for i in range(len(values)-1, -1, -1):
            if amount >= values[i]:
                print(values[i], end=" ")
                amount -= values[i]
                break
    print()


#Test 1
amount = 43
values = [1,2,5,10,20,50,100,200,500,2000]
min_coins_greedy(amount, values)

# Test 2
amount = 200
values = [1,2,5,10,20,50,100,200,500,2000]
min_coins_greedy(amount, values)
    


# Test 3
amount = 8
values = [1,2,5,10,20,50,100,200,500,2000]
min_coins_greedy(amount, values)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:16:30 2020

@author: nenad
"""


#code

# version 1
def equilibrium_point(arr):
    n = len(arr)
    cumsum_forward = [None] * n
    cumsum_backward = [None] * n
    
    cumsum_forward[0] = arr[0]
    cumsum_backward[-1] = arr[-1]
    for i in range(1, n):
        cumsum_forward[i] = cumsum_forward[i-1] + arr[i]
        cumsum_backward[-1-i]=cumsum_backward[-i] + arr[-1-i]
        
    for i in range(n):
        if cumsum_forward[i] == cumsum_backward[i]:
            return i+1
    return -1

# version 2     
def equilibrium_point(arr):
    n = len(arr)
    cumsum_forward = [None] * n
    #cumsum_backward = [None] * n
    
    cumsum_forward[0] = arr[0]
    #cumsum_backward[-1] = arr[-1]
    for i in range(1, n):
        cumsum_forward[i] = cumsum_forward[i-1] + arr[i]
        #cumsum_backward[-1-i]=cumsum_backward[-i] + arr[-1-i]
    
    # total sum
    total_sum = cumsum_forward[-1]
    #print(total_sum)
    for i in range(n):
        if cumsum_forward[i] == total_sum:
            return i+1
        total_sum -= arr[i]

    return -1


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(equilibrium_point(arr))
    


# Test 1
arr = [1,3,2,4]
print(equilibrium_point(arr))


# Test 2
arr = [1,3,5,2,2]
print(equilibrium_point(arr))


# Test 3
arr = [1]
print(equilibrium_point(arr))


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(equilibrium_point(arr))
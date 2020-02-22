#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:48:24 2020

@author: nenad
"""
from collections import deque

# sorted dequeue - slidding window
def maximum_of_k_subarrs(arr, k):
    # window of size k
    n = len(arr)
    d = deque()
    #maxx = []
    for i in range(n):
        # remove elements from deque that're less than current element
        while len(d) > 0 and int(arr[i])>= int(arr[d[-1]]):
            d.pop()
        # add index of the element to deque
        d.append(i)
        # remove all elements that do not belong to this window
        while d[0] <= i-k:
            # remove first element from deque - max element
            d.popleft()
            
        # for every position greater or equal than k add max element from deque (ar 0 index) -> in arr of length n with k-size window we have n-k+1 subarray
        if i >= k-1:
            print(int(arr[d[0]]), end=" ")
    print()
        
    #return maxx
# t = int(input())
# for i in range(t):
#     n, k = input().split()
#     arr = input().split()
#     #maxes = 
#     maximum_of_k_subarrs(arr,int(k))
#     # for max in maxes:
#     #     print(max, end=" ")
#     # print()

# Test 1   
arr = [1,2,3,1,4,5,2,3,6]
print(maximum_of_k_subarrs(arr,3))

# Test 2
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
print(maximum_of_k_subarrs(arr,3))

# Test 3
arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
print(maximum_of_k_subarrs(arr,4))

# Test 4
a = list(map(int,"765 992 1 521 220 380 729 969 184 887 104 641 909 378 724 582 387 583 241 294 159 198 653 369 418 692 36 901 516 623 703 971 304 394 491 525 464 219 183 648 796 287 979 395 356 702 667 743 976 908 728 134 106 380 193 214 71 920 114 587 543 817 248 537 901 739 752 364 649 626 702 444 913 681 529 959 72 196 392 738 103 119 872 900".split()))
k = 47
print(maximum_of_k_subarrs(a,k))
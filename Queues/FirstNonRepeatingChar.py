#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 20:17:09 2020

@author: nenad
"""


def non_repeating_char(arr):
    freq = {}
    queue = []
    for el in arr:
        freq[el] = val = freq.get(el, 0) + 1
        if val == 1:
            queue.append(el)

        while len(queue) and freq[queue[0]]  != 1:
            queue.pop(0)
        if len(queue) == 0:
            print(-1, end = " ")
        else:
            print(queue[0], end=" ")
        #print(queue)
    print()
# Test 1
arr = ['a', 'a', 'b', 'c']
non_repeating_char(arr)
# Test 2
arr = ['a', 'a', 'c']
non_repeating_char(arr)
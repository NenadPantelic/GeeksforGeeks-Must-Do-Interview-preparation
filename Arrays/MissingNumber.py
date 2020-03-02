#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:18:25 2020

@author: nenad
"""


def missingNumber(A):
    A.sort()
    counter = 1
    for i in range(len(A)):
        # if A[i] <= 0 or A[i] < counter:
        #     continue
        if A[i] != counter:
            return counter
        counter += 1
    return counter
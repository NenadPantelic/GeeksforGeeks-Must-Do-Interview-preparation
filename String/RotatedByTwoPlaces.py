#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:02:04 2020

@author: nenad
"""


def rotated_by_two(s1,s2):
    for i in range(len(s1)):
        # condition violation
        if s1[i] != s2[i-2]:
            return 0
    return 1


t = int(input())
for i in range(t):
    s1 = input()
    s2 = input()
    print(rotated_by_two(s1, s2) or rotated_by_two(s2, s1))
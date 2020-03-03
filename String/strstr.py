#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:02:46 2020

@author: nenad
"""


def strstr(string, sub):
    # length of substring we're looking for
    sublen = len(sub)
    for i in range(len(string)-sublen+1):
        if string[i:i+sublen] == sub:
            return i
    return -1


# Test 1
string = "GeeksForGeeks"
print(strstr(string,"Fr"))
print(strstr(string,"For"))
print(strstr(string,"ks"))
        
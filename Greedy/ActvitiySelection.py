#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:56:22 2020

@author: nenad
"""

from collections import defaultdict
def count_activities(start, end):
    activity_len = defaultdict(list)
    for i in range(len(start)):
        activity_len[end(i)-start(i)].append((start[i], end[i]))
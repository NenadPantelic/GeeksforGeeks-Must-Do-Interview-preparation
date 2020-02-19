#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:19:21 2020

@author: nenad
"""


def get_nth_from_last(head, n):
    # determine length
    length = 0
    node = head
    while node:
        node = node.next
        length += 1
    # target index
    middle = length - n
    if middle < 0:
        return -1
    i = 0
    node = head
    # find target element
    while i < middle:
        node = node.next
        i += 1
    return node.data



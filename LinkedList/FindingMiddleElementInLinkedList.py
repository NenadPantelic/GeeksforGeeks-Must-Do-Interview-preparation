#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:13:16 2020

@author: nenad
"""


def find_mid(head):
    # determine length
    length = 0
    node = head
    while node:
        node = node.next
        length += 1
    # middle index
    middle = length // 2
    i = 0
    node = head
    # find middle element
    while i < middle:
        node = node.next
        i += 1
    return node
    
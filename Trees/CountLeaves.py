#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:57:55 2020

@author: nenad
"""


def count_leaves(root):
    if root is None: return 0
    if root.left is None and root.right is None:
        return 1 + count_leaves(root.left) + count_leaves(root.right)
    
    return  count_leaves(root.left) + count_leaves(root.right)
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:53:51 2020

@author: nenad
"""
"""
https://practice.geeksforgeeks.org/problems/symmetric-tree/1
"""

def isSymmetric(root):
    def checkSymetry(left, right):
        if left is right is None:
            return True
        if left is None or right is None:
            return False
        return left.data == right.data and checkSymetry(left.right, right.left) \
            and checkSymetry(left.left, right.right)
    if root is None: return True
    return checkSymetry(root.left, root.right)
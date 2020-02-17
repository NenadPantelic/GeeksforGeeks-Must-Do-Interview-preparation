#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 12:48:34 2020

@author: nenad
"""

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    
    if root is None:
        return 0
    # Diameter goes through root
    diam_inc_root = height(root.left) + height(root.right) + 1
    # otherwise
    diam_exc_root = max(diameter(root.left), diameter(root.right))
    return max(diam_inc_root, diam_exc_root)

# Test 1
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print(diameter(root))    
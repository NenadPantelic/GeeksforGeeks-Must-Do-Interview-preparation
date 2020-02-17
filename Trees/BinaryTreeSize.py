#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:09:24 2020

@author: nenad
"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
# count number of nodes in BT
def size(root):
    if root is None:
        return 0
    # size of left subtree + size of right subtree + 1
    return 1 + size(root.left) + size(root.right)

# Test 1
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)
print(size(root))   
    
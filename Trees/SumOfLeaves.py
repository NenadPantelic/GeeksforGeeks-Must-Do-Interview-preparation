#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:57:48 2020

@author: nenad
"""

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
def sum_leaf(root):
    '''
    :param root: root of given tree.
    :return: sum of leaf nodes
    '''
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    return sum_leaf(root.left) + sum_leaf(root.right)

# Test 1
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)
print(sum_leaf(root))
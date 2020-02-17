#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:04:48 2020

@author: nenad
"""

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def is_identical(root1, root2):
    # both trees are empty
    if root1 is None and root2 is None:
        return True
    # one of the trees is empty
    if root1 is None or root2 is None:
        return False
    # root values or of both of the trees are the same
    if root1.data == root2.data:
        # check subtrees
        return is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)
    return False
        
#Test 1
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 


root2 = Node(1) 
root2.left = Node(2) 
root2.right = Node(3) 
root2.left.left = Node(4) 
root2.left.right = Node(5) 

print(is_identical(root, root2))


#Test 2
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 


root2 = Node(1) 
root2.left = Node(2) 
root2.right = Node(3) 
root2.left.left = Node(4) 
root2.left.right = None 

print(is_identical(root, root2))
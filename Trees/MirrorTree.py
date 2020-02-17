#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:33:55 2020

@author: nenad
"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
        
def mirror(root):
    if root is None:
        return 
    mirror(root.left)
    mirror(root.right)
    root.left, root.right = root.right, root.left
    #return

def inorder( node):
    if node is None:
        return
    # recurse left
    inorder(node.left)
    # print value
    print(node.data, end=" ")
    #recurse right
    inorder(node.right)
    
#Test 1
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)
inorder(root)
print()
mirror(root)
inorder(root)
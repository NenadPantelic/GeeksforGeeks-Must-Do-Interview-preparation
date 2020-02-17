#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:52:45 2020

@author: nenad
"""

def height(root):
    '''
    :param root: root of the given tree.
    :return: Integer, height of the given binary tree
    {
        # Node Class:
        class Node:
            def _init_(self,val):
                self.data = val
                self.left = None
                self.right = None
    }
    '''
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))
    



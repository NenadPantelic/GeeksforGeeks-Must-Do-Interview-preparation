#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:56:44 2020

@author: nenad
"""


def detectLoop(head):
    #code here
    visited_nodes = set()
    node = head
    
    while node:
        node_id = id(node)
        # already visited - loop detected
        if node_id in visited_nodes:
            return True
        visited_nodes.add(node_id)
        node = node.next
    
    return False
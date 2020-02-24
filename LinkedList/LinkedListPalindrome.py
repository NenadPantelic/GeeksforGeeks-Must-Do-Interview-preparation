#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:31:07 2020

@author: nenad
"""
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# check if the given list is palindrome
def is_palindrome(head):
    # determine length of ll
    length = 0
    node = head
    nodes = {}
    # put nodes in map
    while node:
        nodes[length] = node.data
        length += 1
        node = node.next

    
    for i in range(length//2):
        # check node on symetrical position - from the beginning and from the end
        if nodes[i] != nodes[length-1-i]:
            return False
    return True

# second approach is to set first half of the nodes to stack and traverse through second half and compare every node
# with the one got when we pop from the stack

# Test 1
n1 = Node(1)
n2 = Node(2)
n3 = Node(1)
n1.next= n2
n2.next = n3
print(is_palindrome(n1))



# Test 2
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.next= n2
n2.next = n3
n3.next = n4
print(is_palindrome(n1))
    
    
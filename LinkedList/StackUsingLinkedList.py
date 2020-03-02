#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:44:05 2020

@author: nenad
"""


class StackNode:

	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None

# add to head, remove from head
class Stack:
    def __init__(self):
        self.head = None
    # The method push to push element into
    # the stack
    def push(self, data):
        node = StackNode(data)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
        # Add code here

        # The method pop which return the element
        # poped out of the stack

    def pop(self):

        # Add code here
        if self.head:
            val = self.head.data
            self.head = self.head.next
            return val
        return -1

# Test 1    
ms = Stack()
ms.push(2)
ms.push(3)
print(ms.pop())
ms.push(4)
print(ms.pop())

# Test 2
ms2 = Stack()
print(ms2.pop())
ms2.push(4)
ms2.push(5)
print(ms2.pop())

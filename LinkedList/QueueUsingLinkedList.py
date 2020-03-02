#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:24:07 2020

@author: nenad
"""


# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None

# add to tail, remove from head    
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
     # Method to add an item to the queue
    def push(self, item): 
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
           self.tail.next = node
           self.tail = node
           
           
    # Method to remove an item from queue
    def pop(self):
        if self.head:
            value = self.head.data
            self.head = self.head.next
            return value
        
        return -1
         

# Test 1
mq = MyQueue()
mq.push(2)
mq.push(3)
print(mq.pop())
mq.push(1)
print(mq.pop())


# Test 2
mq2 = MyQueue()
mq2.push(2)
print(mq2.pop())
print(mq2.pop())
mq2.push(3)
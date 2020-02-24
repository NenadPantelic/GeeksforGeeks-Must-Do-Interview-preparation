#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:48:02 2020

@author: nenad
"""


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
def merge(head_a,head_b):
    
    # point to nodes of list a
    node_a = head_a
    
    # point to nodes of list b
    node_b = head_b
    
    node = None
    head = None
    
    # until we reach the end of the shorter list
    while node_a and node_b:
        # compare two nodes
        if node_a.data <= node_b.data:
            # if we have head node
            if node:
                node.next = node_a
                node = node_a
            else:
                head = node_a
                node = node_a
            # pick next node in list a
            node_a = node_a.next
        else:
            if node:
                node.next = node_b
                node = node_b
            else:
                head = node_b
                node = node_b
            node_b = node_b.next
            
    # just one of these two cases will be true
    # go to the end of the list
    while node_a:
        node.next = node_a
        node = node_a
        node_a = node_a.next
    # go to the end of the second list
    while node_b:
        node.next = node_b
        node = node_b
        node_b = node_b.next
    return head

# Test 1
# List 1
n1 = Node(2)
n2 = Node(4)
n3 = Node(11)
n1.next = n2
n2.next = n3

# List 2
n4 = Node(1)
n5 = Node(7)
n6 = Node(10)

n4.next = n5
n5.next = n6

head = merge(n1, n4)
node = head
while node:
    print(node.data, end=" ")
    node = node.next
print()


# Test 2
# List 1
n1 = Node(2)
n2 = Node(4)
n3 = Node(11)
n7 = Node(14)
n1.next = n2
n2.next = n3
n3.next = n7 

# List 2
n4 = Node(1)
n5 = Node(7)
n6 = Node(10)

n4.next = n5
n5.next = n6

head = merge(n1, n4)
node = head
while node:
    print(node.data, end=" ")
    node = node.next
print()

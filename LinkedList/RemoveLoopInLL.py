#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:42:33 2020

@author: nenad
"""


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
def removeTheLoop(head):
    # prev node
    node = head
    prev_node = node
    visited_nodes = set()
    while node:
        node_id = id(node)
        # if node is already visited we have a loop
        if node_id in visited_nodes:
            # remove loop - for previous node set next None as next node (terminate list)
            prev_node.next = None
            break
        visited_nodes.add(node_id)
        prev_node = node
        node = node.next
        
    return head


def print_list(head):
    node = head
    while node:
        print(node.data, end= " ")
        node = node.next
    print()

# Test 1
n1 = Node(1)
n2 = Node(3)
n3 = Node(4)
n1.next = n2
n2.next = n3
n3.next = n2

head = removeTheLoop(n1)
print_list(head)

# Test 2
n1 = Node(1)
n2 = Node(8)
n3 = Node(3)
n4 = Node(4)
n1.next = n2
n2.next = n3
n3.next = n4


head = removeTheLoop(n1)
print_list(head)

    



        
    
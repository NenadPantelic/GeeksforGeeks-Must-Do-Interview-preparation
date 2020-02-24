#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 22:26:37 2020

@author: nenad
"""

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
# rotate ll for k places counter-clockwise
# optimize it - not the best solution
def rotate(head, k):
    # count number of nodes in ll
    count = 0
    node = head
    # memorize positions of every node
    pos_map = {}
    
    while node:
        count += 1
        pos_map[count] = node
        prev_node = node
        node = node.next
    
    # position of new head element
    new_head_pos = (k+1) % count
    # convert negative position in positive - backward index to forward index
    if new_head_pos <= 0:
        new_head_pos += count
    # position of new tail element
    new_tail_pos= new_head_pos-1
    # convert negative position in positive - backward index to forward index
    if new_tail_pos <= 0:
        new_tail_pos += count
    # new tail
    new_tail = pos_map[new_tail_pos]
    # terminate list
    new_tail.next = None
    # in case that last node in original order is also last in new rotated order
    if prev_node is not new_tail:
        prev_node.next = head
    return pos_map[new_head_pos]

def print_list(head):
    node = head
    while node:
        print(node.data, end= " ")
        node = node.next
    print()
 # Test 1
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8

head = rotate(n1, 4)
print_list(head)


# Test 2
n1_ = Node(2)
n2_ = Node(4)
n3_ = Node(7)
n4_ = Node(8)
n5_ = Node(9)

n1_.next = n2_
n2_.next = n3_
n3_.next = n4_
n4_.next = n5_


head = rotate(n1_, 3)
print_list(head)


# Test 3
n1_ = Node(1)
n2_ = Node(2)


n1_.next = n2_



head = rotate(n1_, 3)
print_list(head)

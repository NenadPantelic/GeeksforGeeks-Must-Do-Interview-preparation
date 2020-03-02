#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:58:39 2020

@author: nenad
"""
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

def pairwise_swap(head):
    # list contains at least one element, so there is no need to check
    A = head
    B = C = D = None
    if A.next:
        head = A.next
    while A and A.next:
        B = A.next
        C = B.next
        print(A.data,B.data,C.data)
        # swap adjacent nodes
        if D:
            D.next = B
        B.next = A
        A.next = C
        # last node in swapping
        D = A
        # move node for two places
        A = C
    return head

# Test 1
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7


def print_list(head):
    node = head
    while node:
        print(node.data, end=" ")
        node = node.next
    print()
    
head = pairwise_swap(n1)
print_list(head)
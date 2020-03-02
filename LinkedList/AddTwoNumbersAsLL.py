#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:01:21 2020

@author: nenad
"""


'''
	Function to add two numbers represented 
	in the form of the linked list.
	
	Function Arguments: head_a and head_b (heads of both the linked lists)
	Return Type: head of the resultant linked list.
    
    __>IMP : numbers are represented in reverse in the linked list.
    Ex:
        145 is represented as  5->4->1.
    
    resultant head is expected in the same format.
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
def addBoth(head_a,head_b):
    #code here
    
    # pointer to the first ll node
    node_a = head_a
    # pointer to the second ll node
    node_b = head_b
    
    new_head = None
    node = None
    #prev_node = None
    
    acc = 0
    # iterate for (min of lengths of lls) steps
    while node_a and node_b:
        val = node_a.data + node_b.data + acc
        if node is None:
            node = Node(val%10)
            new_head = node
        else:
            node.next = Node(val%10)
            node = node.next
            
        acc = val // 10
        node_a = node_a.next
        node_b = node_b.next
    
    # iterate for the rest of the list a if this list is longer
    while node_a:
        val = acc + node_a.data
        acc = val // 10
        node.next = Node(val%10)
        node = node.next
        node_a = node_a.next
    
    # iterate for the rest of the list b if this list is longer
    while node_b:
        val = acc + node_b.data
        acc = val // 10
        node.next = Node(val % 10)
        node = node.next
        node_b = node_b.next
        
    # if there is situation that when we sum MSDs of both lists and we have result greater than 9; use that carry as new digit
    if acc != 0:
        node.next = Node(acc)
        node = node.next
    return new_head


# Test 1
# n1 = Node(5)
# n2 = Node(4)
# n3 = Node(3)

# n1.next = n2
# n2.next = n3

# n4 = Node(5)
# n5 = Node(4)
# n4.next = n5

# Test 2
# n1 = Node(0)
# n2 = Node(0)
# n3 = Node(8)

# n1.next = n2
# n2.next = n3

# n4 = Node(0)
# n5 = Node(0)
# n6 = Node(2)
# n4.next = n5
# n5.next = n6


# Test 3
    
# n1 = Node(6)
# n2 = Node(6)
# #n3 = Node(8)

# n1.next = n2
# #n2.next = n3

# n4 = Node(7)
# #n5 = Node(0)
# ##n6 = Node(2)
# ##n4.next = n5
# #n5.next = n6
    

n1 = Node(1)
n2 = Node(8)
n3 = Node(4)
n4 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4

n5 = Node(6)
n6 = Node(8)
n7 = Node(5)
n8 = Node(2)
n5.next = n6
n6.next = n7
n7.next = n8
def print_list(head):
    node = head
    while node:
        print(node.data, end=" ")
        node = node.next
    print()
    
head = addBoth(n1, n5)
print_list(head)


    
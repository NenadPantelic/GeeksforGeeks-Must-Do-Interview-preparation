#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:11:12 2020

@author: nenad
"""


'''
    :param x: value to be inserted
    :return: None

    queue_1 = [] # first queue
    queue_2 = [] # second queue
    '''
queue_1, queue_2 = [],[]
def push_in_stack(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    queue_2.append(x)
    for i in range(len(queue_1)):
        queue_2.append(queue_1.pop(0))
    queue_1, queue_2 = queue_2, queue_1
    
def pop_from_stack():
    '''
    :return: the value of top of stack and pop from it.
    '''
    
    # global declaration
    global queue_1
    global queue_2
    
    if len(queue_1) == 0:
        return -1
    return queue_1.pop(0)
    
        

push_in_stack(2)
push_in_stack(3)
print(queue_1, queue_2)
print(pop_from_stack())
push_in_stack(4)
print(pop_from_stack())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:28:39 2020

@author: nenad
"""

# stack1 for pushing
# stack2 for poping
def qPush(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    stack1.append(x)

    

def qPop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    len_1 = len(stack1)
    if len(stack2) == 0:
        while len_1:
            stack2.append(stack1.pop(-1))
            len_1 -= 1
    if len(stack2) == 0:
        return -1
    return stack2.pop(-1)


stack1 = []
stack2 = []
qPush(2, stack1, stack2)
qPush(3, stack1, stack2)
print(qPop(stack1, stack2))
qPush(4, stack1, stack2)
print(qPop(stack1, stack2))
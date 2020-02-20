#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:35:13 2020

@author: nenad
"""


class Stack:
    def __init__(self):
        self.s=[]
        self.minEle=0
        self.size = 0

    def push(self,x):
        if self.size == 0:
            self.s.append(x)
            self.minEle = x
        # we save the info about previous min element by subtracting new min element from prev one, so we can
        # calculate it when the current min element is popped
        else:
            if x >= self.minEle:
                self.s.append(x)
            else:
                self.s.append(x - self.minEle)
                self.minEle = x
        self.size += 1

    def pop(self):
        if self.size <= 0:
            return -1
        ele = self.s.pop(-1)
        if ele >= self.minEle:
            self.size -= 1
            return ele
        else:
            self.size -= 1
            oldMin = self.minEle
            # recalculate prev min element; new one is popped
            self.minEle = oldMin - ele
            return oldMin
         
    def getMin(self):
        if self.size <= 0:
            return -1
        return self.minEle
    
# stack = Stack()
# stack.push(2)
# stack.push(3)
# print(stack.pop())
# print(stack.getMin())
# stack.push(1)
# print(stack.getMin())        
    
    

stack = Stack()
f = open('test2.txt', 'r')
length = int(f.readline())
#data = f.readline().split()
data = ['2', '3', '2', '1', '2', '2', '1', '79', '3', '1', '37', '2', '1', '23', '3', '3', '2', '1', '59', '3', '1', '63', '3', '1', '37', '3', '3', '1', '51', '3', '3', '1', '32', '1', '31', '2', '3', '2', '1', '100', '3', '3', '2', '1', '74', '2', '1', '91', '2', '3', '3', '3', '1', '91']
#print(data)
f.close()
i = 0
while i < length:
    entry = int(data[i])
    if entry == 1:
        stack.push(int(data[i+1]))
        i += 1
    elif entry == 2:
        print(stack.pop())
    else:
        print(stack.getMin())
    i += 1

    
    

    
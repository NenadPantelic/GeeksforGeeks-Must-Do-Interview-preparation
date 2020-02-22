#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:07:41 2020

@author: nenad
"""


'''
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=self.pre=None
'''
class LRUCache:
    # self.queue servers as least-recently used queue - most recent used is at tail
    def __init__(self,cap):
        # cap:  capacity of cache
        #Intialize all variable
        #code here
        self.hsmap=dict()
        self.capacity= cap
        self.count=0

        self.queue = []
            
        
    
    def get(self, key):
        value = self.hsmap.get(key, -1)
        # value present in hsmap
        if value != -1:
            # move key to rear
            index = self.queue.index(key)
            self.queue.pop(index) 
            self.queue.append(key)
        return value
        
          
    def set(self, key, value):
        # key already present
        if key in self.hsmap:
            self.hsmap[key] = value
            index = self.queue.index(key)
            self.queue.pop(index)
            # move key to rear
            self.queue.append(key)
        else:
            # capacity reached
            if self.count == self.capacity:
                element = self.queue.pop(0)
                del self.hsmap[element]
                self.count -= 1
           
            # insert into cache 
            self.hsmap[key] = value
            self.count += 1
            self.queue.append(key)
                        
            
       
        




# # Test 1        
lru = LRUCache(2)
lru.set(1,2)
print(lru.get(1))


# Test 2        
lru = LRUCache(2)
lru.set(1,2)
lru.set(2,3)
lru.set(1,5)
lru.set(4,5)
lru.set(6,7)
print(lru.get(4), end =" ")
print(lru.get(1))
        
#t = int(input())
#for i in range(t):
cap = int(input())
n = int(input())
a = input().split()
lru = LRUCache(cap)
i = 0
q = 1
while q <= n:
    qt = a[i]
    if qt == 'SET':
        lru.set(int(a[i+1]),int(a[i+2]))
        i += 3
    else:
        print(lru.get(int(a[i+1])), end=" ")
        i += 2
    q += 1
        #print()
        
            
        
        


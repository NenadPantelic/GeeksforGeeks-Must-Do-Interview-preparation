#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:21:12 2020

@author: nenad
"""


N = 5
visited = [False] * N
def dfs(g, N, node=0):
    '''
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the dfs of the graph from node 0, newline is given by driver code
    '''
    global visited
    if visited[node]:
        return
    print(node, end=" ")
    visited[node] = True
    for neigh in g[node]:
        dfs(g, N, neigh)
        
        
from collections import deque            
        
def dfs_iter(g, N, source=0):
    visited = [False] * N
    stack = [source]

    while len(stack):
        node = stack.pop(-1)
        if visited[node]:
            continue
        print(node, end=" ")
        visited[node] = True
        neighbours = reversed(g[node])
        for neigh in neighbours:
            if not visited[neigh]:
                stack.append(neigh)
    
   
    
    
    
    
    
    
from collections import defaultdict
# Test 1       
g = defaultdict(list)

g[0] = [1,2,3]
g[2] = [4]
g[1] = [6,7]
g[6] = [8]
#print()
dfs_iter(g, 9)




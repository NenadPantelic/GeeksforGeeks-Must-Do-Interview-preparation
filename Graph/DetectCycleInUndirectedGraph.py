#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:42:33 2020

@author: nenad
"""

from collections import defaultdict
def find_first_unvisited(vis):
    for i in range(len(vis)):
        if not vis[i]:
            return i
    
def isCyclic(g,n):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph
    :return:  boolean (whether a cycle exits or not)
    '''
    q= []
    visited  = [False] * n
    parent = [None] * n
    
    count_visited = 0
    # suppose 0 is the first value in graph
    #visited[0] = True
    count_visited = 1
    visited[0] = True

    q.append(0)
    while len(q) or count_visited != n:
        if not len(q):
            node = find_first_unvisited(visited)
            count_visited += 1
            visited[node] = True
        else:
            node = q.pop(0)
        # adjacent nodes
        nodes = g[node]
        for neigh in nodes:
            if not visited[neigh]:
                visited[neigh] = True
                parent[neigh] = node
                q.append(neigh)
                count_visited += 1
            else:
                # check if that is his parrent or not, it is not, that's a loop
                if parent[node] != neigh:
                    return 1
    return 0
            
        
        


# Test 1
g = defaultdict(list)
g[0] = [1, 0]
g[1] = [0]
print(isCyclic(g, 2))


# Test 2
g = defaultdict(list)
g[0] = [1]
g[1] = [0,2]
g[2] = [1,3]
g[3] = [2]
print(isCyclic(g, 4))

# Test 3

g = defaultdict(list)
g[0] = [1]
g[1] = [0]
g[2] = [3, 4]
g[3] = [2, 4]
g[4] = [3,2]
print(isCyclic(g, 5))
 

        
    
    
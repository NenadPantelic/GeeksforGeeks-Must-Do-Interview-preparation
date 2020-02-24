#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:54:52 2020

@author: nenad
"""

def bfs(graph,N, source=0):
    '''
    can use queue module already imported
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the bfs of the graph from node 0, newline is given by driver code
    '''
    # code here
     # stores info about node visit
    visited = [False] * N
    # queue from where we take nodes
    queue = []#deque()
    queue.append(source)
    visited[source] = True
    print(source, end= " ")
    while len(queue):
        node = queue.pop(0)#.popleft()
        neighs = graph[node]
        for neigh in neighs:
            if visited[neigh]:
                continue
            print(neigh, end=" ")
            queue.append(neigh)
            visited[neigh] = True

from collections import defaultdict
# Test 1       
g = defaultdict(list)

g[0] = [1,2,3]
g[2] = [4]
bfs(g, 5)
        
print()    
# Test 2
g2 = defaultdict(list)
g2[0] = [1,2]
#g[2] = [4]
bfs(g2, 3)
        
    
    
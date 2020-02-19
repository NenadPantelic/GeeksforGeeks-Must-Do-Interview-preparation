#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:21:20 2020

@author: nenad
"""


def dfs_util(start_node, g,visited):
    if visited[start_node]:
        return
    visited[start_node] = True
    #q.append(start_node)
    print(start_node, end=" ")
    neighbours = g[start_node]
    for node in neighbours:
        dfs_util(node,g,visited)
def dfs(g,N):
    '''
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the dfs of the graph from node 0, newline is given by driver code
    '''
    # code here
    start_node = 0
    visited = [False] * N
    return dfs_util(start_node, g,visited)
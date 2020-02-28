#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:32:59 2020

@author: nenad
"""


from heapq import heappush, heappop
# optimize it with indexed pq
def dijkstra(source, graph):
    # number of nodes in graph
    n = len(graph)
    visited = [False] * n
    #prev = [None] * n
    # init distances
    dist = [float('inf')] * n
    # distance from source itself is 0
    dist[source] = 0
    # priority queue
    pq = []
    # heapify with with dist values as comparation value
    heappush(pq, (0, source))
    while len(pq) != 0:
        # node with minimum distance
        min_value, curr_node = heappop(pq)
        visited[curr_node] = True
        for node, distance in graph[curr_node]:
            if visited[node]:
                continue
            new_dist = dist[curr_node] + distance
            if new_dist < dist[node]:
                dist[node] = new_dist
                #prev[node] = curr_node
                heappush(pq, (new_dist, node))
                
    return dist[-1]

def get_matrix(grid, n):
    matr = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            value = i * n + j
            matr[i][j] = grid[value]
    return matr        
            
def convert_matrix_to_adj_list(n, matr):
    g = defaultdict()
    for i in range(n):
        for j in range(n):
            value = i * n + j
            g[value] = []
            # append upper neighbour
            if i > 0:
                g[value].append(((i-1) * n + j, matr[i-1][j]))
            # append left neighbour
            if j > 0:
                g[value].append((i*n +j-1, matr[i][j-1]))
            # append bottom neighbour
            if i < n-1:
                g[value].append(((i+1) * n +j,matr[i+1][j]))
                
                # append right neighbour
            if j < n-1:
                g[value].append((i*n+j+1,matr[i][j+1]))
    return g

from collections import defaultdict

# t = int(input())
# for i in range(t):
#     n = int(input())
#     grid = list(map(int, input().split()))
#     matr = get_matrix(grid, n)
#     graph = convert_matrix_to_adj_list(n, matr)
#     source = 0
#     cost = dijkstra(source, graph) + matr[0][0]
#     print(cost)
    

    
#Test 1
n = 5
grid = list(map(int, "31 100 65 12 18 10 13 47 157 6 100 113 174 11 33 88 124 41 20 140 99 32 111 41 20".split()))
matr = get_matrix(grid, n)
graph = convert_matrix_to_adj_list(n, matr)
source = 0
cost = dijkstra(source, graph) + matr[0][0]
print(cost)    

# Test 2
n = 2
grid = list(map(int, "42 93 7 14".split()))
matr = get_matrix(grid, n)
graph = convert_matrix_to_adj_list(n, matr)
source = 0
cost = dijkstra(source, graph) + matr[0][0]
print(cost)    

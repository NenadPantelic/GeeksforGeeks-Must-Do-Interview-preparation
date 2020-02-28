#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:12:38 2020

@author: nenad
"""


def path_exists(g, source, n):
    visited = [False] * (n*n)
    q = [(source, 1)]
    visited[source] = True
    while len(q):
        position, value = q.pop(0)
        if value == 2:
            return 1
        visited[position] = True
        for n_pos, n_val in g[position]:
            if visited[n_pos]:
                continue
            visited[n_pos] = True
            if n_val != 0:
                q.append((n_pos, n_val))
            
    return 0

from collections import defaultdict
source = None
def get_matrix(grid, n):
    global source
    matr = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            value = i * n + j
            matr[i][j] = grid[value]
            if grid[value] == 1:
                source = value
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

t = int(input())
for i in range(t):
    n = int(input())
    grid = list(map(int, input().split()))
    matr = get_matrix(grid, n)
    graph = convert_matrix_to_adj_list(n, matr)
    #source = 0
    print(path_exists(graph, source, n))
    #print(cost)
    

# Test 1
# n = 4
# grid = list(map(int, "3 0 0 0 0 3 3 0 0 1 0 3 0 2 3 3".split()))
# matr = get_matrix(grid, n)
# graph = convert_matrix_to_adj_list(n, matr)
# #print(graph)
# print(source)
# print(path_exists(graph, source, n))

#d = defaultdict(None, {0: [(4, 0), (1, 0)], 1: [(0, 3), (5, 3), (2, 0)], 2: [(1, 0), (6, 3), (3, 0)], 3: [(2, 0), (7, 0)], 4: [(0, 3), (8, 0), (5, 3)], 5: [(1, 0), (4, 0), (9, 1), (6, 3)], 6: [(2, 0), (5, 3), (10, 0), (7, 0)], 7: [(3, 0), (6, 3), (11, 3)], 8: [(4, 0), (12, 0), (9, 1)], 9: [(5, 3), (8, 0), (13, 2), (10, 0)], 10: [(6, 3), (9, 1), (14, 3), (11, 3)], 11: [(7, 0), (10, 0), (15, 3)], 12: [(8, 0), (13, 2)], 13: [(9, 1), (12, 0), (14, 3)], 14: [(10, 0), (13, 2), (15, 3)], 15: [(11, 3), (14, 3)]})
#print(d)
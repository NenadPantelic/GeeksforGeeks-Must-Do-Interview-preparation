#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:35:44 2020

@author: nenad
"""


def boolean_matrix_problem(matr):
    m = len(matr)
    n = len(matr[0])
    # rows for one-row
    rows = set()
    # cols for one-col
    cols = set()
    for i in range(m):
        for j in range(n):
            if matr[i][j] == 1:
                rows.add(i)
                cols.add(j)
                
    for row in rows:
        for j in range(n):
            matr[row][j] = 1
    for col in cols:
            for i in range(m):
                matr[i][col] = 1
                
    #return matr



# Test 1
matr = [[0,0, 0], [0, 0, 1]]
boolean_matrix_problem(matr)

def print_matr(matr, m, n):
    for i in range(m):
        for j in range(n):
            print(matr[i][j], end=" ")
        print()

#print_matr(matr, 2, 3)


t = int(input())
for i in range(t):
    m,n = map(int, input().split())
    matr = []
    for i in range(m):
        matr.append(list(map(int, input().split())))
    boolean_matrix_problem(matr)
    print_matr(matr, m, n)

                
                
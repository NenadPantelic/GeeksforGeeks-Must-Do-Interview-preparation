#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:44:51 2020

@author: nenad
"""

# if some move is safe
def isSafe(x, y, arr, visited, n):
    # if position is in bounds of the maze and field is safe to pass and it is not previously visited
    return x >= 0 and x < n and y >= 0 and y < n and arr[x][y] == 1 and visited[x][y] == 0
        

def findPath(arr, n):
    paths = []
    visited = [[False for i in range(n)] for j in range(n)]
    solveTheMaze(arr, n, visited, paths)
    return " ".join(paths)
    #for path in paths:
    #    print(path, end=" ")
    #print()
    
    
    
def solveTheMaze(arr, n, visited, paths, x=0, y=0, path=""):
    # if we reached the final position
    if x == n-1 and y == n-1:
        paths.append(path)
        return 
    
    
    if isSafe(x,y,arr, visited, n):
        # to disable getting back to already visited position
        visited[x][y] = 1
        # go down
        solveTheMaze(arr, n, visited, paths, x+1, y, path+"D")
        # go left
        solveTheMaze(arr, n, visited, paths,x, y-1, path+"L")
        # go right
        solveTheMaze(arr, n, visited, paths,x, y+1, path+"R")
        # go up
        solveTheMaze(arr, n, visited, paths,x-1, y, path+"U")
      
        # else backtrack; previous move does not lead to solution, enable reuse of this position
        visited[x][y] = 0
        return
    
    # else position is not safe - doesn't lead to solution
 
# Test 1       
arr = [[1,0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [0, 1, 1, 1]]
n = 4
print(findPath(arr, n))

# Test 2
arr = [[1,0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
n = 4
print(findPath(arr, n))
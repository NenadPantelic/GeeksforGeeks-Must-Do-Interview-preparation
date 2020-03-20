#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:32:30 2020

@author: nenad
"""


def remove_adj_duplicates(string, curr_ind, last_visited, chars):
    if len(s) == 1:
        return string[0]
    if curr_ind == len(string):
        return "".join(chars)
    if len(chars) == 0 or string[curr_ind] != last_visited:
        chars.append(string[curr_ind])
        last_visited = string[curr_ind]
   else:
       last_visited = chars[-1]
    
    # if curr_ind == len(string):
    #     return "".join(chars)
    # if curr_ind == 0:
    #     if string[curr_ind] != string[curr_ind+1]:
    #         chars.append(string[curr_ind])
        
    # elif curr_ind == len(string)-1:
    #   if string[curr_ind] != string[curr_ind-1]:
    #       chars.append(string[curr_ind]) 
    # else:
    #     if string[curr_ind-1] != string[curr_ind] and string[curr_ind] != string[curr_ind+1]:
    #       chars.append(string[curr_ind]) 
        
    return remove_adj_duplicates(string, curr_ind+1, chars)
        

# t = int(input())
# for i in range(t):
#     s = input()
#     print(remove_adj_duplicates(s, 0, [] ))


# Test 1
s = "geeksforgeeks"
print(remove_adj_duplicates(s, 0, [] ))

# Test 2
s = "acaaabbbacdddd"
print(remove_adj_duplicates(s, 0, [] ))
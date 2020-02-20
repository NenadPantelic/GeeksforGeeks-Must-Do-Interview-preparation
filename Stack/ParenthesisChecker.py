#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:15:10 2020

@author: nenad
"""

#from collections import deque
def parenthesis_checker(expr):
    stack = []
    mapping = {'(':')', '{':'}', '[':']'}
    for char in expr:
        if char in '([{':
            # push to stack opening bracket
            stack.append(char)
        else:
            # stack is empty and we have an enclosing bracket
            # if there is not any opening bracket in stack and we current char is enclosing bracket
            if len(stack) == 0:
                return False
            else:
                # if there is not match between opening and enclosing bracket
                last_el = stack.pop(-1)
                if mapping[last_el] != char:
                    return False
    # if there are still opening brackets in stack that do not have their enclosing match
    if len(stack) > 0:
        return False
    return True
    
t = int(input())
for _ in range(t):
    par_expr = input()
    output = parenthesis_checker(par_expr)
    print ('balanced' if output else 'not balanced')

# # Test 1
# expr = '([]'
# print(parenthesis_checker(expr))

# # Test 2
# expr = '()'
# print(parenthesis_checker(expr))


# # Test 3
# expr = '{([])}'
# print(parenthesis_checker(expr))

        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:56:22 2020

@author: nenad
"""


def activity_selection(arr:list):
    # sort by their ending time
    arr.sort(key=lambda x:x[1])
    # counter of activities
    counter = 0
    last_meeting_end_time = 0
    for meeting in arr:
        # first meeting
        if counter == 0:
            counter += 1
            last_meeting_end_time = meeting[1]
        else:
            # meeting overlap - last edning time is greater than current meeting start time
            if last_meeting_end_time > meeting[0]:
                continue
            else:
                # update last meeting end time and increment the meeting counter
                last_meeting_end_time = meeting[1]
                counter += 1
    return counter
            
    
# Test 1    
a = list(map(int, "1 3 2 5 8 5".split()))
b = list(map(int,"2 4 6 7 9 9".split()))

arr = list(zip(a,b))
print(activity_selection(arr))


# Test2
a = list(map(int, "1 3 2 5".split()))
b = list(map(int,"2 4 3 6".split()))

arr = list(zip(a,b))
print(activity_selection(arr))

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int,input().split()))
    arr = list(zip(a,b))
    print(activity_selection(arr))
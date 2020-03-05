#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:28:19 2020

@author: nenad
"""


def n_meetings(arr:list):
    # index map - stores original order of the meetings
    ind_map = {value:index+1 for index,value in dict(enumerate(arr)).items()}
    # sort by their ending time
    arr.sort(key=lambda x:x[1])
    
    
    # meetings
    meetings = []
    
    last_meeting_end_time = 0
    for i in range(len(arr)):
        # first meeting
        if last_meeting_end_time == 0:
            meetings.append(ind_map[arr[i]])
            last_meeting_end_time = arr[i][1]
        else:
            # meeting overlap
            if last_meeting_end_time > arr[i][0]:
                continue
            else:
                # update last meeting end time and add the meeting 
                last_meeting_end_time = arr[i][1]
                meetings.append(ind_map[arr[i]])
    return meetings
            
    
# Test 1    
a = list(map(int, "1 3 2 5 8 5".split()))
b = list(map(int,"2 4 6 7 9 9".split()))

arr = list(zip(a,b))
meetings = n_meetings(arr)
for meeting in meetings:
    print(meeting, end=" ")
print()


# # Test2
a = list(map(int, "75250 50074 43659 8931 11273 27545 50879 77924".split()))
b = list(map(int,"112960 114515 81825 93424 54316 35533 73383 160252  ".split()))
arr = list(zip(a,b))
meetings = n_meetings(arr)

def print_meetings(meetings):
    for meeting in meetings:
        print(meeting, end=" ")
    print()


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int,input().split()))
    arr = list(zip(a,b))
    meetings = n_meetings(arr)
    print_meetings(meetings)

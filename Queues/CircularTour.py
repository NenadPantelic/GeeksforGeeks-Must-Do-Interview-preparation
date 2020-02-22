#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:15:17 2020

@author: nenad
"""


def circular_tour(petrol, distances):
    # index of start gas station
    start = 0
    # petrol amount
    petrol_value = 0
    # deficit in petrol
    deficit = 0
    for i in range(len(petrol)):
        petrol_value += petrol[i] - distances[i]
        # cannot reach some mid-station
        if petrol_value < 0:
            petrol_value = 0
            # move to the next station as start one
            start += 1
            # deficit from previous start point to current gas station where deficit occured
            deficit += petrol_value
    return start if (petrol_value + deficit) >= 0 else -1

petrol = [4, 6, 7, 4] 
distances = [6,5,3,5]

print(circular_tour(petrol, distances))

            
def tour(lis, n):
    # index of start gas station
    start = 0
    # petrol amount
    petrol_value = 0
    # deficit in petrol
    deficit = 0
    for i in range(len(lis)):
        petrol_value += lis[i][0] - lis[i][1]
        # cannot reach some mid-station
        if petrol_value < 0:
            petrol_value = 0
            # move to the next station as start one
            start = i + 1
            # deficit from previous start point to current gas station where deficit occured
            deficit += petrol_value
    return start if (petrol_value + deficit) >= 0 else -1

data = list(zip(petrol, distances))
print(tour(data, 4))
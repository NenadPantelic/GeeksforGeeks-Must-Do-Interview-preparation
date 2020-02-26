#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:19:12 2020

@author: nenad
"""

def is_valid(ip, pos,segments):
    len_flag = True
    # ip is not valid in form 0x e.g 121.03.22.234
    if len(ip) > 1 and ip[0] == "0":
        len_flag = False
    # check ip length, value and if ip's part is already checked 
    return len_flag and len(ip) > 0 and 0 <= int(ip) <= 255 and segments[pos] == False

def genIP(string):
    ips = []
    n = len(string)
    segments = [False] * n
    solve(string, n, 0, ips, segments, [])
    print(ips)
    
def solve(string, n, pos, ips,segments, ip):
    # ip has 4 parts
    if len(ip) == 4:
        # if we raached end of the string that we process
        if pos>=n:
            ips.append(".".join(ip))
        return 
    # one part of ip has length from 1 to 3, both inclusive
    for i in range(1,min(4, n-pos+1)):
        # take substring as ip's quartette
        substr = string[pos:pos+i]
        # if ip is valid
        if is_valid(substr, pos,segments):
            # mark that char as used
            segments[pos] = True
            # check the rest of the string - can we form the rest of ip from that substring
            solve(string, n, pos+i, ips, segments, ip + [substr])
            # backtrack if we can't do that
            segments[pos] = False
    return

   

# Test 0
string = "1111"
genIP(string)
            
# Test 1            
string = "11211"
genIP(string)

# Test 2
string = "112112"
genIP(string)

# Test 3
string = "25500255"
genIP(string)


    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 22:29:38 2018

@author: thejumpingspider
"""
fifthPowersList = []
for i in range (10, 355000):
    total = 0
    j = str(i)
    for k in j:
        total += (int(k)**5)
    if total == i:
        fifthPowersList.append(i)
print (sum(fifthPowersList))
        
        
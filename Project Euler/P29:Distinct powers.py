#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 12:02:58 2019

@author: thejumpingspider
"""
import math
powers = []
final_powers = []
for i in range (2,101):
    for j in range (2,101):
        powers.append(math.pow(i,j))
powers.sort()
for k in powers:
    if k not in final_powers:
        final_powers.append(k)
print (len(final_powers))
        

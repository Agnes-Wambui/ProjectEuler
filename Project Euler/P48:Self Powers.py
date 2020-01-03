#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 22:12:50 2018

@author: thejumpingspider
"""

total = 0
for i in range (1,1001):
    total += (i**i)
totalString = str(total)
totalStringLen = len(totalString)

print (totalString[totalStringLen-10 : totalStringLen])
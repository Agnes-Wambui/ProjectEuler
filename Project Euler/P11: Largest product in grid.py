#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 14:57:16 2018

@author: thejumpingspider
"""

grid = open ('largest product in grid.txt', 'r')
gridLines = grid.read();
gridList = gridLines.split(" ")
grid =[]
for i in gridList:
    j = i.rstrip()
    grid.append(j)

print (grid)

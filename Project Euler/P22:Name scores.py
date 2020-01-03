#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:01:27 2018

@author: thejumpingspider
"""

namesFile = open("p022_names.txt", "r")
names = namesFile.read()
namesList = names.split(",")
sortedNamesList = sorted(namesList)
alphaPos = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
            'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,
            'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, '"':0}
total = 0
noOfNames = 1
for name in sortedNamesList:
    nameScore = 0;
    for char in name:
        nameScore += alphaPos[char]
    total += (nameScore * noOfNames)
    noOfNames += 1
print (total, noOfNames)

    
            
            
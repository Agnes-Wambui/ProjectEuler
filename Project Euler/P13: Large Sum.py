#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 23:02:33 2018

@author: thejumpingspider
"""

numbersFile = open('large sum.txt','r')
numbers = numbersFile.read()
numbersList = numbers.split()

total = 0
for num in numbersList:
    num = num.replace('\ufeff','')
    total += int(num)

print (total)


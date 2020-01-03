#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 18:05:11 2018

@author: thejumpingspider
"""

numbersFile = open ('1-1000 in words','r')
numbers = numbersFile.read()
numbersList = numbers.split(",")
wordCount = 0
for num in numbersList:
    num = num.replace('-','').replace(' ','').replace('\n','')
    wordCount += len(num)
print (wordCount)


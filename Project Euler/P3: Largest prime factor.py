#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 22:04:11 2018

@author: thejumpingspider
"""
import math
num = 13195

factors = []
while num > 1:
    sqrtNum =int(math.sqrt(num))
    for i in range (2, sqrtNum):
        if num%i == 0:
            num = num/i
            factors.append(i)
print (factors)
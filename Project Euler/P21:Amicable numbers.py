#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:12:19 2018

@author: thejumpingspider
"""
amicableNums = []
amicableNums1 = []
for i in range (4,10001):
    factors1 = [j for j in range (1,i) if i%j == 0]
    sumFactors1 = sum(factors1)
    factors2 = [k for k in range (1,sumFactors1) if sumFactors1%k == 0]
    sumFactors2 = sum(factors2)
    if i != sumFactors1 and sumFactors2 == i:
        amicableNums.append(i)
        amicableNums.append(sumFactors1)
for l in amicableNums:
    if l not in amicableNums1:
        amicableNums1.append(l)
    
print (sum(amicableNums1))
    
    
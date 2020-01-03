#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 15:33:58 2018

@author: thejumpingspider
"""
from functools import reduce
a = 10
b = 55
noOfFactors = 0
total = 0
while noOfFactors <= 500:
    a += 1
    b = b + a    
    factors = reduce(list.__add__,([i, b//i] for i in range (1, int(b**0.5) + 1) if b%i == 0))
    noOfFactors = len(factors)
print (b)    
    
    
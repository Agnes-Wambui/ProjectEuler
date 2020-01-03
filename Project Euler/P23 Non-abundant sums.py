#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 18:44:04 2019

@author: thejumpingspider
"""
from functools import reduce

abundant_numbers = []
nonabundant_sums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
for b in range (12, 28123):
     factors = reduce(list.__add__,([i, b//i] for i in range (1, int(b**0.5) + 1) if b%i == 0))
     factors.remove(b)    
     sum_of_factors = sum(factors)
     if sum_of_factors > b:
         abundant_numbers.append(b)
for c in range (24,28123):
    abnum = abundant_numbers[0:]
    boolean = all([a for a in abnum if (c-a) in abnum])          
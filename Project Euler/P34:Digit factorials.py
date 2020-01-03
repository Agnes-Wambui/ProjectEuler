#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:46:51 2019

@author: thejumpingspider
"""
import math

digit_factorials = 0
for i in range (3,50000):
    i_to_string = str(i)
    string_to_list = list(i_to_string)
    fact_sum = 0
    for j in string_to_list:
        fact_sum += math.factorial(int(j))
    if fact_sum == i:
        digit_factorials += i
print (digit_factorials)
        
        
        
        
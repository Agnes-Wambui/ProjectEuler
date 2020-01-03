#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:14:45 2018

@author: thejumpingspider
"""
maximum_length = 0

for i in range (10,1000000):
    j = i
    collatz_sequence = []
    while j > 1:        
        collatz_sequence.append(j)
        if j%2 == 0:
            j = j/2
            collatz_sequence.append(j)
        else:
            j = 3*j+1
            collatz_sequence.append(j)
    length_of_sequence = len(collatz_sequence)
    if length_of_sequence > maximum_length:
        maximum_length = length_of_sequence
        maximum_dict = {}
        maximum_dict[i] = maximum_length
print (maximum_dict)
        
        
        
            
        
    
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 21:23:20 2018

@author: thejumpingspider
"""

noOfDigits = 0
a = 1
b = 1
n = 1
while noOfDigits <1000: 
    temp = a
    a = b
    b =  temp + b
    noOfDigits = len(str(a))
    n +=1
    
print (a, n)  
    
    
   
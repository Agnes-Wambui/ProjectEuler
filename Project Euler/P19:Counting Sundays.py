#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 18:03:01 2019

@author: thejumpingspider
"""

year = 1900
sunday = 7
first_day_sunday = 0
while year <= 2000:
    while sunday <= 31:
        sunday += 7
        if sunday == 1:
            first_day_sunday += 1
    
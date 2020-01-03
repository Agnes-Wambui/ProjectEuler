#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 21:01:46 2018

@author: thejumpingspider
"""

import itertools
permsList = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
sortedPermsList = sorted(permsList)
print (sortedPermsList[999999])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 12:07:48 2018

@author: thejumpingspider
"""

class Darasa (object):
    def __init__ (self):
        self.darasa = []
    
    def addClassMember(self,name):
        '''
    adds a new  member into the Darasa. 
    This method does not allow for duplicate Darasa members. If this member exists, handle it 
    as you please. 
    arguements: String name 
    returns: Darasa member added or something else if member exists 
    '''  
    if name in self.darasa:
        raise ValueError ('Duplicate member')        
    else:
        self.darasa.append(name)

        
    def removeClassMember(self, name):
        '''
        removes member from this Darasa. 
        If member does not exist in the Darasa, handle it as you please. 
        Arguements: String name
        returns: Darasa member removed from class or something else if member does not exist
        '''
        try:
            self.darasa.remove(name)
            return name
        except:
            raise ValueError (name, 'not found')
        
    def getDarasaMembers(self):
        '''
        returns the members of this class
        '''
        return self.darasa

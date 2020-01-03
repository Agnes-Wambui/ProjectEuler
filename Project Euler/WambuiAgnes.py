#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 12:44:27 2018

@author: thejumpingspider
"""

class Darasa (object):
    def __init__(self):
        """ create an empty class"""
        self.darasa = []
        
    def addClassMember (self,name):
        """Add members to the class. Return a student of the class."""
        if name not in self.darasa:
            self.darasa.append(name)
            return name
        else:
            raise ValueError ('Duplicate Member')
        
    def removeClassMember (self,name):
        """Remove a student from the class. Return the removed student."""
        try:
            self.darasa.remove(name)
            return name
        except:
            raise ValueError (name, 'not found')
            
    def getDarasaMembers (self):
        """Return the students in the class"""
        return self.darasa
    
standard1 = Darasa()
print(standard1.addClassMember('Richard Hendricks'))
standard2 = Darasa() 
print(standard2.addClassMember('Dinesh '))
standard3 = Darasa()  
print(standard3.addClassMember('Jared Dunn'))
    
class Shule (object):
    """create an empty school called shuleName"""
    def __init__ (self, shuleName):
        self.shuleName = shuleName
        self.shule = {}
        
    def addDarasa (self,name,darasa):
        """Add a class called name to the school. Return the school.  """
        if name not in self.shule:
            self.shule[name] = darasa.getDarasaMembers()
            return self.shule
        else:
            raise ValueError ('Duplicate Class')        
    
    def removeDarasa (self,name):
        """Remove a class from the school. Return the school"""
        try:
            del(self.shule[name])
            return (self.shuleName, self.shule)
        except:
            raise ValueError (name, 'not found')
    def getShule (self):
        """Return the school"""
        return self.shule
            
shule1 = Shule('JKUAT')
print(shule1.addDarasa('CS',standard1))
print(shule1.addDarasa('Math',standard2)) 
print(shule1.addDarasa('Bio',standard3))         
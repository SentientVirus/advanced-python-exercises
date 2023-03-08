#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:19:21 2023

@author: marmo435
"""

class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']
    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
            print('\t%s ' % member)
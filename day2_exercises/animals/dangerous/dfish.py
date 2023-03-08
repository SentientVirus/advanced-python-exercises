#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:06:32 2023

@author: marmo435
"""

class Fish:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Puffer Fish', 'Great White Shark', 'Electric Eel']
    def printMembers(self):
        print('Printing members of the dangerous fish class')
        for member in self.members:
            print('\t%s ' % member)
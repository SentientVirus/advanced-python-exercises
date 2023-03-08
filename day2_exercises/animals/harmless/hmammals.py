#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:06:32 2023

@author: marmo435
"""

class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Rabbit', 'Red Panda', 'Manatee']
    def printMembers(self):
        print('Printing members of the harmless mammals class')
        for member in self.members:
            print('\t%s ' % member)
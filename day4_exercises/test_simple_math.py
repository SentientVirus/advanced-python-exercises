#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:37:12 2023

@author: marmo435
"""

import simple_math as sm

def test_simple_add():
    assert sm.simple_add(6, 3) == 9
    
def test_simple_sub():
    assert sm.simple_sub(6, 3) == 3
    
def test_simple_mult():
    assert sm.simple_mult(6, 3) == 18
    
def test_simple_div():
    assert sm.simple_div(6, 3) == 2
    
def test_poly_first():
    assert sm.poly_first(3, 6, 2) == 12
    
def test_poly_second():
    assert sm.poly_second(3, 6, 2, 2) == 30
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:29:05 2023

@author: marmo435
"""

from classroom import Person, Student, Teacher

me = Person("Marina", "Mota")
me.printFullName()

        
me2 = Student("Marina", "Mota", "biology")
me2.printNameSubject()

        
me3 = Teacher("Marina", "Mota", "Genome Analysis")
me3.printNameCourse()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:29:05 2023

@author: marmo435
"""

class Person:
    def __init__(self, first_name, last_name):
        ''' Constructor for this class. '''
        # Assign values to object
        self.first_name = first_name
        self.last_name = last_name
    def printFullName(self):
        print(f'{self.first_name} {self.last_name}')

class Student(Person):
    def __init__(self, first_name, last_name, subject):
        Person.__init__(self, first_name, last_name)
        #super(Student, self).__init__(first_name, last_name)
        self.subject = subject
    def printNameSubject(self):
        print(f'{self.first_name} {self.last_name}, {self.subject}')

class Teacher(Person):
    def __init__(self, first_name, last_name, course):
        Person.__init__(self, first_name, last_name)
        #super(Student, self).__init__(first_name, last_name)
        self.course = course
    def printNameCourse(self):
        print(f'{self.first_name} {self.last_name} teaches {self.course}')
        
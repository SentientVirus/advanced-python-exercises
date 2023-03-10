#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:43:54 2023

@author: marmo435
"""
import numpy as np
import scipy.linalg as la
from numpy import inf
#from scipy.linalg import solve

#a.
A = np.array([[1, -2, 3],
     [4, 5, 6],
     [7, 1, 9]])

print("a.: ", A)

#b.
b = np.arange(1,4)

print("b.: ", b)

#c.
x = np.linalg.solve(A, b)

print("c.: ", x)

#d.
y = la.solve(A, b)

print("d.: ", y)

#e.
B = np.random.rand(3, 3)
xe = np.linalg.solve(A, B)
ye = la.solve(A, B)
print("e.: B:", B)
print("e.: numpy solution: ", xe)
print("e.: scipy solution: ", ye)
print("e.: numpy vs scipy: ", xe == ye)

#f.
f = la.eig(A)
print("f.: eigenvalues: ", f[0])
print("f.: eigenvectors: ", f[1])

#g.
g1 = la.inv(A)
g2 = la.det(A)
print("g.: inverse: ", g1)
print("g.: determinant: ", g2)

#h.
orders = [inf, -inf, 'fro', 'nuc', None]
for i in orders:
    h = la.norm(A, i)
    print(f"h.: order: {i}", h)




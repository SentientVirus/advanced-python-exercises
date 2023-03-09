#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 09:06:07 2023

@author: marmo435
"""

import numpy as np

#a.

a = np.zeros(10)
a[4] = 1
print(f"a.: {a}", end = "\n\n")

#b.
b = np.arange(10, 50)
print(f"b.: {b}", end = "\n\n")

#c.
c = b[::-1]
print(f"c.: {c}", end = "\n\n")

#d.
dv = np.random.rand(3, 3)
dv *= 8
print(f"d.: {dv}", end = "\n\n")

#e.
ev = [1,2,0,0,4,0]
e = np.flatnonzero(ev)
print(f"e.: {e}", end = "\n\n")

#f.
f = np.random.rand(30)
f *= 10 #Random numbers from 0 to 10
f_mean = np.mean(f)
print(f"f.: {f_mean}", end = "\n\n")

#g.
g0 = np.zeros((5, 5))
g = np.pad(g0[1:-1,1:-1], pad_width = ((1, 1), (1, 1)), mode = "constant", 
constant_values = 1)
print(f"g.: {g}", end = "\n\n")

#h.
h = np.zeros((8,8), dtype = int)
h[1::2,::2] = 1
h[::2,1::2] = 1
print(f"h.: {h}", end = "\n\n")

#i
i = np.tile(np.array([[0,1],[1,0]]), (4, 4))
print(f"i.: {i}", end = "\n\n")

#j.
j = np.arange(11)
j[3:9] *= -1
print(f"j.: {j}", end = "\n\n")

#k.
k = np.random.random(10)
k = np.sort(k)
print(f"k.: {k}", end = "\n\n")

#l.
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A, B)
if equal == False:
    print("l.: The arrays are different.", end = "\n\n")
else:
    print("l.: The arrays are equal.", end = "\n\n")
    
#m.
m = np.arange(10, dtype = np.int32)
print(f"m.: {m.dtype} changes to...", end = " ")
mv = m.view('float32')
mv[:] = m
print(f"{mv.dtype}", end = "\n\n")

#n.
nA = np.arange(9).reshape(3,3)
nB = nA + 1
nC = np.dot(nA,nB)
nD = np.diagonal(nC)
print(f"n. {nD}", end = "\n\n")
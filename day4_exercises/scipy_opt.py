#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:36:05 2023

@author: marmo435
"""

import numpy as np
import matplotlib.pyplot as plt
#from scipy.optimize import minimize_scalar
from scipy.interpolate import interp1d

exp_data = np.load('I_q_IPA_exp.npy')
model = np.load('I_q_IPA_model.npy')

def scale(x, a, b):
    scaled = a*x
    return scaled - b

exp_data = exp_data[~np.isnan(exp_data[:, 0])]

model_x = interp1d(exp_data[:, 0], exp_data[:, 1], kind = 'nearest')

new_x = np.linspace(min(exp_data[:, 0]), max(exp_data[:, 0]), len(exp_data))
new_y = model_x(new_x)

plt.scatter(exp_data[:, 0], exp_data[:, 1])
plt.scatter(new_x, new_y, alpha = 0.2)
plt.savefig('approximation.png')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:36:05 2023

@author: marmo435
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.interpolate import interp1d
from sklearn.metrics import mean_squared_error

exp_data = np.load('I_q_IPA_exp.npy')
model = np.load('I_q_IPA_model.npy')


exp_data = exp_data[~np.isnan(exp_data[:, 1])]

model_x = interp1d(model[:, 0], model[:, 1])

new_y = model_x(exp_data[:, 0])


new_model = minimize(mean_squared_error, exp_data[:, 1], args = (new_y,))

plt.figure(figsize=(12, 8), dpi=80)
plt.scatter(exp_data[:, 0], exp_data[:, 1])
plt.scatter(exp_data[:, 0], new_model.x/10**4)

plt.savefig('approximation.png')


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:36:05 2023

@author: marmo435
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from scipy.interpolate import interp1d
from sklearn.metrics import mean_squared_error

#Load data
exp_data = np.load('I_q_IPA_exp.npy')
model = np.load('I_q_IPA_model.npy')

#Filter out nans
exp_data = exp_data[~np.isnan(exp_data[:, 1])]

#Make interpolations for both the data and the model
model_int = interp1d(model[:, 0], model[:, 1])
exp_int = interp1d(exp_data[:, 0], exp_data[:, 1])

#Make a new x so that both new y have the same length
new_x = np.linspace(min(exp_data[:, 0]), max(exp_data[:, 0]), 250)

#Calculate new y
new_model_y = model_int(new_x)
new_exp_y = exp_int(new_x)

#Define mse function using in-built mse function
def mse(x):
    return mean_squared_error(new_exp_y, new_model_y*x)

#Minimize scaling factor
scalar = minimize_scalar(mse)

#Plot results
plt.figure(figsize=(12, 8), dpi=80)
plt.scatter(exp_data[:, 0], exp_data[:, 1])
plt.plot(model[:, 0], model[:,1]*scalar.x, "r-")

plt.savefig('approximation.png')


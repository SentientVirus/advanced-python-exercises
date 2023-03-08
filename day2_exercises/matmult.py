# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250

#@profile
def NxN_matrix(N): # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    return X

#@profile
def NxN_1_matrix(N): # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    return Y

#@profile
def result_NxN_1(N): # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    return result

#@profile
def X_Y_iter(X, Y, result): #I would start by optimizing this section
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]


X = NxN_matrix(N)
Y = NxN_1_matrix(N)
result = result_NxN_1(N)
X_Y_iter(X, Y, result)
for r in result:
    print(r)

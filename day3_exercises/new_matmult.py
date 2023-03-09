# Program to multiply two matrices using nested loops
import numpy as np

N = 250

@profile
def NxN_matrix(N): # NxN matrix
    X = np.random.randint(0, 100, size = (N, N))
    return X

@profile
def NxN_1_matrix(N): # Nx(N+1) matrix
    Y = np.random.randint(0, 100, size = (N, N+1))
    return Y

@profile
def result_NxN_1(N): # result is Nx(N+1)
    result = np.zeros(shape = (N, N+1), dtype = int)
    return result

@profile
def X_Y_iter(X, Y, result):
    result += np.matmul(X, Y)


X = NxN_matrix(N)
Y = NxN_1_matrix(N)
result = result_NxN_1(N)
X_Y_iter(X, Y, result)
[print(r) for r in result]

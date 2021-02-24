# ejemplo de clase -------------------------------------------------------------------------------------
import numpy as np
def linear_cost(X, y, theta):
    '''
        X: (m, n) np.array
        y: (m, n) np.array
        theta: (n, 1) np.array
    '''
    h = X @ theta
    return ((h - y) ** 2).sum() / (2*len(X))

# print(linear_cost(np.array([[1, 2], [1, 2]]), np.array([[1, 2], [1, 2]]), np.array([[2], [2]])))

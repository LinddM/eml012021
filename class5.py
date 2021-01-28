import numpy as np
X = np.array([
    [1, 2],
    [3, 4]
])

# join horizontal: hstack
X = np.hstack((
    np.ones(2).reshape(2, 1),
    X
))
# join vertical: vstack

Theta = np.array([
    [5],
    [6],
    [7]
])

print(X @ Theta)
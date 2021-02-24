# from matplotlib import pyplot as plt
import numpy as np

def linear_cost(X, y, theta):
    h = X @ theta
    return ((h - y) ** 2).sum() / (2*len(X))

def linear_cost_gradient(X, y, theta):
    h = X @ theta
    return ((h - y).T @ X).T / (2*len(X))

def gradient_descent(
    X, y, theta_0, 
    cost_function, cost_function_gradient,
    learning_rate=0.01, 
    threshold=0.001,
    max_iter=1000
):
    theta = theta_0
    iteration = 0
    costs = []

    while np.linalg.norm(cost_function_gradient(X, y, theta)) > threshold and iteration < max_iter:
        iteration += 1
        theta -= learning_rate * cost_function_gradient(X, y, theta)
        costs.append(cost_function(X, y, theta))

    return theta, costs

## example
TRAINING_SET_SIZE = 200
x = np.linspace(-10, 30, TRAINING_SET_SIZE)
print(x.shape)
# matriz de entrada
X = np.vstack(
    (
        np.ones(TRAINING_SET_SIZE),
        x
    )
).T

y = (5 + 2 * x + np.random.randint(-15, 15, TRAINING_SET_SIZE)).reshape(TRAINING_SET_SIZE, 1) # producir y's medio aleatorios

m, n = X.shape
theta_0 = np.random.rand(n, 1)

r_theta, costs = gradient_descent(
    X, y, theta_0,
    linear_cost,
    linear_cost_gradient,
    learning_rate=0.0001,
    threshold=1.5
)

print("theta ", r_theta)
# print("costs ", costs)

# # plt.scatter(X[:,1], y)
# plt.plot(costs)
# plt.show()
# libraries ----------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# data ---------------------------
df = pd.read_csv('satgpa.csv')

# equations ----------------------
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
    history = []
    while np.linalg.norm(cost_function_gradient(X, y, theta)) > threshold and iteration < max_iter:
        iteration += 1
        theta -= learning_rate * cost_function_gradient(X, y, theta)
        history.append(theta - learning_rate * cost_function_gradient(X, y, theta))

    return theta, history

# methods ------------------------
x = df.copy()
y = np.array(df['fy_gpa']).reshape(1000, 1)
del x['sat_sum']
del x['fy_gpa']

X = np.hstack(
    (
        np.ones(1000).reshape(1000, 1), # para el intercepto
        x
    )
)

m, n = X.shape
theta_0 = np.random.rand(n, 1)

r_theta, history = gradient_descent(
    X, y, theta_0,
    linear_cost,
    linear_cost_gradient,
    learning_rate=0.0001,
    threshold=1.5
)

plt.scatter(X[:,3], y)
plt.plot(X[:,3], X @ history[math.floor(len(history)*0.05)], color='red')
plt.show()

plt.scatter(X[:,3], y)
plt.plot(X[:,3], X @ history[math.floor(len(history)*0.3)], color='red')
plt.show()

plt.scatter(X[:,3], y)
plt.plot(X[:,3], X @ history[math.floor(len(history)*0.8)], color='red')
plt.show()

plt.scatter(X[:,3], y)
plt.plot(X[:,3], X @ r_theta, color='green')
plt.show()
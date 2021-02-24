# libraries ----------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
    costs = []
    while np.linalg.norm(cost_function_gradient(X, y, theta)) > threshold and iteration < max_iter:
        iteration += 1
        theta -= learning_rate * cost_function_gradient(X, y, theta)
        costs.append(cost_function(X, y, theta))

    return theta, costs

# methods ------------------------
x = df.copy()
y = np.array(df['fy_gpa']).reshape(1000, 1)
del x['sat_sum']
del x['fy_gpa']
print(x.head())

X = np.hstack(
    (
        np.ones(1000).reshape(1000, 1), # para el intercepto
        x
    )
)

m, n = X.shape
theta_0 = np.random.rand(n, 1)

print('Forma de X', X.shape)
print('Forma de Y', y.shape)
print('Forma de matriz de thetas', theta_0.shape)

r_theta, costs = gradient_descent(
    X, y, theta_0,
    linear_cost,
    linear_cost_gradient,
    learning_rate=0.0001,
    threshold=1.5
)

# print("Thetas\n", r_theta)

# plt.scatter(X[:,1], y)
# plt.plot(X[:,1], X @ r_theta, color='red')
# plt.show()

# ans ----------------------------
print('\nIntercept: ', r_theta[0])
print('Sex coef: ', r_theta[1])
print('SAT_v coef: ', r_theta[2])
print('SAT_m coef: ', r_theta[3])
print('HS_gpa coef: ', r_theta[4])

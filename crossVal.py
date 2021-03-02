import numpy as np
import matplotlib.pyplot as plt
import math

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
    thetas = []

    while np.linalg.norm(cost_function_gradient(X, y, theta)) > threshold and iteration < max_iter:
        iteration += 1
        theta -= learning_rate * cost_function_gradient(X, y, theta)
        costs.append(theta-learning_rate * cost_function_gradient(X, y, theta))
        thetas.append(theta.copy())

    return theta, costs, thetas

## example
TRAINING_SET_SIZE = 200
x = np.linspace(-10, 30, TRAINING_SET_SIZE)
print(x.shape)
# matriz de entrada
X = np.vstack(
    (
        np.ones(TRAINING_SET_SIZE),
        x,
        x ** 2 # agregar nueva caracteristica para probar otro grado en la prediccion
    )
).T

# la nube de puntos tiene naturalmente una forma parabolica al poner la x al cuadrado
y = (5 + 2 * x ** 2 + np.random.randint(-200, 200, TRAINING_SET_SIZE)).reshape(TRAINING_SET_SIZE, 1) # producir y's medio aleatorios

# plt.scatter(X[:, 1], y)
# plt.show()

m, n = X.shape # n va a ser 3 porque tengo mas columnas
theta_0 = np.random.rand(n, 1)

r_theta, costs, thetas = gradient_descent(
    X, y, theta_0,
    linear_cost,
    linear_cost_gradient,
    learning_rate=0.0000001,
    threshold=0.001
)

for test_theta in thetas:
    plt.scatter(X[:,1], y)
    plt.plot(X[:,1], X @ test_theta, color='green')
    plt.show()
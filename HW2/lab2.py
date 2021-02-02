import numpy as np

# problema 1 -------------------------------------------------------------

M = np.array([
    [1, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1]
])

M1 = np.array([
    [1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1]
])

M2 = np.array([
    [1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
])

check = lambda mat : print(f'La matriz \n{mat}'
                           f'\nEs reflexiva: {np.all(np.diagonal(mat))}'
                           f'\nEs simétrica: {np.allclose(mat, mat.T)} '
                           f'\nEs transitiva: {np.allclose(mat, np.where(mat@mat>1, 1, mat@mat))}')

check(M)
check(M1)
check(M2)

# problema 2 -------------------------------------------------------------

A = np.arange(5, 9).reshape(2, 2)
print(A)

B = np.arange(-7, -1).reshape(2, 3)
print(B)

C = np.arange(4, 14, 3).reshape(2, 2)
print(C)

D = np.eye(2)
print(D)

E = np.zeros(6).reshape(2, 3)
print(E)

H = np.vstack((np.hstack((A, np.hstack((np.eye(2), np.zeros(6).reshape(2, 3))))), np.hstack((np.eye(2), np.hstack((C, B))))))
print(H)

# problema 3 -------------------------------------------------------------

A = np.arange(0, 24).reshape(4, 6)

# en contra del reloj

rota90 = lambda mat: np.rot90(mat)
print(rota90(A))

rota180 = lambda mat: np.rot90(mat, 2)
print(rota180(A))

rota270 = lambda mat: np.rot90(mat, 3)
print(rota270(A))

# a favor del reloj

rota90_otro_lado = lambda mat: np.rot90(mat, 1, (1, 0))
print(rota90_otro_lado(A))

rota180_otro_lado = lambda mat: np.rot90(mat, 2, (1, 0))
print(rota180_otro_lado(A))

rota270_otro_lado = lambda mat: np.rot90(mat, 3, (1, 0))
print(rota270_otro_lado(A))

# problema 4 -------------------------------------------------------------

variables = np.array([
#    x  a  y  b  z  c  t  d
    [2, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [-1, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, -1, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, -1, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, -1, 2]
])

constantes = np.array([4, 3, 3, 3, 2, 1, 6, 4, 2, -3, -1, 4]).reshape(12, 1) # constante

ans = np.hstack((
    np.array([
        ['x'],
        ['a'],
        ['y'],
        ['b'],
        ['z'],
        ['c'],
        ['t'],
        ['d']
    ]),
    (np.linalg.lstsq(variables, constantes, rcond=None)[0])
))

print(f'Solución del sistema de ecuaciones: \n{ans}')
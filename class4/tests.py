# una tupla es inmutable (no le puedo cambiar el valor)
# shape es una tupla que me dicta dimensiones de cada eje

import numpy as np

print(type(np.arange(10, 20, 2)))

# my_array = np.array(
#     [
#         [1, 5, -2],
#         [6, 0, 2]
#     ]
# )

my_array = np.zeros((10, 10, 2)).reshape((25, 8)) # si no son compatibles las dimensiones solo no lo convierte

my_array = np.arange(200).reshape((25, 8)) % 2 == 0 # expresión booleana con un array con los resultados de la operación


print(type(my_array), my_array, my_array.shape)

# tuplas
def division(numerador, denominador):
    return (numerador // denominador, numerador % denominador) if denominador != 0 else (None, None)

cociente, residuo = division(11, 3)

print(cociente) # 3
print(residuo) # 2

arr = np.linspace(0, 2, 10) < 1

arr = np.full((3, 3), 2)

arr = np.eye(7) # matriz identidad
print(arr)

a = np.array([
    [1, 2, 3],
    [9, 8, 7],
    [6, 4, 5]
])

b = np.eye(3)

print(a @ b) # multiplicación de matrices
print(a.dot(b))

c = np.arange(1, 10).reshape(3, 3)
d = np.arange(10, 13).reshape(3, 1)

print(c)
print(d)
print(c.shape)
print(d.shape)

print(d.T @  c)


# Ejercicio --------------------------------------------------
'''
    n caracteristicas
    k etiquetas

    calcular y: x, theta son dados
'''

'''

    Suposiciones:

        me dan un arreglo con varias theta
        me dan un arreglo con varias x
        debo regresar un arreglo con la solucion y

        filas las indica K
        columnas las indica n

'''

# try 1

def makeArray(k, n, thetaArray, xMatrix):
    '''
        xMatrix tiene k,n-1 dimensiones
        thetaArray tiene 1,n
    '''

    # agregar columna de 1's a xMatrix al principio
    for i in range(k):
        xMatrix[i] = np.insert(xMatrix[i], 0, 1)

    ans = np.zeros((k, 1))

    for i in range(k): # filas
        for j in range(n): # columnas
            ans[i] += thetaArray[j]*xMatrix[i][j]

    return ans

print('Ans ' , makeArray(3, 4, [1, 2, 3, 4], [[5, 6, 7], [1, 6, 7], [5, 6, 7]]))

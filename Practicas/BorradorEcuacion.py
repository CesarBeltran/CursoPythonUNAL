






##Listas y Matrices
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Llenar la matriz del 1 al 9
numero = 1
for fila in range(3):
    for columna in range(3):
        matriz[fila][columna] = numero
        numero += 1
        #print(fila)

# Imprimir la matriz
for fila in matriz:
    print(fila)




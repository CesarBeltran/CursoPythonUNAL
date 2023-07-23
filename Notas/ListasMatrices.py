

#Para hacer referencia a X elemento de la matriz
# matriz[#fila][#columna]
#print(matriz[0][2])

#print("longitud",len(matriz))
'''
############# TEST 2
i=3
j=3
lista =  [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
n=1
for fila in range(i):
	for columna in range(j):
		lista[fila][columna]=n
		n+=1
for fila in lista:	
	print(fila)

print(len(lista))

'''



##Listas y Matrices
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Llenar la matriz del 1 al 9
numero = 1
for fila in range(3):
    for columna in range(3):
        matriz[fila][columna] = numero
        numero *= -1
        #print(fila)

# Imprimir la matriz
for fila in matriz:
    print(fila)










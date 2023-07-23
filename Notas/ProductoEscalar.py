'''
u = [1, 3, 5, 7]
v = [2, 4, 6, 8]

res = [ ]

#La función zip() se utiliza para combinar los elementos de los iterables en pares ordenados.
for i, k in zip (u, v):
	res.append (i * k)

print(res)

'''

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

#a=[int(elemento) for elemento in a.split()]
#b=[int(elemento) for elemento in b.split()]

n=len(a)

for i in range(n):
	print(a[i],b[i])
	suma=suma+a[i]*b[i]
	print(suma)
print(suma)









'''
Para esta actividad deberá escribir un programa de Python que tome como entrada dos secuencias de números y calcule el producto punto de los vectores correspondientes.
u⋅v=(1×4)+(3×2)+(5×0)
u⋅v=4+6+0
u⋅v=10
'''

#u=input()
#v=input()
u='-32 -4 -13 -36 -7'
v='-22 20 37 11 -38'
x=[]

#convertir elementos de una lista 'a' en enteros
u=[int(elemento) for elemento in u.split()]
v=[int(elemento) for elemento in v.split()]

#if Longituda=len(a) == Longitudb=len(b)


for iu,iv in zip(u,v):
	x.append(iu*iv)

print(x)
print(sum(x))
	




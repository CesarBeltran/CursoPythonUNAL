
x0 = 15
v0 = 3.2
a = 0
t = 0


# 2) Convertir cada valor de texto obtenido de la entrada en un valor numérico decimal.
'''
x0 = float(x0)
v0 = float(v0)
a = float(a)
t = float(t)
'''



# 3) Utilizar los valores numéricos en una expresión matemática y obtener el valor de la posición final.


x = x0+v0*t+(a*t**2)/2


# 4) Reportar el resultado de la operación con dos dígitos decimales.

print(x)
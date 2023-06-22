##################################################
#### 💻 Tarea: Ejercicios de física (II)  💻 ####
##################################################

## 👇 Escriba su código DEBAJO de esta línea 👇 ##


# 1) Obtener de la entrada del programa los parámetros iniciales.

'''
x0 = input()
v0 = input()
a = input()
t = input()

# 2) Convertir cada valor de texto obtenido de la entrada en un valor numérico decimal.
x0 = float(x0)
v0 = float(v0)
a = float(a)
t = float(t)
'''

x0 = 47
v0 = 6
a = 5e-2
t = 147

# 3) Realizar las operaciones matemáticas para las conversiones de unidad de medida necesarias.
#     Convertir la velocidad inicial de km/h a m/s

v0=v0/3.6

		
# 4) Utilizar los valores numéricos en las expresiones matemáticas de cada ecuación y obtener el valor de:

#     i. Posición final 
x = x0+v0*t+(a*t**2)/2



#     ii. Velocidad final.  
v = (v0+a*t)
print(f"la velocidad es de {v:.3f} m/s")


# Convertiendo de m/s a km/h
v = v*3.6


# 5) Reportar el resultado de la operación con el formato solicitado.

print(f"La posición final es de {x:.2f} m y la velocidad es de {v:.3f} km/h")
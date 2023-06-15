##################################################
### 💻  Ejemplo: Ejercicios de física (I)  💻 ###
##################################################
'''
Podemos calcular el valor Posicion final (x) a partir de algunos parámetros iniciales que describen el problema. Estos parámetros iniciales son:
La velocidad inicial v0 del objeto en dirección del recorrido.
La posición inicial x0. En este caso el recorrido solo se dará en una dirección de forma horizontal.
La aceleración a que se mantiene constante en todo el recorrido.
El tiempo t o duración del recorrido.

Se conoce que la posición de un objeto uniformemente acelerado puede ser calculada por la siguiente ecuación:
'''

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


x0 = 15
v0 = 3.2
a = 0
t = 0

# 3) Utilizar los valores numéricos en una expresión matemática y obtener el valor de la posición final.


x = x0+v0*t+(a*t**2)/2


# 4) Reportar el resultado de la operación con dos dígitos decimales. :.2    o :.3

print(f"La posición final es {x:.2f} metros.")



## ☝️ Escriba su código ENCIMA de esta línea ☝️ ##
'''
En este ejercicio deberá realizar un programa que defina si un punto dado, con posición horizontal px 
y posición vertical py, se encuentra dentro de un rectángulo (x, y, w, h). 
Los puntos ubicados en el borde, como el punto (0,0) con la primera figura, 
también se considera que están contenidos dentro del rectángulo.

Nota: existen distintas maneras de definir un área rectangular por medio de coordenadas cartesianas. 
No se debe confundir este enfoque con el que define los 4  valores como las coordenadas de dos esquinas
opuestas del rectángulo. En este caso, esta esquina opuesta corresponde a los valores x + w   y   y + h, 
respectivamente.

### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 7-10 líneas de código)
# Entrada del programa (~ 6 líneas).
# Posición y dimensiones del rectángulo.
x = int(input())
y = int(input())
w = int(input())
h = int(input())

# Posición del punto.
px = int(input())
py = int(input())

'''
x = 1
y = 1
w = 2
h = 2

px = 0
py = 1

# Operación booleana y salida del programa (~ 1-4 líneas).


esta_dentro= (px>=x and px<=x+w) and (py>=y and py<=y+h)

print(esta_dentro)


#print((px>=x and px<=w)and(py>=y and py<=h))


n=-1


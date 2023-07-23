## Entrada del valor HX como string

color16='#6e00ff'

###cadena = "ff"
###valor_hexadecimal = int(cadena, 16)


#crear una lista a partir de un objeto iterable (Cadena introducida)
lista=list(color16)
print(lista)

#Se convierte en Hexadecimal la posicion las parejas de valores de la lista
#
r=int((lista[1]+lista[2]),16)
g=int((lista[3]+lista[4]),16)
b=int((lista[5]+lista[6]),16)

#r10=int(r, 10)


print(f" R: {r} G: {g} B: {b}")


### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 5 líneas de código)
# Entrada del programa (~ 1 línea).

#w = float(input())                       # Reemplace 'None' por el código necesario. 
w = 90.98

# Cálculo de la capacidad (~ 3 líneas).
d=0
n=0
while True:
    if w<=d:
        break
    n+=1
    d=2**(n)
    print(f"n={n} d={d}")
    
print(f"La capacidad requerida es de {d} GB.")


# Salida del programa (~ 1 línea).
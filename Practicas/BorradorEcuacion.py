nsec=int(input())
i=int(input())
n=i
min=3
max=15

print(f"¡Bienvenido! Por favor ingrese números entre {min} y {max} para ganar.")
for i in range(i):
    print(f"Intentos restantes: {n-i}.")
    x=int(input())
    
    while max>x>min:
        if x==nsec:
            print("¡Felicidades! El número ingresado es correcto.")
            break
        
        elif (n-i==1) and (x!=nsec):
            print(f"Se acabaron los intentos. El número correcto era {nsec}.")
            break
        elif (x!=nsec) and (i<n):
            
            if x>nsec:
                print("Respuesta incorrecta. El número que ingresó es mayor que el número secreto.")
            elif x<nsec:
                print("Respuesta incorrecta. El número que ingresó es menor que el número secreto.")
            
            
            
            
    print("El número que ingresó no se encuentra en el rango de valores indicado. Intente nuevamente")
        
print("Fin del juego. ¡Gracias por participar!")



### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 24 - 27 líneas de código)

nsec=int(input())
i=int(input())
n=i
min=int(input())
max=int(input())

print(f"¡Bienvenido! Por favor ingrese números entre {min} y {max} para ganar.")

while n<=i:  
    
    print(f"Intentos restantes: {n}.")
    x=int(input())
    
    if x==nsec:
        print("¡Felicidades! El número ingresado es correcto.")
        break
        
    elif (n==1) and (x!=nsec):
        print(f"Se acabaron los intentos. El número correcto era {nsec}.")
        break
    
    elif x<min or x>max:
        print("El número que ingresó no se encuentra en el rango de valores indicado. Intente nuevamente")
        n=n+1
    
    elif (x!=nsec): # and (i<=n):
    
        if x>nsec:
            
            print("Respuesta incorrecta. El número que ingresó es mayor que el número secreto.")
        elif x<nsec:
            
            print("Respuesta incorrecta. El número que ingresó es menor que el número secreto.")
   

    
    n=n-1
            
    
print("Fin del juego. ¡Gracias por participar!")

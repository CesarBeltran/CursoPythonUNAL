nsec=int(input())
i=int(input())
n=i

for i in range(i):
    print(f"Intentos restantes: {n-i}.")
    x=int(input())
    
    if x==nsec:
        print("¡Felicidades! El número ingresado es correcto.")
        break
    
    elif (n-i==1) and (x!=nsec):
        print(f"Se acabaron los intentos. El número correcto era {nsec}.")
        break
    elif (x!=nsec) and (i<n):
        print("Respuesta incorrecta. Intente de nuevo.")
        
print("Fin del juego. ¡Gracias por participar!")



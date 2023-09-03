print("#####################################################")
print("#### Programa: Algoritmo RSA")
print("#### Asignatura: Seguridad en Nuevas Tecnologías")
print("#####################################################")
import math

# Función para calcular el MCD (Máximo Común Divisor)
def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Función para calcular el inverso modular
def calcular_inverso_modular(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Función para generar las claves RSA
def generar_claves(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Encontrar posibles valores de 'e' (1 < e < phi_n) coprimos con phi_n
    posibles_e = [e for e in range(2, phi_n) if calcular_mcd(e, phi_n) == 1]

    print("Valor de n:", n)
    print("Valor de φ(n): (p-1)*(q-1)")
    print("Valor de φ(n):", p-1," * ", q-1)
    print("Valor de φ(n):", phi_n)
    print("Posibles valores de e (coprimos con φ(n)):", posibles_e)

    # El usuario ingresa el valor de 'e'
    e = int(input("Ingresa el valor de 'e' de la lista de posibles valores: "))

    # Calcular el inverso modular de 'e' modulo phi_n para encontrar 'd'
    d = calcular_inverso_modular(e, phi_n)

    print("Valor de d:", d)

    # Clave pública (n, e)
    clave_publica = (n, e)
    # Clave privada (n, d)
    clave_privada = (n, d)

    print("Clave pública (Kpub):", clave_publica)
    print("Clave privada (Kprv):", clave_privada)

    return clave_publica, clave_privada

# Función para calcular el valor de 'k' tal que (k*phi_n + 1) % e = 0
def calcular_k(phi_n, e):
    k = 1
    while (k * phi_n + 1) % e != 0:
        k += 1
    return k

# Función para cifrar un mensaje usando la clave pública
def cifrar_mensaje(mensaje, clave_publica):
    n, e = clave_publica
    mensaje_cifrado = []
    for char in mensaje:
        char_ascii = ord(char)
        cifrado = pow(char_ascii, e, n)
        print(f"Cifrado de '{char}' ({char_ascii}): {char_ascii} ^ {e} % {n} = {cifrado}")
        mensaje_cifrado.append(cifrado)
    return mensaje_cifrado

# Función para descifrar un mensaje usando la clave privada
def descifrar_mensaje(mensaje_cifrado, clave_privada):
    n, d = clave_privada
    mensaje_descifrado = [chr(pow(char, d, n)) for char in mensaje_cifrado]
    return ''.join(mensaje_descifrado)

# Función principal
if __name__ == "__main__":
    p = int(input("Ingresa el valor de 'p' (número primo): "))
    q = int(input("Ingresa el valor de 'q' (número primo): "))

    clave_publica, clave_privada = generar_claves(p, q)

    mensaje = input("Ingresa el mensaje a cifrar: ")

    mensaje_cifrado = cifrar_mensaje(mensaje, clave_publica)
    print("Mensaje cifrado:", mensaje_cifrado)

    mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, clave_privada)
    print("Mensaje descifrado:", mensaje_descifrado)

    # Proceso de codificación con llave privada
    mensaje_codificado_privada = cifrar_mensaje(mensaje, clave_privada)
    print("Mensaje codificado con llave privada:", mensaje_codificado_privada)

    # Proceso de decodificación con llave pública
    mensaje_decodificado_publica = descifrar_mensaje(mensaje_codificado_privada, clave_publica)
    print("Mensaje decodificado con llave pública:", mensaje_decodificado_publica)

    # Calcular el valor de 'k' tal que (k*phi_n + 1) % e = 0
    phi_n = (p - 1) * (q - 1)
    k = calcular_k(phi_n, clave_publica[1])
    print("Valor de k:", k)

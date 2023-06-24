## Funciones.
import base64 
import hashlib

def encriptar(x):
	#b64encode No recibe STRINGS, entonces se conbierte a bytes
	txt_bytes=x.encode('utf-8')
	
	#Se codifica la el texto en bytes.
	codificado= base64.b64encode(txt_bytes)

	#se aplica Hash SHA256 sobre la codificacion b64
	salida = hashlib.sha384(codificado).hexdigest()

	print(f"Texto en bytes: 			{txt_bytes}")
	print(f"Codificacion Base64: 		{codificado}")
	print(f"code+hash: 					{salida}")

	return(salida)

x="Hola Mundo"
hashcode=encriptar(x)


print(f"							{hashcode}")




'''
def Modulo(n):
	m=n%2
	return m

n=int(input())
salida=Modulo(n)

print(salida)



def multplicar(x,y):
	z=x*y
	return z

salida=multplicar(2,5)
print(salida)



def concatenar(a,b):
	c=a+b
	return c

Texto=(concatenar("hola ","Mundo"))
print(Texto)

'''


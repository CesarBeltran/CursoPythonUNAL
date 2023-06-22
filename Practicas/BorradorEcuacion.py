'''ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 7-10 líneas de código)
Calcular el valor de PI usando la serie de Leibniz.
'''
n=25615
num=4
signo=1
pi=0.0

for n in range(0,n):
	if n%2!=0:
		pi=pi+signo*(num/n)
		signo*= -1
		print(f"n:{n} num={num} Denom{n} pi:{pi} signo: {signo}")
		
print(pi)

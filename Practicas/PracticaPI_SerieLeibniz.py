'''
Calcular el valor de PI usando la serie de Leibniz.
la serie está compuesta por las fracciones con numerador 1
 y denominador impar en orden, intercalando entre valores positivos y negativos
El resultado es el valor pi/4

'''
n=25615
num=4 ## el resultado de la serie se multiplica * 4, por eso se inicializa el numerador con valor en 4
signo=1
pi=0.0

for n in range(0,n):
	if n%2!=0:					#Realiza el calculo solo cuando n es Impar
		pi=pi+signo*(num/n)		#sumatoria de Leibniz
		signo*= -1				#cada iteracion se alterna el signo (-/+)
		print(f"n:{n} num={num} Denom{n} pi:{pi} signo: {signo}")
		
print(pi)

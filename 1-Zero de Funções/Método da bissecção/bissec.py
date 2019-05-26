import math

def f(x):
	return pow(math.e,-1*pow(x,2)) - math.cos(x)

def bissec(a,b,precisao):
	
	x=(a+b)/2
	iteracoes = 0
	
	while b-a >= precisao:
		x = (a+b)/2
		iteracoes += 1
		##print(x)
		##print(f(x))
		
		if f(a)*f(x) > 0:
			a = x
		else:
			b = x
			
		if b-a < precisao:
			break
		
	print("iteracoes =",iteracoes)
	return x
	

"""a = float(input("Insira a, o ínicio do intervalo:"))
b = float(input("Insira b, o fim do intervalo:"))
precisao=float(input("insira a precisao desejada:"))"""

a = 1
b = 2
precisao = pow(10,-4)

resultado = bissec(a,b,precisao)

print("resultado =",resultado)
print("f(x) =",f(resultado))

























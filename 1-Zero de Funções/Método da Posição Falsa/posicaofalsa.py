from math import*

def f(x):
	return pow(e,-1*pow(x,2)) - cos(x)
	
def posicaofalsa(a,b,erro1,erro2):
	
	x = (a*f(b) - b*f(a))/(f(b)-f(a))
	iteracoes = 0
	
	if b-a < erro1 or fabs(f(a)) < erro2 or fabs(f(b)) < erro2: 
		return a
	
	while b-a >= erro1 and fabs(f(x)) >= erro2: 
	
		x = (a*f(b) - b*f(a))/(f(b)-f(a))
		iteracoes += 1	
			
		if fabs(f(x)) < erro2:
			break
			
		if f(a)*f(x) > 0:
			a = x
		else:
			b = x
			
		if b - a < erro1:
			break

	print(iteracoes)
	return x

"""a = float(input())
b = float(input())
erro1 = float(input())
erro2 = float(input())"""
a = 1
b = 2
erro1 = pow(10,-4)
erro2 = pow(10,-4)
x = posicaofalsa(a,b,erro1,erro2)

print(x)
print(f(x))

























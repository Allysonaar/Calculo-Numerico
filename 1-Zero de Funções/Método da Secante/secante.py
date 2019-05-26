from math import*

def f(x):
	return pow(x,3) - x - 1
	
def secante(x0,x1,erro1,erro2):
	
	iteracoes = 0
	
	if fabs(f(x0)) < erro1:
		print(iteracoes)
		return x0
	
	if fabs(f(x1)) <erro1 or fabs(x1-x0) < erro2:
		print(iteracoes)
		return x1
		
	while 1:
		
		x2 = x1 - (f(x1)/(f(x1)-f(x0))) * (x1-x0)
		iteracoes += 1

		if fabs(f(x2)) < erro1 or fabs(x2 - x1) < erro2:
			print(iteracoes)
			return x2

		x0 = x1
		x1 = x2


"""x0 = float(input())
x1 = float(input())
erro1 = float(input())
erro2 = float(input())"""

x0 = 0
x1 = 0.5
erro1 = pow(10,-6)
erro2 = pow(10,-6)

x = secante(x0,x1,erro1,erro2)

print(x)
print(f(x))

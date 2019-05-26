from math import*

def f(x):
	return pow(e,-1*pow(x,2)) - cos(x)
	
def fi(x):
	return cos(x) - pow(e,-1*pow(x,2)) + x 

def mpf(x0,erro1,erro2):
	
	iteracao = 0
	
	if fabs(f(x0)) < erro1:
		print(iteracao)
		return x0
	
	while 1:
		x1 = fi(x0)
		iteracao += 1
		
		if fabs(f(x1)) < erro1 or fabs(x1 - x0) < erro2:
			break
			
		x0 = x1
	
	print(iteracao)
	return x1
	
	
x0 = 1.5
erro1 = pow(10,-4)
erro2 = pow(10,-4)
x = mpf(x0,erro1,erro2)

print(x)
print(f(x))


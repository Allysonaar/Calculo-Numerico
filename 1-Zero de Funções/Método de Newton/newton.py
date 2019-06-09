from sympy import*

x = symbols("x")

def f(x):
	return pow(x,3) -9*x + 3

def newton(x0,e1,e2,howmuch):
	
	if abs(f(x0)) < e1:
		return x0
	
	while howmuch:
	
		x1 = x0 - (f(x0)/diff(f(x),x).subs(x,x0))
		print(x1)
		
		if abs(f(x1)) < e1 or abs(x1 - x0) < e2:
			return x1
			 
		x0 = x1
		howmuch -= 1
		

x0 = 0.5
e1 = pow(10,-4)
e2 = pow(10,-4)
howmuch = -1

result = newton(x0,e1,e2,howmuch)

print(result)

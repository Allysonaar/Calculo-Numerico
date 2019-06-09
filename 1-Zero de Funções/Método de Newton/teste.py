from sympy import*


def f(x):
	return pow(x,3) -9*x + 3

x = symbols("x")

print(f(0.5))

print(diff(f(x),x))

from sympy import*
import math

def f(x):
	return pow(x,3) -9*x + 3

x = symbols("x")

pprint(Integral(f(x),x),uni_code = False)

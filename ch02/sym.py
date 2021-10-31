#%%
from sympy import *
import matplotlib.pyplot as plt

x = symbols('x')

f = x**3+x**2+x+1
print("f = " + str(f))
d = diff(f)
print("Derivatives = " + str(d))
i = integrate(f)
print("Integrate = " + str(i))

print('\n')

g = 1/x**3+1/x**2+1/x+1
print("g = " + str(g))
d = diff(g)
print("Derivatives = " + str(d))
i = integrate(g)
print("Integrate = " + str(i))

print('\n')


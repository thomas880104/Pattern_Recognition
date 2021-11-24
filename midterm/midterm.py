from sympy import *
from sympy.abc import i, k, m, n, x ,y
from sympy.stats import P, E, variance, Die, Normal
from scipy.stats import norm
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
init_printing(use_unicode=True)
#x,n = symbols('x n')
f = Function('f')(x,y)
g = Function('g')(x,y)
f = exp(-((x-1)**2+(y+1)**2))
#1.01
print(integrate(x**10, (x, 0,n)))

#1.02
print(Sum(x**10,(x,0,n)).doit())
#1.03
print(Sum((x-1)**10,(x,1,n)).doit())
#1.04
print(integrate(x**10*exp(-x), (x, 0,oo)))
#1.05
print(f.diff(x))
print(f.diff(y))
print(f.diff(x,y))
#1.06
eq1 = Eq(f.diff(x),0)
eq2 = Eq(f.diff(y),0)

print(solve([eq1,eq2],(x,y))) 
#1.07
i = sqrt(-1)
j = i**i
print(j.evalf())
#-------------------------------
a = Matrix([[5,1],[1,5]])
b = Matrix([[10],[20]])
print(a)
print(b)
#2.01
print(a**-1)
#2.02
print(a*b)
#2.03
#print(b*a)
#2.04
print(b.T*a)
print(a.eigenvects())
f = exp(-(x**2/2))/((2*pi)**1/2)
#-------------------------------
#3.01
print(norm.cdf(2)-norm.cdf(-2))
#3.02
print(integrate(f,(x,-oo,n)))
mean, var, skew, kurt = norm.stats(moments='mvsk')
#3.03
print(mean)
#3.04
print(var)
#3.05
print(skew)
#3.06
print(kurt)
#3.07
print(norm.entropy())
#3.08
r = norm.rvs(size=1000)
plt.plot(r)
plt.show()
#3.09
plt.hist(r,bins=100)
plt.show()


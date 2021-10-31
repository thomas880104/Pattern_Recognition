from sympy import *
import sympy.plotting as smpl 
import matplotlib.pyplot as plt


x,y = symbols('x,y')

z1= x**3+x**2+x+1 + 1/y**3+1/y**2+1/y+1 

title= ''' 

$z_1= (x**3+x**2+x+1 + 1/y**3+1/y**2+1/y+1)$ 

''' 

smpl.plot3d(z1,  
            
           	(x,-1,1), 

           xlabel='x', 

           ylabel='y', 

           title= title) 
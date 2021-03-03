# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 15:55:34 2020

@author: gonca
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
 
#x, y, z = sym.symbols('x y z')

# Criando a figura e projeção em 3D

kx = 1
ky = 1
kz = 1

# W = sym.sin(kx*x)*sym.sin(ky*y)*sym.exp(kz*z*sym.I)
def W(x, y):
    return np.sin(kx*x)*np.sin(ky*y)

for n in range(1, 4):
    ky = n*np.pi/4 
    for m in range(1, 4):
        print ('n = '+str(n)+' and m = '+str(m))
        kx = m*np.pi/3
        a = np.linspace(0,6,200)
        b = np.linspace(0,4,200)
        X, Y = np.meshgrid(a, b)
        Z = W(X, Y)
        
        fig = plt.figure('Plot Contour Slice '+ 'n = '+str(n)+' and m = '+str(m))
        fig.suptitle('Contour Slice Plot '+'n = '+str(n)+' and m = '+str(m), fontweight = 'bold', fontsize = 14)
        ax = plt.axes(projection='3d')

        ax.contour3D(X, Y, Z, 50, cmap='cool')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z');
        
        fig2 = plt.figure('Plot Contour levels '+ 'n = '+str(n)+' and m = '+str(m))
        fig2.suptitle('Contour Levels Plot '+'n = '+str(n)+' and m = '+str(m), fontweight = 'bold', fontsize = 14)
        ax2 = plt.axes()
        ax2.contour(X, Y, Z, 50, cmap='cool')
        

        plt.savefig('Plot Contour Slice '+ 'n = '+str(n)+' and m = '+str(m))
        plt.savefig('Plot Contour levels '+ 'n = '+str(n)+' and m = '+str(m))

    
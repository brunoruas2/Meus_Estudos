# Modulos usados
import time
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import tabloo # to see the df

from mpl_toolkits import mplot3d

pd.options.mode.chained_assignment = None  # default='warn'

plt.style.use('dark_background')

#####################################################################################################
# Funções usadas no modelo
#####################################################################################################
a = 100
b = 2

def dem_inv(y1,y2):
	return a - b*y1 - b*y2

def lucro2(y1,y2,c2):
	return (a*y2 - b*y1*y2 - b*y2*y2) - c2

def cur_reac(y1):
	return (a - b*y1)/4

def lucro1(y1,y2,c1):
	return (a*y1 - b*y1*y1 - b*y1*y2) - c1

#####################################################################################################
# Gerando o gráfico - fonte: https://www.geeksforgeeks.org/contour-plot-using-matplotlib-python/
#####################################################################################################

fig = plt.figure(dpi=120)
ax = plt.axes()
ax.grid(color='gray',linewidth=.2)

q1 = np.linspace(0,50,100)
q2 = cur_reac(q1)
  
# Creating 2-D grid of features
[X, Y] = np.meshgrid(q1, q2)
  
# plots contour lines
Z1 = lucro1(X,Y,0)
CL1 = ax.contour(X, Y, Z1, levels = [100,312.5,625,1000,1200])

Z2 = lucro2(X,Y,0)
CL2 = ax.contour(X, Y, Z2, levels = [100,312.5,625,1000,1200])

ax.set_title('cap 28.2 - Modelo de Stackelberg')
ax.set_xlabel('Qtd Empresa 1')
ax.set_ylabel('Qtd Empresa 2')

ax.clabel(CL1, inline=1, fontsize=10)
ax.clabel(CL2, inline=1, fontsize=10)

plt.plot(q1, q2,'--',color='red', label='f Reação Seguidora')

# adding points with a label
coord = [25,12.5]
plt.plot(coord[0],coord[1],marker='o',color='red')
plt.annotate('  Equilíbrio de \n Stackelberg',(coord[0],coord[1]))

plt.legend(loc='upper right')
plt.show()
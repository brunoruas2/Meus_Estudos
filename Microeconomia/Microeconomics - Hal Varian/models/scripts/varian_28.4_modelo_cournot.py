# Modulos usados
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

def f_reac1(y1):
	return (a - 2*b*y1)/(b)

def lucro1(y1,y2):
	return ((a - b*y2)*y1)/(2*b)

def f_reac2(y1):
	return (a - b*y1)/(2*b)

def lucro2(y1,y2):
	return ((a - b*y1)*y2)/(2*b)

#####################################################################################################
# Gerando o gráfico - fonte: https://www.geeksforgeeks.org/contour-plot-using-matplotlib-python/
#####################################################################################################

fig = plt.figure(dpi=120)
ax = plt.axes()
ax.grid(color='gray',linewidth=.2)

q1 = np.linspace(0,50,100)
q2 = np.linspace(0,50,100)

# Creating 2-D grid of features
[X, Y] = np.meshgrid(q1, q2)
  
# plots contour lines
level = lucro1(16.7,16.7)

Z1 = lucro1(X,Y)
CL1 = ax.contour(X, Y, Z1, levels = [level*0.5,level,level*1.5])

Z2 = lucro2(X,Y)
CL2 = ax.contour(X, Y, Z2, levels = [level*0.5,level,level*1.5])

ax.clabel(CL1, inline=1, fontsize=10)
ax.clabel(CL2, inline=1, fontsize=10)

ax.set_title('cap 28.5 - Modelo de Cournot')
ax.set_xlabel('Qtd Empresa 1')
ax.set_ylabel('Qtd Empresa 2')

plt.plot(q1, f_reac2(q1),'-',color='red', label='Reação Empresa 2')
plt.plot(q1, f_reac1(q2),'-',color='blue', label='Reação Empresa 1')

# adding points with a label
coord = [16.7,16.7]
plt.plot(coord[0],coord[1],marker='o',color='white')
plt.annotate('  Equilíbrio de \n Cournot',(coord[0],coord[1]))

plt.xlim(0)
plt.ylim(0)
plt.legend(loc='upper right')
plt.show()
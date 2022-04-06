# Modulos usados
import os
from matplotlib import colors
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import tabloo # to see the df

from PIL import Image
from mpl_toolkits import mplot3d
from mpl_toolkits.axes_grid1 import host_subplot

pd.options.mode.chained_assignment = None  # default='warn'

plt.style.use('dark_background')

#####################################################################################################
# Funções usadas no modelo
#####################################################################################################
# funcoes de utilidade
def fu_a(x1,x2,alpha,beta):
	return (x1**alpha)*(x2**beta)

def fu_b(x1,x2,a,b):
	return (x1**a)*(x2**b)

def dem(a,b,wa1,wa2,p1,p2):
	return [(a*(wa1*p1 + wa2 * p2))/(p1),(b*(wa1*p1 + wa2 * p2))/(p2)]

def dotacao(w1,w2,x1,p1,p2):
	return ((w1*p1 + w2*p2) - p1*x1)/p2

#####################################################################################################
# Gerando o gráfico - fonte: https://pythontic.com/image-processing/pillow/blend
#####################################################################################################
## dados
max_val = 100
q1 = np.linspace(0,max_val,100)
q2 = np.linspace(0,max_val,100)

alpha = 0.1
beta = 0.9
a = 0.5
b = 0.5

p1 = 1
p2 = 2

x1a = dem(alpha,beta,80,20,p1,p2)[0]
x2a = dem(alpha,beta,80,20,p1,p2)[1]
x1b = dem(a,b,20,80,p1,p2)[0]
x2b = dem(a,b,20,80,p1,p2)[1]

# graph
fig = plt.figure(dpi=120)
ax = host_subplot(111)
ax.grid(color='gray',linewidth=.2)

ax.set_title('cap 32.4 - Caixa de Edgeworth (p1 = 1 e p2 = 2)\n')
ax.set_xlabel('Bem 1')
ax.set_ylabel('Bem 2')

# Creating 2-D grid of features
[X, Y] = np.meshgrid(q1, q2)  

# plots contour lines
Z1 = fu_a(X,Y,0.1,0.9)
#CL1 = ax.contour(X, Y, Z1, colors="red", levels = range(0,100,10), alpha = 1) # , cmap="winter"
CL1 = ax.contour(X, Y, Z1, colors="red", levels = [fu_a(x1a,x2a,alpha,beta)], alpha = 1) # , cmap="winter"
ax.clabel(CL1, inline=1, fontsize=10)

ax.yaxis.tick_left()
ax.yaxis.set_ticks_position('both')
ax.xaxis.tick_bottom()
ax.xaxis.set_ticks_position('both')

plt.xlim(0,100)
plt.ylim(0,100)

ax = host_subplot(111)
ax.grid(color='gray',linewidth=.2)

Z2 = fu_b(X,Y,0.5,0.5)
#CL2 = ax.contour(X, Y, Z2, colors="cyan", levels = range(0,100,10), alpha = 1) # , cmap="winter"
CL2 = ax.contour(X, Y, Z2, colors="cyan", levels = [fu_b(x1b,x2b,a,b)], alpha = 1) # , cmap="winter"
ax.clabel(CL2, inline=1, fontsize=10)

# adding line graphs
#plt.plot(q1,q2,color = 'white') # curva de contrato
plt.plot(q1,dotacao(20,80,q1,p1,p2),color = 'white') # curva de dotacao

# adding points with a label
coord = [20,80] # aqui os eixos estao invertidos Y e X
plt.plot(coord[0],coord[1],marker='o',color='white')
plt.annotate('  Dotação\n  Inicial',(coord[0],coord[1]))

'''
coord = [50,50] # aqui os eixos estao invertidos Y e X
plt.plot(coord[0],coord[1],marker='o',color='white')
plt.annotate('  Alocação\n  Final\n  Possível',(coord[0],coord[1]))
'''
# putting arows
'''
coord = [0,40]
ax.text(
    coord[0], coord[1], "Bem 2 para consumidor B", ha="center", va="center", rotation=-90, size=10,
    bbox=dict(boxstyle="rarrow,pad=0.3", fc="royalblue", ec="royalblue", lw=1))

coord = [40,0]
ax.text(
    coord[0], coord[1], "Bem 1 para consumidor B", ha="center", va="center", rotation=0, size=10,
    bbox=dict(boxstyle="larrow,pad=0.3", fc="royalblue", ec="royalblue", lw=1))

coord = [100,60]
ax.text(
    coord[0], coord[1], "Bem 2 para consumidor A", ha="center", va="center", rotation=-90, size=10,
    bbox=dict(boxstyle="larrow,pad=0.3", fc="darkred", ec="darkred", lw=1))

coord = [60,100]
ax.text(
    coord[0], coord[1], "Bem 1 para consumidor A", ha="center", va="center", rotation=0, size=10,
    bbox=dict(boxstyle="rarrow,pad=0.3", fc="darkred", ec="darkred", lw=1))
'''

ax.yaxis.tick_right()
ax.yaxis.set_ticks_position('both')
ax.xaxis.tick_top()
ax.xaxis.set_ticks_position('both')

plt.xlim(100,0)
plt.ylim(100,0)

#plt.legend(loc='upper left')
path = \
r'C:\Users\bruno\Documents\Metadata\Meus_Estudos\Microeconomia'\
r'\Microeconomics - Hal Varian\images\cap31_1-caixa_edgeworth_9.png'

plt.savefig(path, transparent=True)

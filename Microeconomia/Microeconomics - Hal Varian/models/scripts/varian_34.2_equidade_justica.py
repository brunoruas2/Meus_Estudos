# Modulos usados
from cProfile import label
import os
from cv2 import rotate
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
#plt.rcParams['text.usetex'] = True

#####################################################################################################
# Funções usadas no modelo
#####################################################################################################
# funcoes de utilidade
def fu_rob(x1,x2,alpha,beta):
	return (x1**alpha)*(x2**beta)

def fu_feira(x1,x2,alpha,beta):
	return (x1**alpha)*(x2**beta)

def f_prod(x1,a):
	return x1**a

def fp_peixe(x1,a):
	return x1**a

def fp_coco(x1,a):
	return x1**a

def isolucro(pi,w,L):
	return pi + w*L

#####################################################################################################
# Gerando o gráfico
#####################################################################################################
## dados
max_val = 400
q1 = np.linspace(0,max_val,100)
q2 = np.linspace(0,max_val,100)

alpha = 0.5
beta = 0.5

PF = 1
PC = 1

# graph
fig = plt.figure(dpi=120)
ax = host_subplot(111)
ax.grid(color='gray',linewidth=.2)

ax.set_title('cap 34 - Bem-Estar')
ax.set_xlabel('')
ax.set_ylabel('')
#ax.xaxis.set_major_locator(plt.NullLocator())
#ax.yaxis.set_major_locator(plt.NullLocator())

# fake axis
'''
plt.figtext(0.04, 0.09, "Pessoa\n    A", fontsize = 10)
plt.figtext(0.91, 0.85, "Pessoa\n    B", fontsize = 10)
plt.figtext(0.06, 0.85, "Bem\n  2", fontsize = 10)
plt.figtext(0.91, 0.09, "Bem\n  1", fontsize = 10)
plt.figtext(0.06, 0.5, "w2/2", fontsize = 10)
plt.figtext(0.91, 0.5, "w1/2", fontsize = 10)
'''

# curva de alocacao justa
plt.plot(q1,(300**2 - q1**2)**(1/2), color='red')

# curva de indiferenca
plt.plot(q1,((212/(q1**0.5))**2),color='blue',alpha=1)

# pontos de alocacao
coord = [300,125]
plt.plot(coord[0],coord[1],marker='o',color='white')
plt.annotate('Alocação\nresultante\nda troca',(coord[0]+3,coord[1]),fontsize=10)

coord = [210,214]
plt.plot(coord[0],coord[1],marker='o',color='white')
plt.annotate('Alocação\njusta',(coord[0]+5,coord[1]),fontsize=10)


# linha entre as alocacoes
plt.plot([300,210],[125,214],color='white')

plt.xlim(25,350)
plt.ylim(25,350)

path = r'C:\Users\bruno\Documents\Metadata\Meus_Estudos\Microeconomia\Microeconomics - Hal Varian\images\cap34_6-inveja_equidade.png'
plt.savefig(path, transparent=True)

plt.show()

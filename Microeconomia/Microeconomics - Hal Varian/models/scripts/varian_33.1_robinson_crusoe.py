# Modulos usados
from cProfile import label
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
def fu_rob(x1,x2,alpha,beta):
	return (x1**alpha)*(x2**beta)

def f_prod(x1,a):
	return x1**a

def isolucro(pi,w,L):
	return pi + w*L

#####################################################################################################
# Gerando o gráfico
#####################################################################################################
## dados
max_val = 100
q1 = np.linspace(0,max_val,100)
q2 = np.linspace(0,max_val,100)

alpha = 0.5
beta = 0.5

# graph
fig = plt.figure(dpi=120)
ax = host_subplot(111)
ax.grid(color='gray',linewidth=.2)

ax.set_title('cap 33 - A maximização do Lucro')
ax.set_xlabel('Trabalho = 100 - Lazer')
ax.set_ylabel('Cocos')

plt.plot(q1,f_prod(14*q1,1/2),color='red',label='função de produção')

'''
# curvas de indiferença
for i in [38]:
	plt.plot(q1,(i/(100-q1)**0.5)**(1/0.5),label='C.I. = {}'.format(i))
'''

# curva de iso lucro
for i in range(12,13,1):
	plt.plot(q1,isolucro(i,0.3,q1),label='Isolucro = {}'.format(i))


# point
coord = [41.5,24.5]
plt.plot(coord[0],coord[1],marker='o',color='white')
#plt.annotate('  Cesta',(coord[0],coord[1]))


plt.xlim(0,100)
plt.ylim(0,50)

plt.legend(loc='upper left')

path = r'C:\Users\bruno\Documents\Metadata\Meus_Estudos\Microeconomia\Microeconomics - Hal Varian\images\cap33_3-max_lucro.png'

plt.savefig(path, transparent=True)


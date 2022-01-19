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
#plt.rcParams['text.usetex'] = True

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

ax.set_title('cap 33 - Equilíbrio no Consumo e Produção')
ax.set_xlabel('<- Lazer | trabalho -> ')
ax.set_ylabel('Cocos')

# funcao de producao
plt.plot(q1,f_prod(14*q1,1/2),color='red',label='função de produção')

# curvas de indiferença
plt.plot(q1,(38/(100-q1)**0.5)**(1/0.5),label='C.I.')

# curva de iso lucro e reta orçamentaria
#plt.plot(q1,isolucro(11.5,0.31,q1),label='Isolucro')
plt.plot(q1,isolucro(11.5,0.31,q1),label='Restrição\nOrçamentária')


# point
coord = [33.3,22]
plt.plot(coord[0],coord[1],marker='o',color='white')
#plt.annotate(r'$\pi^*$',(coord[0],coord[1]+1),fontsize=20)


plt.xlim(0,100)
plt.ylim(0,50)

plt.legend(loc='upper left')

#plt.show()

path = r'C:\Users\bruno\Documents\Metadata\Meus_Estudos\Microeconomia\Microeconomics - Hal Varian\images\cap33_5-equilibrio.png'
plt.savefig(path, transparent=True)


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
ax.set_xlabel('Utilidade Pessoa 1')
ax.set_ylabel('Utilidade Pessoa 2')

# funcoes de producao
#plt.plot(q1,f_prod(14*q1,1/2),color='red',label='função de produção') # retornos decrescentes
#plt.plot(q1,q1*0.57,color='red',label='Função de Produção/\nRestrição Orçamentária') # retornos constantes

# curvas de indiferença
#plt.plot(q1,(38/(100-q1)**0.5)**(1/0.5),label='C.I.')
for i in range(0,500,40):
	if i == 0:
		plt.plot(q1,((i/(q1**0.5))**2),color='blue',alpha=1,label='Curvas de Isobem-estar')
	else:
		plt.plot(q1,((i/(q1**0.5))**2),color='blue',alpha=1)

# possibilidade de producao
x = [0,50,145,200,245,287,300] # q1
y = [300,287,245,200,145,50,0] # 10 * (10 - (q1/20)) + 20 * (10 - (q1/10))
plt.plot(x,y,color='red',label='Fronteira Possibilidade Utilidade',linewidth=2)
plt.fill_between(x, y, color='red',alpha=0.08) # area vermelha

# curva de iso lucro e reta orcamentaria
#plt.plot(q1,isolucro(11.5,0.31,q1),label='Isolucro')
#plt.plot(q1,isolucro(11.5,0.31,q1),label='Restrição\nOrçamentária')
#for pi in range(392,393,392):
pi = 392
pi_L = pi + 10 # lucro + trabalho-otimo
pC = 5
pF = 5
#plt.plot(q1,(pi_L-(pF/pC)*q1),color='white',label='Isolucro')

# point
#coord = [51,30]
#plt.plot(coord[0],coord[1],marker='o',color='white')
#plt.annotate(r'$\pi^*$',(coord[0],coord[1]+1),fontsize=20)

coord = [200,200]
plt.plot(coord[0],coord[1],marker='o',color='white')
plt.annotate('Conjunto de\npossibilidades\nde utilidade',(100,100),fontsize=10)
plt.annotate('Bem-Estar\n Máximo',(coord[0],coord[1]),fontsize=10)

plt.xlim(0,350)
plt.ylim(0,350)

plt.legend(loc='upper right')

path = r'C:\Users\bruno\Documents\Metadata\Meus_Estudos\Microeconomia\Microeconomics - Hal Varian\images\cap34_3-maximizacao_bem_estar.png'
plt.savefig(path, transparent=False)

plt.show()

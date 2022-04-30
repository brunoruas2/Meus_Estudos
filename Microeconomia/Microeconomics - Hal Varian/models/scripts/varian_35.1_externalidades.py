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
from labellines import labelLines
from mpl_toolkits.axes_grid1 import host_subplot

pd.options.mode.chained_assignment = None  # default='warn'

plt.style.use('dark_background')
#plt.rcParams['text.usetex'] = True

#####################################################################################################
# Funções usadas no modelo
#####################################################################################################
# funcoes de utilidade
def fu_A(x1,x2,alpha,beta):
	return (x1**alpha)*(x2**beta)

def fu_B(x1,x2,alpha,beta):
	return (x1**alpha)*(x2**beta)


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

ax.set_title('cap 35 - Externalidades')
ax.set_xlabel('')
ax.set_ylabel('')
ax.xaxis.set_major_locator(plt.NullLocator())
ax.yaxis.set_major_locator(plt.NullLocator())

# fake axis
plt.figtext(0.04, 0.09, "Pessoa\n    A", fontsize = 10)
plt.figtext(0.91, 0.85, "Pessoa\n    B", fontsize = 10)
plt.figtext(0.040, 0.85, "Fumaça", fontsize = 10)
plt.figtext(0.905, 0.09, "Dinheiro", fontsize = 10)

# dotacoes
coord = [50,0]
plt.plot(coord[0],coord[1],marker='o',color='white')
plt.annotate('Dotação E',(coord[0]+2,coord[1]+1),fontsize=10)

coord = [50,100]
plt.plot(coord[0],coord[1],marker='o',color='white')
plt.annotate('Dotação E\'',(coord[0]-15,coord[1]-5),fontsize=10)

plt.plot([50,50],[0,100],color='white',linestyle='--')

# curvas de indiferenca
for u_max in [15,25,45,75,87]:
	if u_max == 15:
		plt.plot(q1,(u_max/(q1**alpha))**(1/beta),color='red',label='Utilidade A')
		plt.plot(q1,(max_val - (u_max/((max_val - q1)**alpha))**(1/beta)),color='blue',label='Utilidade B')
	else:
		plt.plot(q1,(u_max/(q1**alpha))**(1/beta),color='red')
		plt.plot(q1,(max_val - (u_max/((max_val - q1)**alpha))**(1/beta)),color='blue')

# Dotações possiveis
plt.plot([50,0],[0,50],color='white')
plt.plot([50,100],[100,50],color='white')

# Cestas possiveis
coord = [25,25]
plt.annotate(' Cesta X',coord)
plt.plot(coord[0],coord[1],marker='o',color='white')

coord = [75,75]
plt.annotate(' Cesta Y',coord)
plt.plot(coord[0],coord[1],marker='o',color='white')


plt.xlim(0,100)
plt.ylim(0,100)

labelLines(plt.gca().get_lines(), zorder=2.5)

#plt.legend(loc='upper left')

path = r'C:\Users\bruno\Documents\Metadata\Meus_Estudos\Microeconomia\Microeconomics - Hal Varian\images\cap35_1-dinheiro_fumaca.png'
plt.savefig(path, transparent=False)

plt.show()

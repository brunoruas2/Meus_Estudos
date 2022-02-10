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

# curvas de indiferenca
for u_max in range(0,200,10):
	if u_max == 15:
		plt.plot(q1,(u_max - 5*q1**alpha),color='red',label='Utilidade A')
#		plt.plot(q1,(max_val - (u_max - q1**alpha)),color='blue',label='Utilidade B')
	else:
		plt.plot(q1,(u_max - 5*q1**alpha),color='red')
#		plt.plot(q1,(max_val - (u_max - q1**alpha)),color='blue')


plt.xlim(0,100)
plt.ylim(0,100)

labelLines(plt.gca().get_lines(), zorder=2.5)

plt.legend(loc='upper left')

path = r'C:\Users\bruno\Documents\Metadata\Meus_Estudos\Microeconomia\Microeconomics - Hal Varian\images\cap35_2-teorema_coase.png'
plt.savefig(path, transparent=True)

plt.show()

# Modulos usados
import math
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from mpl_toolkits.axes_grid1 import host_subplot

pd.options.mode.chained_assignment = None  # default='warn'

plt.style.use('dark_background')
#plt.rcParams['text.usetex'] = True

#####################################################################################################
# Funções usadas no modelo
#####################################################################################################


#####################################################################################################
# Gerando o gráfico
#####################################################################################################
## dados
max_val = 20
q1 = np.linspace(0,max_val,100)
q2 = np.linspace(0,max_val,100)

alpha = 0.5
beta = 0.5

# graph
fig = plt.figure(dpi=120)
ax = host_subplot(111)
ax.grid(color='gray',linewidth=.2)

ax.set_title('cap 35 - Externalidades')
ax.set_ylabel('PMe\nPMa')
ax.set_xlabel('Quantidade de Vacas')

# curvas
plt.plot(q1,-2*q1 + 20,color='green',label='PMa')
plt.plot(q1,-1*q1 + 20,color='red',label='PMe')
plt.plot([0,max_val],[5,5],color='white',label='a')

coord = [7.5,5]
plt.annotate('Maximização\ndo Lucro',coord)
plt.plot(coord[0],coord[1],marker='.',color='white')

coord = [15,5]
plt.annotate('Equilíbrio\ndos Comuns',coord)
plt.plot(coord[0],coord[1],marker='.',color='white')


plt.xlim(0,max_val)
plt.ylim(0,max_val)

plt.legend(loc='upper right')

path = r'C:\Users\bruno\Documents\Metadata\Meus_Estudos\Microeconomia\Microeconomics - Hal Varian\images\cap35_6-tragedia_comum.png'
plt.savefig(path, transparent=False)

plt.show()

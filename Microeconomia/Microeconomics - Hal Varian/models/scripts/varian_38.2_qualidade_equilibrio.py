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
# Gerando o gráfico
#####################################################################################################
## dados
max_val = 20
q1 = np.linspace(0,max_val,100)
q2 = np.linspace(0,max_val,100)

alpha = 0.5
beta = 0.5

fig = plt.figure(dpi=120)

# graph 1 - left panel
ax1 = host_subplot(111)
ax1.grid(color='gray',linewidth=.2)

ax1.set_title('cap 38 - Bens Públicos')
ax1.set_ylabel('Preço')
ax1.set_xlabel('Parcela de Empresas de Alta Qualidade')

# curvas
plt.plot(q1,11.50+(q1*0),color='red')
plt.plot([0.535,1],[11.5,11.5],color='white')
plt.plot(q1,14*q1+8*(1-0.5),color='blue',label='Demanda')
plt.plot([0.535,0.535],[0,20],linestyle='--',color='gray')

plt.xlim(0,1)
plt.ylim(0,max_val)

plt.legend(loc='upper right')

path = r'C:\Users\bruno\Documents\Metadata\Meus_Estudos\Microeconomia\Microeconomics - Hal Varian\images\cap38_2-qualidade_equilibrio.png'
plt.savefig(path, transparent=False)

plt.show()

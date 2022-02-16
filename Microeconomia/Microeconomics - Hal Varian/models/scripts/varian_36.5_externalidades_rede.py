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
max_val = 1250
q1 = np.linspace(0,max_val,100)
q2 = np.linspace(0,max_val,100)

alpha = 0.5
beta = 0.5

fig = plt.figure(dpi=120)

# graph 1 - left panel
ax1 = host_subplot(111)
ax1.grid(color='gray',linewidth=.2)

ax1.set_title('cap 36 - Tecnologia da Informação')
ax1.set_ylabel('Propensão a Pagar')
ax1.set_xlabel('Tamanho da Rede')

# curvas
plt.plot(q1,-(q1**1.5)+q1*20+15,color='red')
plt.plot(q1,400+(q1*0),color='white')

plt.xlim(0,400)
plt.ylim(0,max_val)

#plt.legend(loc='upper right')

path = r'C:\Users\bruno\Documents\Metadata\Meus_Estudos\Microeconomia\Microeconomics - Hal Varian\images\cap36_5-externalidades_rede.png'
plt.savefig(path, transparent=False)

plt.show()

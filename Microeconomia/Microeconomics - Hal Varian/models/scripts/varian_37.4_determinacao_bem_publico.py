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

# graph
fig = plt.figure(dpi=120)
ax = host_subplot(111)
ax.grid(color='gray',linewidth=.2)

ax.set_title('cap 37 - Bens Públicos')
ax.set_ylabel('TMS')
ax.set_xlabel('G')

# curvas
plt.plot(q1,10-0.6*q1,color='green',label='TMS1')
plt.plot(q1,7-0.417*q1,color='green',alpha=0.5,label='TMS2')
plt.plot(q1,(10-0.6*q1)+(7-0.417*q1),color='blue',label='TMS1+TMS2')

plt.plot(q1,2+q1**1.09,label='CMa')

coord = [6.85,10.15]
plt.annotate('   G*',coord)
plt.plot(coord[0],coord[1],marker='o',color='white')


plt.xlim(0,max_val)
plt.ylim(0,max_val)

plt.legend(loc='upper right')

path = r'C:\Users\bruno\Documents\Metadata\Meus_Estudos\Microeconomia\Microeconomics - Hal Varian\images\cap37_4-bem_publico.png'
plt.savefig(path, transparent=False)

plt.show()

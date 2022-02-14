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

# graph 1 - left panel
fig = plt.figure(dpi=120)
ax = host_subplot(111)
ax.grid(color='gray',linewidth=.2)

ax.set_title('cap 37 - Bens Públicos')
ax.set_ylabel('Bem Público')
ax.set_xlabel('Bem Privado')

# curvas
plt.plot(q1,15-1*q1,color='red',label='w1')
plt.plot(q1,(7.5/q1**alpha)**(1/beta))

coord = [7.5,7.5]
plt.annotate('   G = g1 e x1',coord)
plt.plot(coord[0],coord[1],marker='o',color='white')


plt.xlim(0,max_val)
plt.ylim(0,max_val)

plt.legend(loc='upper right')

path = r'C:\Users\bruno\Documents\Metadata\Meus_Estudos\Microeconomia\Microeconomics - Hal Varian\images\cap37_6-problema_carona1.png'
plt.savefig(path, transparent=False)

plt.show()

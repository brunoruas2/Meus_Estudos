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
# funcoes de utilidade
def fu_A(x1,x2,alpha,beta):
	return (x1**alpha)*(x2**beta)

def fu_B(x1,x2,alpha,beta):
	return (x1**alpha)*(x2**beta)


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
for util in range(0,200,4):
	if util == 0:
		plt.plot(q1,(math.e**(util - q1)),color='red',label='Utilidade A')
		plt.plot(q1,max_val - (math.e**(util - (max_val - q1 - 0.6))),color='blue',label='Utilidade B')
	else:
		plt.plot(q1,(math.e**(util - q1)),color='red')
		plt.plot(q1,max_val - (math.e**(util - (max_val - q1 - 0.6))),color='blue')

# curva de contrato

plt.plot([0,20],[10,10],color='white',label='Curva de Contrato')

plt.xlim(0,max_val)
plt.ylim(0,max_val)

plt.legend(loc='upper right')

path = r'C:\Users\bruno\Documents\Metadata\Meus_Estudos\Microeconomia\Microeconomics - Hal Varian\images\cap35_2-teorema_coase.png'
plt.savefig(path, transparent=False)

plt.show()

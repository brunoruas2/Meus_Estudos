# Modulos usados
import time
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d

pd.options.mode.chained_assignment = None  # default='warn'

plt.style.use('dark_background')

#####################################################################################################
# Funções usadas no modelo
#####################################################################################################
# constantes usadas nas funcoes
a = 100
b = 2

def oferta_2(p1):
	return p1

def demanda_inv(q):
	return (a - q)/b

def demanda_res_inv(q):
	return (a - q)/(b + 1)

def cma1(q):
	return 5 * (q/q)

def rma1(q):
	return (a/(b+1)) - (2/(b+1))*q

#####################################################################################################
# Gerando o gráfico
#####################################################################################################

fig = plt.figure(dpi=120)
ax = plt.axes()
ax.grid(color='gray',linewidth=.2)

# vetores
q1 = np.linspace(0,100,100)
q2 = oferta_2(q1)
demanda = demanda_inv(q1)
demanda_res = demanda_res_inv(q1)

ax.set_title('cap 28.3 - Modelo de Liderança no Preço')
ax.set_xlabel('Quantidade')
ax.set_ylabel('Preço')

plt.plot(q1, q2,'--',color='blue', label='Oferta da Seguidora')
plt.plot(q1, demanda,'-',color='red', label='Demanda')
plt.plot(q1, demanda_res,'--',color='red', label='Demanda Residual')
plt.plot(q1, cma1(q1),'-',color='green', label='CMa1')
plt.plot(q1, rma1(q1),'-',color='yellow', label='RMa1')

plt.ylim(0,50)
plt.xlim(0)

# adding points with a label
coord = [42,19.5]
plt.plot(coord[0],coord[1],marker='o',color='white')
plt.annotate(' Qtd \n Lider',(coord[0],coord[1]))

coord = [61.5,19.5]
plt.plot(coord[0],coord[1],marker='o',color='white')
plt.annotate(' Qtd \n Total',(coord[0],coord[1]))

coord = [19,19.5]
plt.plot(coord[0],coord[1],marker='o',color='white')
plt.annotate('  Qtd \n Seguidor',(coord[0],coord[1]))

plt.legend(loc='upper right')
plt.show()
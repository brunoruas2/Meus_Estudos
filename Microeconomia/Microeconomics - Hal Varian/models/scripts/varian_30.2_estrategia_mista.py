# Modulos usados
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import tabloo # to see the df

from mpl_toolkits import mplot3d

pd.options.mode.chained_assignment = None  # default='warn'

plt.style.use('dark_background')

#####################################################################################################
# Funções usadas no modelo
#####################################################################################################
# curvas de melhor resposta
def melhor_a(pb_left):
	pb_right = 1 - pb_left

	banco = pd.DataFrame()

	i = 0
	while i < 1.01:
		pa_up = i
		pa_down = abs(round(1 - pa_up,2))
		result = (2*pa_up*pb_left) + (0*pa_down*pb_left) + (0*pa_up*pb_right) + (1*pa_down*pb_right)
		banco = banco.append([[pa_up,pa_down,pb_left,pb_right,result]])
		i = i + 0.01
	
	banco.columns = ['pa_up','pa_down','pb_left','pb_right','result']

	if banco[banco['result'] == max(banco['result'])]['pa_up'].shape[0] != 1:
		return max(banco[banco['result'] == max(banco['result'])]['pa_up'])
	else:
		return max(banco[banco['result'] == max(banco['result'])]['pa_up'])

def melhor_b(pa_up):
	pa_down = 1 - pa_up

	banco = pd.DataFrame()

	i = 0
	while i < 1.01:
		pb_left = i
		pb_right = abs(round(1 - pb_left,2))
		result = (1*pa_up*pb_left) + (0*pa_down*pb_left) + (0*pa_up*pb_right) + (2*pa_down*pb_right)
		banco = banco.append([[pa_up,pa_down,pb_left,pb_right,result]])
		i = i + 0.01
		
	banco.columns = ['pa_up','pa_down','pb_left','pb_right','result']

	if banco[banco['result'] == max(banco['result'])]['pb_left'].shape[0] != 1:
		return max(banco[banco['result'] == max(banco['result'])]['pb_left'])
	else:
		return max(banco[banco['result'] == max(banco['result'])]['pb_left'])

#####################################################################################################
# Gerando o gráfico - fonte: https://www.geeksforgeeks.org/contour-plot-using-matplotlib-python/
#####################################################################################################

fig = plt.figure(dpi=120)
ax = plt.axes()
ax.grid(color='gray',linewidth=.2)

q1 = np.linspace(0,1,300)
q2 = np.linspace(0,1,300)
  
ax.set_title('cap 30.2 - Estratégias Mistas')
ax.set_ylabel('Jogador Coluna - Prob Esquerda')
ax.set_xlabel('Jogador Linha - Prob Alto')

# lines
resultado_a = list()
resultado_b = list()
for x in range(0,len(q2)):
	print(x/len(q2))
	resultado_a.append(melhor_a(q2[x]))
	resultado_b.append(melhor_b(q1[x]))

plt.plot(resultado_a, q2,'-',color='blue', label='Melhor Resp Linha',linewidth=4)
plt.plot(q1, resultado_b,'-',color='red', label='Melhor Resp Coluna',linewidth=4)

# points
coord = [2/3,1/3]
plt.plot(coord[0],coord[1],marker='o',color='white')
plt.annotate('Equilíbrio\nde Nash',(coord[0]-0.05,coord[1]+0.05))

coord = [0,0]
plt.plot(coord[0],coord[1],marker='o',color='white')

coord = [1,1]
plt.plot(coord[0],coord[1],marker='o',color='white')

plt.xlim(0,1)
plt.ylim(0,1)
plt.legend(loc='upper left')

plt.show()
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
def return_a(pa_up,pb_left):
	pa_down = 1 - pa_up
	pb_right = 1 - pb_left

	return (0*pa_up*pb_left) + (1*pa_down*pb_left) + (0*pa_up*pb_right) + (-1*pa_down*pb_right)

def return_b(pa_up,pb_left):
	pa_down = 1 - pa_up
	pb_right = 1 - pb_left

	return (0*pa_up*pb_left) + (0*pa_down*pb_left) + (-1*pa_up*pb_right) + (3*pa_down*pb_right)

#####################################################################################################
# Gerando o gráfico - fonte: https://www.geeksforgeeks.org/contour-plot-using-matplotlib-python/
#####################################################################################################

fig = plt.figure(dpi=120)
ax = plt.axes()
ax.grid(color='gray',linewidth=.2)

q1 = np.linspace(0,1,200)
q2 = np.linspace(0,1,200)
  
ax.set_title('cap 29.3 - Equilíbrio Nash em Estratégia Mista')
ax.set_ylabel('Jogador B - Prob Esquerda')
ax.set_xlabel('Jogador A - Prob Alto')

# Creating 2-D grid of features
[X, Y] = np.meshgrid(q1, q2)
  
# plots contour lines
Z1 = return_a(X,Y)
CL1 = ax.contour(X, Y, Z1, cmap="autumn_r")
ax.clabel(CL1, inline=1, fontsize=10)

Z2 = return_b(X,Y)
CL2 = ax.contour(X, Y, Z2, cmap="winter")
ax.clabel(CL2, inline=1, fontsize=10)

coord = [0.75,0.5]
plt.plot(coord[0],coord[1],marker='.',color='white')
plt.annotate('Equilíbrio\nde Nash',(coord[0]-0.05,coord[1]+0.05))

plt.xlim(0,1)
plt.ylim(0,1)

plt.show()
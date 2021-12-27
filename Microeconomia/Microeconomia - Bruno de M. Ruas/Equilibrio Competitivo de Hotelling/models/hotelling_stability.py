
#####################################################################################################
# Computacao do modelo de Herald Hotelling - Stability in Competition (1929)
#####################################################################################################

# Modulos usados
import time
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

def lucro1(l,a,b,p1_max,p2_max):

#####################################################################################################
# Montando o banco de dados
#####################################################################################################
y_min = 0
y_max = 100
data = pd.DataFrame(np.zeros([y_max,y_max]))
data['q1'] = range(y_min,data.shape[0])

# lembrete: x = y1 e data.columns[i] = y2
for i in range(0,data.shape[1]-1):
	print(i/data.shape[1])
	data[i] = data['q1'].apply(lambda x: \
		max_y1(x,x,data.columns[i],0,20)['lucro1'].iloc[0] + \
		max_y2(data.columns[i],data.columns[i],x,0,20)['lucro2'].iloc[0])

data2d = pd.DataFrame()
for i in range(0,data.shape[1]-1):
	for j in range(0,data.shape[0]):
		print(i/data.shape[1])
		data2d = data2d.append([[data['q1'].iloc[j],data.columns[i],data[i].iloc[j]]])

data2d.columns = ['q1','q2','lucro']
data2d = data2d[data2d['lucro'] > 0]

#####################################################################################################
# Gerando o gráfico
#####################################################################################################

fig = plt.figure(dpi=120)
ax = plt.axes(projection='3d')
ax.grid(color='gray',linewidth=.2)

plt.title('Cap 26.6 - Tarifas Bipartidas')

# plot labels
ax.set_zlabel('Lucro')
ax.set_xlabel('Bem 1')
ax.set_ylabel('Bem 2')

# data from a 3d line plot
zline = data2d['lucro']
xline = data2d['q1']
yline = data2d['q2']

ax.scatter(xline,yline,zline, c=zline,alpha=0.5)

ax.set_xlim3d(min(xline), max(xline))
ax.set_ylim3d(min(yline), max(yline))
ax.set_zlim3d(0, max(zline))

plt.show()
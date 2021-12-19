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

# Parte 1 - Função que me retorne o p1 e q1 que maximizam o lucro do monopolista
def p1(y1,y2):
	return 100 - y1 - y2

def rec1(y1,y2):
	return p1(y1,y2) * y1

def custo1(cf1,cv1,y1):
	return cf1 + cv1 * y1

def rma1(y1,y2):
	return 100 - 2*y1 - y2

def lucro1(y1,y2,cf1,cv1):
	return rec1(y1,y2) - custo1(cf1,cv1,y1)

def max_y1(miny1,maxy1,y2,cf1,cv1):
	y = np.linspace(miny1,maxy1)

	data = pd.DataFrame()
	data['q1'] = y
	data['p1'] = p1(y,y2)
	data['rec1'] = rec1(y,y2)
	data['rma1'] = rma1(y,y2)
	data['custo1'] = custo1(cf1,cv1,y)
	data['lucro1'] = lucro1(y,y2,cf1,cv1)
	
	return data[data['lucro1'] == max(data['lucro1'])][['q1','p1','lucro1']]

# Parte 2 - Função que retorna p2 e q2 que maximiza o lucro do monopolista
def p2(y1,y2):
	return 100 - y2 - y1

def rec2(y1,y2):
	return p2(y1,y2) * y2

def custo2(cf2,cv2,y2):
	return cf2 + cv2 * y2

def rma2(y1,y2):
	return 100 - 2*y2 - y1

def lucro2(y1,y2,cf2,cv2):
	return rec2(y1,y2) - custo2(cf2,cv2,y2)

def max_y2(miny2,maxy2,y1,cf2,cv2):
	y = np.linspace(miny2,maxy2)

	data = pd.DataFrame()
	data['q2'] = y
	data['p2'] = p2(y1,y)
	data['rec2'] = rec2(y1,y)
	data['rma2'] = rma2(y1,y)
	data['custo2'] = custo2(cf2,cv2,y)
	data['lucro2'] = lucro2(y1,y,cf2,cv2)
	
	return data[data['lucro2'] == max(data['lucro2'])][['q2','p2','lucro2']]

#####################################################################################################
# Montando o banco de dados
#####################################################################################################
y_min = 0
y_max = 100
data = pd.DataFrame(np.zeros([y_max,y_max]))
data['q1'] = range(y_min,data.shape[0])

i = 0
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
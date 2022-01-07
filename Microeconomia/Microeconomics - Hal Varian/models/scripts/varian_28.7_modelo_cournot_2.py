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
a = 100
b = 2

def f_reac1(y1):
	return (a - 2*b*y1)/(b)

def lucro1(y1,y2):
	return ((a - b*y2)*y1)/(2*b)

def f_reac2(y1):
	return (a - b*y1)/(2*b)

def lucro2(y1,y2):
	return ((a - b*y1)*y2)/(2*b)

#####################################################################################################
# Gerando o gráfico - fonte: https://www.geeksforgeeks.org/contour-plot-using-matplotlib-python/
#####################################################################################################

fig = plt.figure(dpi=120)
ax = plt.axes()
ax.grid(color='gray',linewidth=.2)

q1 = np.linspace(0,50,100)
q2 = np.linspace(0,50,100)

ax.set_title('cap 28.7 - Ajustamento')
ax.set_xlabel('Qtd Empresa 1')
ax.set_ylabel('Qtd Empresa 2')

plt.plot(q1, f_reac2(q1),'-',color='red', label='Reação Empresa 2')
plt.plot(q1, f_reac1(q2),'-',color='blue', label='Reação Empresa 1')

# adding points with a label
coord = [40,5]
plt.plot(coord[0],coord[1],marker='.',color='white')
label = '  Cesta (t)'
plt.annotate(label,(coord[0],coord[1]))

coord = [22.5,5]
plt.plot(coord[0],coord[1],marker='.',color='white')
label = '  Cesta (t+1)'
plt.annotate(label,(coord[0],coord[1]))

coord = [22.5,14]
plt.plot(coord[0],coord[1],marker='.',color='white')
label = '  Cesta (t+2)'
plt.annotate(label,(coord[0],coord[1]))

coord = [22.5,14]
plt.plot(coord[0],coord[1],marker='.',color='white')
label = '  Cesta (t+2)'
plt.annotate(label,(coord[0],coord[1]))

coord = [18,14]
plt.plot(coord[0],coord[1],marker='.',color='white')

coord = [18,16]
plt.plot(coord[0],coord[1],marker='.',color='white')

coord = [17,16]
plt.plot(coord[0],coord[1],marker='.',color='white')

coord = [16.7,16.7]
plt.plot(coord[0],coord[1],marker='.',color='white')


# Movement arrows
ax.annotate("", xy=(22.5, 5), xytext=(40, 5),arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(22.5,14), xytext=(22.5,5),arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(18,14), xytext=(22.5,14),arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(18,16), xytext=(18,14),arrowprops=dict(arrowstyle="-"))
ax.annotate("", xy=(17,16), xytext=(18,16),arrowprops=dict(arrowstyle="-"))

# Text
coord = [32,20]
plt.plot(coord[0],coord[1],marker='',color='white')
label = 'Empresa 01:\nOk, estou satisfeito. \n\nEmpresa 02:\nOk, estou satisfeito.'
plt.annotate(label,(coord[0],coord[1]))

plt.xlim(0)
plt.ylim(0)
plt.legend(loc='upper right')
plt.show()
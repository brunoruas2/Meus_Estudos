# Modulos usados
import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import tabloo # to see the df

from PIL import Image
from mpl_toolkits import mplot3d
from mpl_toolkits.axes_grid1 import host_subplot

pd.options.mode.chained_assignment = None  # default='warn'

plt.style.use('dark_background')

#####################################################################################################
# Funções usadas no modelo
#####################################################################################################
# funcoes de utilidade
def fu_a(x1,x2,a,b):
	return (x1**a)*(x2**b)

def fu_b(x1,x2,a,b):
	return (x1**a)*(x2**b)

#####################################################################################################
# Gerando o gráfico - fonte: https://pythontic.com/image-processing/pillow/blend
#####################################################################################################
max_val = 100
q1 = np.linspace(0,max_val,100)
q2 = np.linspace(0,max_val,100)

# graph

fig = plt.figure(dpi=120)
ax = host_subplot(111)
ax.grid(color='gray',linewidth=.2)

ax.set_title('cap 32.1 - Caixa de Edgeworth\n')
ax.set_xlabel('Bem 1')
ax.set_ylabel('Bem 2')

# Creating 2-D grid of features
[X, Y] = np.meshgrid(q1, q2)
  
# plots contour lines
Z1 = fu_a(X,Y,0.5,0.5)
CL1 = ax.contour(X, Y, Z1, colors="red", levels = range(10,1000,10)) # , cmap="winter"
ax.clabel(CL1, inline=1, fontsize=10)

ax.yaxis.tick_left()
ax.yaxis.set_ticks_position('both')
ax.xaxis.tick_bottom()
ax.xaxis.set_ticks_position('both') # THIS IS THE ONLY CHANGE

plt.xlim(0,100)
plt.ylim(0,100)

ax = host_subplot(111)
ax.grid(color='gray',linewidth=.2)

Z2 = fu_b(X,Y,0.5,0.5)
CL2 = ax.contour(X, Y, Z2, colors="cyan", levels = range(10,1000,10)) # , cmap="winter"
ax.clabel(CL2, inline=1, fontsize=10)

ax.yaxis.tick_right()
ax.yaxis.set_ticks_position('both')
ax.xaxis.tick_top()
ax.xaxis.set_ticks_position('both') # THIS IS THE ONLY CHANGE

plt.xlim(100,0)
plt.ylim(100,0)

#plt.legend(loc='upper left')
plt.savefig('img2.png', transparent=True)

## merge images
# Take two images for blending them together   
image1 = Image.open("img1.png")
image2 = Image.open("img2.png")

# alpha-blend the images with varying values of alpha
alphaBlended1 = Image.blend(image1, image2, alpha=1)

# Display the alpha-blended images
alphaBlended1.save(r'C:\Users\bruno\Documents\Metadata\Meus_Estudos\Microeconomia\Microeconomics - Hal Varian\images\cap31_1-caixa_edgeworth.png')

os.remove('img2.png')
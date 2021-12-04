### Universidade do Estado do Amazonas - UEA (Microeconomia II)
## Modelo de Otimização da Receita do Monopólio com uma Demanda linear
# Varian página 632

# Modulos usados
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('dark_background')

# Constantes usadas:
a = 100
b = 5

# Sistema de Equações:
# Curva de Demanda Linear -> p(y) = a - by #
# Função Receita -> r(y) = p(y)y = ay - by^2
# Função Receita Marginal -> RM(y) = a - 2by

# Modelo
y = np.linspace(0,100,1000)

dem_lin = a - b * y
receita = a * y - b * (y ** 2)
rec_marg = a - 2*b*y

dataframe = pd.DataFrame()
dataframe['quant'] = y
dataframe['dem_lin'] = dem_lin
dataframe['receita'] = receita
dataframe['rec_marg'] = rec_marg


# Gerando o gráfico
fig = plt.figure(dpi=120)
ax = plt.axes()
ax.grid(color='gray',linewidth=.2)

plt.plot(dataframe['quant'], dataframe['dem_lin'],'-',color='red', label='Demanda')
plt.plot(dataframe['quant'], dataframe['rec_marg'],'-',color='blue', label='Receita Marginal')
#plt.plot(dataframe['quant'], dataframe['receita'],'-',color='green', label='Receita')

plt.ylim(0,max(dataframe['dem_lin']))
plt.xlim(0,a/b)
plt.legend(loc='upper right')
plt.show()

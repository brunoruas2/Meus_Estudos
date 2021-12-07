### Universidade do Estado do Amazonas - UEA (Microeconomia II)
## Modelo de Otimização da Receita do Monopólio com uma Demanda com Elasticidade Constante
# Varian página 634

# Modulos usados
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from math import inf

pd.options.mode.chained_assignment = None  # default='warn'

plt.style.use('dark_background')

# Sistema de Equações:
# Curva de Demanda Inversa com Elasticidade Constante -> p(y) = (k/y)^(1/alpha)
# Função Receita -> r(y) = p(y)y = ay - by^2
# Função Receita Marginal -> RM(y) = a - 2by
# Função Custo Total -> c(y) = CF + 5*CV*y + (CV*y^3)/3
# Função Custo Marginal -> CMa(y) = CV

# Constantes usadas nas equações:
alpha = 5
k = 100000000
CF = 150 # custo fixo
CV = 1 # custo variavel

# Modelo
y = np.linspace(0.01,100,1000)

dem_ces = (k/y)**(1/alpha)
receita = dem_ces*y
rec_marg = ((alpha - 1)/(alpha))*(y**(-1/alpha))*(k**(1/alpha))
custo_total = CF + 5*CV*y + (CV*y**3)/3
custo_medio = custo_total / y
custo_marginal = 5*CV + CV*y**2
lucro = receita - custo_total

dataframe = pd.DataFrame()
dataframe['quant'] = y
dataframe['dem_ces'] = dem_ces
dataframe['receita'] = receita
dataframe['rec_marg'] = rec_marg
dataframe['custo_total'] = custo_total
dataframe['custo_medio'] = custo_medio
dataframe['custo_marginal'] = custo_marginal
dataframe['lucro'] = lucro

dataframe.to_excel('teste.xlsx')

# Gerando o gráfico
fig = plt.figure(dpi=120)
ax = plt.axes()
ax.grid(color='gray',linewidth=.2)

plt.subplot(2,1,1) # rows, columns, panel number

plt.title('cap 25.2 - Demanda Linear e Monopólio')

plt.plot(dataframe['quant'], dataframe['dem_ces'],'-',color='red', label='Demanda')
plt.plot(dataframe['quant'], dataframe['rec_marg'],'-',color='blue', label='Receita Marginal')
plt.plot(dataframe['quant'], dataframe['custo_medio'],'-',color='green', label='Custo Medio')
plt.plot(dataframe['quant'], dataframe['custo_marginal'],'-',color='white', label='CMa')
plt.legend(loc='upper right')
plt.ylim(0,max(dataframe['dem_ces'].iloc[1:10]))
plt.xlim(0,max(dataframe['dem_ces'].iloc[1:10]))

plt.subplot(2,1,2) # rows, columns, panel number
plt.plot(dataframe['quant'], dataframe['lucro'],'--',color='white', label='Lucro')
plt.plot(dataframe['quant'], dataframe['custo_total'],'--',color='blue', label='Custo Total')
plt.plot(dataframe['quant'], dataframe['receita'],'--',color='red', label='Receita')
plt.legend(loc='upper right')
plt.ylim(0,max(dataframe['receita'].iloc[1:dataframe.shape[0]]))
plt.xlim(0,max(dataframe['dem_ces'].iloc[1:10]))

plt.show()

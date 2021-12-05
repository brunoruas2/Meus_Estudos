### Universidade do Estado do Amazonas - UEA (Microeconomia II)
## Modelo de Otimização da Receita do Monopólio com uma Demanda linear
# Varian página 632

# Modulos usados
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None  # default='warn'

plt.style.use('dark_background')

# Constantes usadas:
a = 100
b = 5
CF = 200 # custo fixo
CV = 10 # custo variavel

# Sistema de Equações:
# Curva de Demanda Linear -> p(y) = a - by #
# Função Receita -> r(y) = p(y)y = ay - by^2
# Função Receita Marginal -> RM(y) = a - 2by
# Função Custo Total -> c(y) = CF + CV*y
# Função Custo Marginal -> CMa(y) = CV

# Modelo
y = np.linspace(0,100,1000)

dem_lin = a - b * y
receita = a * y - b * (y ** 2)
rec_marg = a - 2*b*y
custo_total = CF + CV*y
custo_medio = CF / y
custo_marginal = CV
lucro = receita - custo_total

dataframe = pd.DataFrame()
dataframe['quant'] = y
dataframe['dem_lin'] = dem_lin
dataframe['receita'] = receita
dataframe['rec_marg'] = rec_marg
dataframe['custo_total'] = custo_total
dataframe['custo_medio'] = custo_medio
dataframe['custo_marginal'] = custo_marginal
dataframe['lucro'] = lucro

# Gerando o gráfico
fig = plt.figure(dpi=120)
ax = plt.axes()
ax.grid(color='gray',linewidth=.2)


plt.subplot(2,1,1) # rows, columns, panel number

plt.title('cap 25.2 - Demanda Linear e Monopólio')

plt.plot(dataframe['quant'], dataframe['dem_lin'],'-',color='red', label='Demanda')
plt.plot(dataframe['quant'], dataframe['rec_marg'],'-',color='blue', label='Receita Marginal')
plt.plot(dataframe['quant'], dataframe['custo_medio'],'-',color='green', label='Custo Medio')
plt.plot(dataframe['quant'], dataframe['custo_marginal'],'-',color='white', label='CMa')
plt.legend(loc='upper right')
plt.ylim(0,max(dataframe['dem_lin']))
plt.xlim(0,a/b)

plt.subplot(2,1,2) # rows, columns, panel number
plt.plot(dataframe['quant'], dataframe['lucro'],'--',color='white', label='Lucro')
plt.plot(dataframe['quant'], dataframe['custo_total'],'--',color='blue', label='Custo Total')
plt.plot(dataframe['quant'], dataframe['receita'],'--',color='red', label='Receita')
plt.legend(loc='upper right')
plt.ylim(0,max(dataframe['receita']))
plt.xlim(0,a/b)

plt.show()

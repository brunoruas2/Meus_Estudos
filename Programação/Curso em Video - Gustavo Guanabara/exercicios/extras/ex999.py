# rodar um dado 1000 vezes
import random

# media de n numeros
n = 'start'

result = []
for j in range(0,100):
  print(j)
  for i in range(0,1000):
    if n == 'start':
      n = random.randint(1,6)
      qtd = 1
    else:
      n = random.randint(1,6) + n
      qtd = qtd + 1  
  result = result.append(n/qtd)


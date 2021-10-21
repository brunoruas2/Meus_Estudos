# media de n numeros
cont = 'yes'
n = 'start'
while cont == 'yes':
  if n == 'start':
    n = float(input('Insira o primero número \n '))
    qtd = 1
  else:
    test = input('Escolha: \n a - Inserir mais um número \n b - Calcular a média \n ')
    if test == 'a':
      n = float(input('Insira um número \n ')) + n
      qtd = qtd + 1
    if test == 'b':
      print('A média dos valores é igual a {}'.format(n/qtd))
      break

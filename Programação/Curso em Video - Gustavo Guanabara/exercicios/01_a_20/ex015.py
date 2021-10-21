# calculo do preço do aluguel do carro
dias = int(input('quantos dias? \n'))
km = float(input('quantos km? \n'))

preco = 60*dias + 0.15*km

print('O valor a ser pago é de R${:.2f}'.format(preco))
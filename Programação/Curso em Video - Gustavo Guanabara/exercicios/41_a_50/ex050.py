# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma 
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for i in range(0,6):
	num = int(input('Escolha um número inteiro {}/6: '.format(i+1)))
	if num % 2 == 0:
		soma += num
		cont += 1
	else:
		pass

print('A soma dos {} números pares é {}'.format(cont,soma))
# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 

num = int(input('Digite um número: '))

cont = 0
for i in range(1,num+1):
	if num % i == 0:
		print("{} ".format(i),end='')
		cont += 1

if cont > 2:
	print("Não é Primo",end='')
else:
	print("É Primo",end='')

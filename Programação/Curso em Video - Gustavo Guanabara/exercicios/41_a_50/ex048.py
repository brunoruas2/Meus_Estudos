# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são
#  múltiplos de três e que se encontram no intervalo de 1 até 500.

num = 0
n_num = 0

for i in range(3,501,3):
	if i % 2 > 0:
		num = num + i
		n_num = n_num + 1
	else:
		pass

print('A soma dos {} números é igual a {}'.format(n_num,num))

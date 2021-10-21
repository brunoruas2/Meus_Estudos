# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
#  e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal. 

import numpy as np

numero = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão')
print('[ 1 ] Binário')
print('[ 2 ] Octal')
print('[ 3 ] Hexadecimal')
opcao = int(input("Qual sua opção? "))

if opcao == 1:
	print('Conversão igual a {}'.format(bin(numero)[2:]))
elif opcao == 2:
	print('Conversão igual a {}'.format(oct(numero)[2:]))
elif opcao == 3:
	print('Conversão igual a {}'.format(hex(numero)[2:]))
else:
	print('Opção inválida')
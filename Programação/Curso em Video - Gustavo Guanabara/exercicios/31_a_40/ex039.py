# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com
#  a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já
#  passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year

ano = int(input('Qual o ano do nascimento? '))
idade = atual - ano

sexo = input('Qual seu sexo? [M ou F] ')

print("Quem nasceu em {} tem {} anos em 2021".format(ano,idade))

if sexo == 'M':
	if ano < 2003: # passou o prazo
		print("Você deveria ter se alistado há {} anos".format(idade-18))
		print('Seu alistamento foi em {}'.format(ano+18))
	elif ano == 2003: # no ano correto
		print("Você tem 18 anos em 2021")
		print("Está na hora de se alistar!")
	else: # ainda nao chegou o prazo
		print("Ainda faltam {} anos para o seu alistamento".format(18-idade))
		print('Seu alistamento será em {}'.format(ano+18))
else:
	print('Mulheres não precisam se alistar')
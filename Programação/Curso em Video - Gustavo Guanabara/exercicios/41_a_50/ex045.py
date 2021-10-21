# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import time
import random

opcoes = ['Pedra','Papel','Tesoura']

cpu = random.randint(0,3)

player = int(input(''' Escolha uma opção:
[0] Pedra
[1] Papel
[2] Tesoura
'''))

print('='*20)
print('JO-')
time.sleep(1)
print('KEN-')
time.sleep(1)
print('PO!')
print('='*20)

if player not in [0,1,2]:
	print('Jogada inválida')
elif cpu == player:
	resultado = 'EMPATE!'
elif (cpu == 0 and player == 2) or (cpu == 1 and player == 0) or (cpu == 2 and player == 1):
	resultado = 'CPU VENCE!'
else:
	resultado = 'PLAYER VENCE!'

if player in [0,1,2]:
	cpu = opcoes[cpu]
	player = opcoes[player]
	print('''CPU = {}\nPLAYER = {}\n{} '''.format(cpu,player,resultado))

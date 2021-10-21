# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

print("="*25)
print('10 TERMOS DE UMA PA')
print("="*25)

termo = int(input('Primeiro termo: '))
razao = int(input('razao: '))

for i in range(0,10):
	print("{} -> ".format(termo + i*razao),end='')

print("ACABOU")
# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o 
# estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time

for i in range(11,1,-1):
	print(i-1)
	time.sleep(1)

print("BUM BUM POOW")
# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# disclaimer -> aqui eu usei uma abordagem para string, na resolucao o professor foi pra manipulacao de interger

numero = input('Informe um número entre 0 e 9999: ').zfill(4) # colocando zeros a esquerda do input

print('Unidade: {}'.format(numero[len(numero)-1:len(numero)]))
print('Dezena: {}'.format(numero[len(numero)-2:len(numero)-1]))
print('Centena: {}'.format(numero[len(numero)-3:len(numero)-2]))
print('Milhar: {}'.format(numero[len(numero)-4:len(numero)-3]))



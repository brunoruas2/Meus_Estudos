# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input('Qual seu nome? ')
nome = nome.upper()

print('Seu nome tem Silva? '+ str(nome.find('SILVA') != -1))
# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Me diga um número qualquer: '))

if num % 2 != 0:
  print("O número é ímpar!")
else:
  print("O número é par!")
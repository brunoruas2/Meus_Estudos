# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# dei uma roubadinha https://pt.wikipedia.org/wiki/Ano_bissexto

ano = int(input("Insira um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
  print("ano bissexto")
else:
  print('não bissexto20')
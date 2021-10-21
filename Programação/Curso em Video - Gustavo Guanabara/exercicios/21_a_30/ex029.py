# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

veloc = float(input('Qual a velocidade atual do carro? '))

if veloc <= 80:
  print('Tenha um bom dia! Dirija com segurança!')
else:
  print('Você ultrapassou o limite de velocidade. O valor da multa é de R$ {:.2f}'.format((veloc-80)*7))
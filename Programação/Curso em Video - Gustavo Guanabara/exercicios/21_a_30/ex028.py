# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número
#  inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido 
# pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import time
import random

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Vou pensar em um número entre0 e 5. Tente advivinhar...')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

num = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
time.sleep(2)

new = random.randint(0,5)

if num == new:
  print('Parabéns!')
else:
  print('Melhor sorte na próxima. Eu pensei em {}'.format(new))

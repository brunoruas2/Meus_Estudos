# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao 
# usuário se elas podem ou não formar um triângulo.

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

t1 = abs(b - c) < a < b + c
t2 = abs(a - c) < b < a + c
t3 = abs(a - b) < c < a + b

if t1 == t2 == t3 == True:
  print('Dá pra fazer um triângulo')
else:
  print('Não da pra fazer um triângulo')
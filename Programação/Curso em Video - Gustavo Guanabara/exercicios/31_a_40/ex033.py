# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('numero 1: '))
n2 = float(input('numero 2: '))
n3 = float(input('numero 3: '))

vetor = [n1,n2,n3]

print('O menor número é {}'.format(min(vetor)))
print('O maior número é {}'.format(max(vetor)))
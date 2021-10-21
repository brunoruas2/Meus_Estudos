#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ').strip()

print('Analisando seu nome...')
print('Seu nome em {} é {}'.format('Maiúsculas',nome.upper()))
print('Seu nome em {} é {}'.format('Minúsculas',nome.lower()))
print('Seu nome tem {} letras ao todo'.format(len(nome.replace(' ',''))))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.split()[0],len(nome.split()[0])))
# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando 
# em seguida o primeiro e o último nome separadamente. 

# nome = input('Qual seu nome? ').strip().upper()
nome = "BRUNO DE MELO RUAS"

nome = nome.split()

print('Seu primeiro nome é {}'.format(nome[0].capitalize()))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

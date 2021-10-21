# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes 
# aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a 
# última vez.

frase = input('Digite uma Frase: ').strip()
frase = frase.upper()

# tive que roubar, eu nao consegui pensar em uma maneira de usar o 'find' ao contrário para 
# procurar a última vez que a letra 'a' aparece
def cont_back(string,letter):
  i = 0
  while letter != string[len(string)-i:len(string)+1][0:1]:
    i = i + 1
  return len(frase) - i 

print('A letra "a" aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra "a" apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra "a" apareceu na posição {}'.format(cont_back(frase,'A')+1))


# SOLUCAO DO PROFESSOR! 'str.find' permite a lógica str.rfind (right find!)
print('A ultima letra "a" apareceu na posição {}'.format(frase.rfind('A')+1))


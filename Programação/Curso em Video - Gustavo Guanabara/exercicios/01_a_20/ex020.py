# ordenando uma lista

from random import sample

n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')

vetor = [n1,n2,n3,n4]

print("O aluno sorteado é {}".format(sample(vetor,4)))

# outro jeito de fazer isso é usando a funcao shuffle
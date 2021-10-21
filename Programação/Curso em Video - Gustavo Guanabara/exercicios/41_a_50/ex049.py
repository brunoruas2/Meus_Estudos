# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
# só que agora utilizando um laço for.

num = int(input('Qual o número? '))

print('-'*12)
for i in range(1,11):
  print('{} x {:2} = {}'.format(num,i,(i*num)))
print('-'*12)

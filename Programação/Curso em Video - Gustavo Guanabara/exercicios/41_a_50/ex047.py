# Exercício Python 47: Crie um programa que mostre na tela todos os números pares que
#  estão no intervalo entre 1 e 50. 

string = ''
i = 2

for i in range(1,51):
	if i % 2 == 0:
		string = string + "{} ".format(i)
	else:
		pass

print(string + 'acabou')

# ou
for i in range(2,51,2):
	if i % 2 == 0:
		print("{}".format(i),end=' ')

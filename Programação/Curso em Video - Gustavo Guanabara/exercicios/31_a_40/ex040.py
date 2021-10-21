# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))

media = (n1 + n2) / 2

if media <= 5: 
	print('reprovado com média {:.2f}'.format(media))
elif media >= 7:
	print('aprovado com média {:.2f}'.format(media))
else:
	print('recuperação com média {:.2f}'.format(media))
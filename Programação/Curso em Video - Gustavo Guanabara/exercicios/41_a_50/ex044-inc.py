# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

print('=-'*10)
print('Lojas Guanabara')
print('=-'*10)

preco = float(input('Qual o preço? '))

forma = int(input(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais
Qual opção? 
'''))

if forma == 1:
	print('preço R$ {}'.format(preco*0.9))
elif forma ==2:
		print('preço R$ {}'.format(preco*0.95))
elif forma ==2:
		print('preço R$ {}'.format(preco*0.95))
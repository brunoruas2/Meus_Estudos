# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário? R$'))
anos = int(input('Quantos anos? '))

print('Para pagar R${:.2f} em {} anos. A mensalidade é de {:.2f}'.format(valor,anos,valor/(12*anos)))

if valor/(12*anos) > salario*0.3:
	print('Empréstimo NEGADO')
else:
	print('Empréstimo LIBERADO') 
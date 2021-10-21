# calculo do desconto de um produto 5%

preco = float(input('Qual o preço? \n'))
desconto = float(input('Qual o desonto (%)? \n'))

print("O preço do produto é {:.2f}, com o desconto de {} % o novo valor será {:.2f}".format(preco,desconto,preco*(1-desconto/100)))
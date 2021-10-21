# programa pra pintar paredes 2m^2 = 1l de tinta

larg = float(input('Qual a largura? \n '))
alt = float(input('Qual a altura? \n'))

area = larg * alt

print('A parede tem dimensão {:.2f} x {:.2f} e área de {:.2f} m²'.format(larg,alt,area))
print('Vai ser necessário um total de {:.2f} litros de tinta'.format(area/2))
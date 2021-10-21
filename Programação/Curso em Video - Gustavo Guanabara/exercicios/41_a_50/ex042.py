# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
#  que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes 

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

t1 = abs(b - c) < a < b + c
t2 = abs(a - c) < b < a + c
t3 = abs(a - b) < c < a + b

# tive que roubar um pouco. Criei uma funcao que retorna uma string com o tipo do triangulo
def type_triangle(a,b,c):
	if a == b == c:
		return 'Triângulo EQUILÁTERO'
	elif a != b and a != c and b != c:
		return 'Triângulo ESCALENO'
	elif a == b or a == c or b == c:
		return 'Triângulo ISÓSCELES'

if t1 == t2 == t3 == True:
  print('Dá pra fazer um triângulo. Esse triangulo é um {}'.format(type_triangle(a,b,c)))
else:
  print('Não da pra fazer um triângulo')

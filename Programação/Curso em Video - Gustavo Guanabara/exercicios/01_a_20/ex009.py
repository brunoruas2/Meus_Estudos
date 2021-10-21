# programa que pegue um int e mostre a tabuada dele

num = int(input('Qual o número? '))

i = 0
while i <= 10:
  print('{} x {:2} = {}'.format(num,i,(i*num)))
  i = i + 1
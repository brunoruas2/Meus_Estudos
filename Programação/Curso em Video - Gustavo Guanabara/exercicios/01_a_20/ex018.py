# seno cosseno e tangente de um angulo qualquer

from math import sin,cos,tan,radians

ang = radians(float(input('angulo: '))) # converte graus em radianos

print('o seno é: {:.2f}'.format(sin(ang)))
print('o cosseno é: {:.2f}'.format(cos(ang)))
print('a tangente é: {:.2f}'.format(tan(ang)))
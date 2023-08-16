from math import sin, cos, tan, radians
angulo = int(input('Digite um ângulo: '))
angulo = radians(angulo)
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print(f'O seno deste ângulo é: {seno:.2f}')
print(f'O cosseno deste ângulo é: {cosseno:.2f}')
print(f'O tangente deste ângulo é: {tangente:.2f}')
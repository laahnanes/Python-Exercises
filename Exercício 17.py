from math import hypot
nco = float(input('Digite o valor do cateto oposto: '))
nca = float(input('Digite o valor do cateto adjacente: '))
resul = hypot(nco, nca)
print(f'O valor da hipotenusa é de: {resul:.2f}')
frase = input('Digite uma frase: ').strip().upper()
print('A letra A aparece',frase.count('A'), 'vezes na frase.')
print('A primeira letra A apareceu na posição', frase.find('A') + 1)
print('A última letra A apareceu na posição', frase.rfind('A') + 1)
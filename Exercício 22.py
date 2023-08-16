nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiusculo: {nome.upper()}')
print(f'Seu nome em minusculo: {nome.lower()}')
print('Seu nome tem:', len(nome) - nome.count(' '), 'letras')
nome = nome.split()
pri = nome[0]
print(f'Seu primeiro nome tem:', len(pri), 'letras')

#Faça um programa que leia algo e diga o maior número de informações sobre elas:
algo = input('Digite algo: ')
print(f'O tipo primitivo de {algo} é {type(algo)}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um número {algo.isnumeric()}!')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print((f'Está em minúsculas? {algo.islower()}'))
print(f'Está capitalizada {algo.istitle()}')

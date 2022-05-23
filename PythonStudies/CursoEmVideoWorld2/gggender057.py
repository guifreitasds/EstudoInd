# Leitor de generos com while

g = str(input('Digite seu genero [M/F]: ')).strip().upper()
while g not in 'MmFf':
    print('\033[31mErro de digitação,\033[m',end=' ')
    g = str(input('Digite seu genero novamente [M/F]: ')).strip().upper()
print(f'Sexo {g} registrado com sucesso!')

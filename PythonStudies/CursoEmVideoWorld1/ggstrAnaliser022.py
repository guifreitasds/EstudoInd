# Analisador de String
name = str(input('Digite seu nome completo: ')).strip()
splitted = name.split()


print('Todas letras maiusculas = {}'.format(name.upper()))
print('Todas letras minusculas = {}'.format(name.lower()))
print('A quantidade de letras é = {}'.format(len(name) - name.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(splitted[0], len(splitted[0])))


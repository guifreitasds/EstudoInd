# Conversor para Binário, octal, hexadecimal

number = int(input('Digite um número: '))
menu = int(input('Escolha a conversão\n [ 1 ] - Binário\n [ 2 ] - Octal\n [ 3 ] - Hexadecimal'))

if menu == 1:
    print(f'O número {number} em binário é {bin(number)[2:]}')
elif menu == 2:
    print(f'O número {number} em octal é {oct(number)[2:]}')
elif menu == 3:
    print(f'O número {number} em hexadecimal é {hex(number)[2:]}')
else:
    print('Opção inválida')
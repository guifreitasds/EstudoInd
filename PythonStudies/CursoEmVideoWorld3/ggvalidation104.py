def leiaInt(n):
    while True:
        try:
            number = int(input(n))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO, Digite um número inteiro valido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar\033[m')
            return 0
        else:
            return number


def leiaFloat(n):
    while True:
        try:
            number = float(input(n))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO, Digite um número inteiro valido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar\033[m')
            number = 0
            return number
        else:
            break
    return number

# main
#n = leiaInt('Digite um número: ')
#print(f'Você acabou de digitar o número {n}')
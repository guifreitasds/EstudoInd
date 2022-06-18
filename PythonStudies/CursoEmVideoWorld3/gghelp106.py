from time import sleep
def ajuda():
    while True:
        print('\033[44m')
        escreva('Sistema de ajuda PyHelp')
        print('\033[m')
        n = str(input('Função ou Biblioteca > ')).lower()
        if n == 'fim':
            print('\033[42m')
            escreva('<VOLTE SEMPRE>')
            print('\033[m')
            break
        print(f'Procurando a função {n}...\033[41m')
        sleep(1)
        help(n)
        print('\033[m')
def escreva(phrase):
    print('~'*(len(phrase)+4))
    print(f'  {phrase}')
    print('~'*(len(phrase)+4))


ajuda()
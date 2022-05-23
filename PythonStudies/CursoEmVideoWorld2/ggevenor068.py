# Par ou impar com computador
from random import randint
cont = n = 0
# Bloco While com escolhas do usuário + resolução do jogo
while True:
    n = int(input('Vamos Jogar! Digite seu número: '))
    comp = randint(0, 10)
    u = str(input('Escolha Par ou Impar [P/I]: ')).upper()
    soma = n + comp
    if soma % 2 == 0 and u == 'P':
        print('VOCÊ GANHOU, PARABÉNS!!!')
        print(f'Você escolheu {n} e o computador escolheu {comp}, a soma é {soma} que é um número par!')
        cont += 1
    elif soma % 2 == 1 and u == 'I':
        print('VOCÊ GANHOU, PARABÉNS!!!')
        print(f'Você escolheu {n} e o computador escolheu {comp}, a soma é {soma} que é um número ímpar!')
        cont += 1
    else:
        break
print(f'VOCÊ PERDEU, o computador escolheu {comp}, você ganhou o total de {cont} jogos')

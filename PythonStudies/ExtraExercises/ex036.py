from basiclibs.numeros import leiaFloat, leiaInt, simple_calculator

print('--------------CALCULADORA SIMPLES--------------')
n1 = leiaFloat('Digite o primeiro valor: ')
n2 = leiaFloat('Digite o segundo valor: ')

operation = leiaInt('Digite a operação: [1-Soma // 2-Subtração // 3-Multiplicação // 4-Divisão]')

res = simple_calculator(n1, n2, operation)

print(f'O resultado da operação é: {res}')
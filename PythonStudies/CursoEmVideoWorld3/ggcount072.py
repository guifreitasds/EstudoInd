contagem = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número entre 0 e 20 para ver ele por extenso: '))
while n < 0 or n > 20:
    n = int(input('Tente novamente, Digite um número entre 0 e 20 para ver ele por extenso: '))

print(f'Você digitou o número {contagem[n]}')
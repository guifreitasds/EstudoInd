from math import sqrt

# Code to discover the double, triple and square root of a number

n1 = int(input('Digite um número: ')) # request of the number to the user

db = n1 * 2 # double variable
tp = n1 * 3 # triple variable
sr = sqrt(n1) # square root variable

print('O dobro de {} é {}'.format(n1, db)) # print do dobro com format
print('O triplo de {} é {}'.format(n1, tp)) # print do triplo com format
print('A raiz quadrada de {} é {:.2f}'.format(n1, sr)) # print da raiz com format e com formatação das casas decimais

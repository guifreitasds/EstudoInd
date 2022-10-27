from basiclibs.numeros import *

n1 = leiaFloat('Digite a primeira nota: ')
n2 = leiaFloat('Digite a segunda nota: ')

media = (n1+n2)/2
con = ''
situ = ''
if media >= 9:
    con = 'A'
    situ = 'Aprovado'
if 7.5 <= media < 9:
    con = 'B'
    situ = 'Aprovado'
if 6.0 <= media < 7.5:
    con = 'C'
    situ = 'Aprovado'
if 4 <= media < 6:
    con = 'D'
    situ = 'Reprovado'
if media < 4:
    con = 'E'
    situ = 'Reprovado'

print(f'{n1} + {n2} forma uma média {media} com nota {con} // Situação: {situ}')
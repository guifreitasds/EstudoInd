from basiclibs.numeros import leiaFloat

n1 = leiaFloat('Digite a 1a nota: ')
n2 = leiaFloat('Digite a 2a nota: ')

media = (n1 + n2) / 2

if media >= 7 and media < 10:
    print('Aluno aprovado')
elif media < 7:
    print('Aluno reprovado!')
elif media == 10:
    print('Aluno aprovado com distinção!')
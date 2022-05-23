# Leitor de Pessoas

maiores = wminor = mans = cont = 0

while True:
    conf = ' '
    s = ' '
    while conf not in 'SN':
        conf = str(input('Deseja inserir uma nova pessoa? [S/N] ')).upper().strip()[0]
    if conf == 'N':
        break
    elif conf == 'S':
        cont += 1
        a = int(input('Digite a idade da pessoa: '))
        while s not in 'FM':
            s = str(input('Digite o sexo da pessoa [F/M]: ')).upper().strip()[0]
        if a >= 18:
            maiores += 1
        if s == 'M':
            mans += 1
        if s == 'F' and a < 20:
            wminor += 1

print(f'O total de pessoas maiores de idade é: {maiores}')
print(f'O total de Homens é: {mans}')
print(f'O total de mulheres com menos de 20 anos é: {wminor}')
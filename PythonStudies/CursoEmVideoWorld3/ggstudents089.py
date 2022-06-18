# Armazenador e verificador de notas
tot = []
name = []
grade = []

while True:
    n = str(input('Digite o nome do aluno: '))
    g1 = float(input('Digite a primeira nota do aluno: '))
    g2 = float(input('Digite a segunda nota do aluno: '))
    name.append(n)
    grade.append(g1)
    grade.append(g2)
    name.append(grade[:])
    tot.append(name[:])
    name.clear()
    grade.clear()
    u = str(input('Deseja adicionar mais alunos? [S/N] ')).strip().upper()[0]
    if u == 'N':
        break

for i in range(0, len(tot)):
    print(f'Aluno: {tot[i][0]} --> Média: {sum(tot[i][1])/2}')

while True:
    s = str(input('Gostaria de checar as notas de qual aluno? '))
    for a in range(0, len(tot)):
        if s in tot[a][0]:
            print(f'Notas do aluno(a) {s}: {tot[a][1]}')
    us = str(input('Deseja adicionar mais alunos? [S/N] ')).strip().upper()[0]
    if us == 'N':
        break




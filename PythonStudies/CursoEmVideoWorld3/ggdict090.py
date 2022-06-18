# Alunos com Dicionários

alunos = {}
alunos['nome'] = str(input('Digite o nome do aluno: '))
alunos['média'] = float(input(f'Digite a média de {alunos["nome"]}: '))
if alunos['média'] >= 7:
    alunos['situação'] = 'Aprovado'
elif 5 <= alunos['média'] < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'

for k, v in alunos.items():
    print(f'{k} é igual a {v}')
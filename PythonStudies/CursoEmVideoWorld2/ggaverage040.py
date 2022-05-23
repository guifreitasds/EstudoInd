# Resolução da Média do aluno

notas = []
print('\033[31m-=-\033[m' * 20)

for i in range(1, 5):
    n1 = float(input(f'\033[36mDigite a nota {i} do aluno: \033[m'))
    notas.append(n1)

average = sum(notas)/len(notas)

if average >= 7:
    print('\033[32mAluno aprovado!\033[m')
elif 5 < average < 7:
    print('\033[37mAluno em recuperação!\033[m')
else:
    print('\033[31mAluno reprovado!\033[m')
print('\033[31m-=-' *20)
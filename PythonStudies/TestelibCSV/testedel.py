# [IMPORTANDO LIB]
import csv

# [ABRINDO E LENDO O ARQUIVO DE INPUT]
with open('3ano.csv', 'r', encoding='utf-8') as ano:
    reader = csv.reader(ano)
    # [ARMAZENANDO A MATRIZ DOS DADOS EM UMA LISTA]
    dados = [linha for linha in reader]

# [ESCOLHENDO AS COLUNAS A SEREM PRESERVADAS]
col_desej = [dados[i][2] + ',' + dados[i][3] + ',' + dados[i][4] + ',' + dados[i][5] + ',' + dados[i][6] + ',' + dados[i][7] + ',' + dados[i][8] for i in range(len(dados))]


# [ABRINDO ARQUIVO PARA A ESCRITA]
with open('testewrite.csv', 'w', encoding='utf-8', newline='') as output:
    writer = csv.writer(output)
    # [CRIANDO LAÇO PARA A ESCRITA DAS COLUNAS COM TODAS AS LINHAS]
    for row in col_desej:
        writer.writerow(row.split(','))
# import csv
#
# with open('3ano.csv', 'r', encoding='utf-8') as ano:
#     reader = csv.reader(ano)
#     dados = [linha for linha in reader]
#
# col_desej = [dados[i][2] + ',' + dados[i][3] + ',' + dados[i][4] + ',' + dados[i][5] + ',' + dados[i][6] + ',' + dados[i][7] + ',' + dados[i][8] for i in range(len(dados))]
#
#
# with open('testewrite.csv', 'w', encoding='utf-8', newline='') as output:
#     writer = csv.writer(output)
#     for row in col_desej:
#         writer.writerow(row.split(','))
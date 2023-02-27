import csv

# mtall = []
# lctrl = []
# fieldnames = ['ID', 'TIPO_PIPOCA', 'QTD_PIPOCA', 'VALOR_PIPOCA', 'VALOR_TOTAL', 'DATA', 'HORÁRIO']
# with open('teste.csv', newline='', encoding='utf-8') as t:
#     reader = csv.reader(t, delimiter=',')
#     for i, row in enumerate(reader):
#         for a in range(0, len(fieldnames)):
#             lctrl.append(row[a])
#         mtall.append(lctrl)
#         lctrl = []
#         with open('testewrite.csv', 'w', newline='') as g:
#             writer = csv.DictWriter(g, fieldnames=fieldnames)
#             for a in range(0, len(mtall)):
#                 writer.writerow({f'ID': mtall[a][0], 'TIPO_PIPOCA': mtall[a][1], 'QTD_PIPOCA': mtall[a][2], 'VALOR_PIPOCA': mtall[a][3], 'VALOR_TOTAL': mtall[a][4], 'DATA': mtall[a][5],
#                 'HORÁRIO': mtall[a][6]})

# with open('teste.csv', 'r', encoding='utf-8') as t:
#     reader = csv.reader(t)
#     with open('testewrite.csv', 'w', newline='', encoding='utf-8') as g:
#         writer = csv.writer(g)
#         for row in reader:
#             if '{2}' in row:
#                 pass
#             else:
#                 writer.writerow(row)

# with open('teste.csv', 'r') as t:
#     reader = csv.reader(t)
#     with open('testewrite.csv', 'a', newline='') as g:
#         writer = csv.writer(g)
#         for row in reader:
#             writer.writerow(row)



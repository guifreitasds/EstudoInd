import csv



with open('teste.csv', newline='', encoding='utf-8') as t:
      reader = csv.reader(t, delimiter=',')
      for id, row in enumerate(reader):
        print(id, row)
#with open('teste.csv','w', newline='') as t:
#      fieldnames = ['ID', 'TIPO_PIPOCA', 'QTD_PIPOCA', 'VALOR_PIPOCA', 'VALOR_TOTAL', 'DATA', 'HORÁRIO']
#      writer = csv.DictWriter(t, fieldnames=fieldnames)
#      for i in range(0,5):
#          id+=1
#          tipo=1
#          writer.writerow({f'ID': id, 'TIPO_PIPOCA': 'Doce' if tipo==1 else 'Salgada', 'QTD_PIPOCA': 1, 'VALOR_PIPOCA': {3 if tipo==1 else 2}, 'VALOR_TOTAL': 3.00, 'DATA': 15,
#               'HORÁRIO': 16})


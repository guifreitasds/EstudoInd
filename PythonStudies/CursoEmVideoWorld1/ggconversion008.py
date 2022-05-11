# Conversão metros para ...

m = float(input('Digite uma medida em metros: '))

print('{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format((m/1000), (m/100), (m/10), (m*10), (m*100), (m*1000)))

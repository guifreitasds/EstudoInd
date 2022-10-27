from basiclibs.numeros import *

h = leiaInt('Quanto você recebe por hora trabalhada? ')
hd = leiaInt('Quantas horas você trabalha por dia? ')

bruto = (hd*30)*h
ir = bruto * 0.11
inss = bruto * 0.08
sindi = bruto * 0.05
liquid = bruto-ir-inss-sindi

print(f'''
+ Salário bruto: {bruto}
- IR: R${ir}
- INSS: R${inss}
- Sindicato: R${sindi}
= Salário Liquido: {liquid}''')
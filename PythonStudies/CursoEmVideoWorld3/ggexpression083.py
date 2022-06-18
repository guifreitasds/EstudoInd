expression = []

ex = str(input('Digite a expressão a ser verificada: '))
expression.append(ex)
contadordefech = 0
contadordeabr = 0
for cont,i in enumerate(expression[0]):
    if i == '(':
        contadordeabr += 1
    elif contadordeabr == 0 and i == ')':
        contadordefech += 1
for cont1, i1 in enumerate(expression[0]):
    if i1 == ')':
        contadordefech += 1
if contadordeabr == contadordefech:
    print('Expressão aceita!')
else:
    print('Expressão errada!')
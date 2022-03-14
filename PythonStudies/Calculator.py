# Tentativa de Calculadora

print('Vamos calcular?')

soma = 1
sub = 2
mult = 3
div = 4


number1 = float(input('Digite o primeiro número:'))
simbol = int(input('Digite o numero do sinal desejado! 1 = soma, 2 = subtração, 3 = multiplicação e 4 = divisão: '))
number2 = float(input('Digite outro número: '))

if(simbol == soma):
  finalresult = (number1 + number2)
  p = ('O resultado da soma é: ' + str(finalresult))
  print(p)
elif(simbol == sub):
  finalresult1 = (number1 - number2)
  p1 = ('O resultado da subtração é: ' + str(finalresult1))
  print(p1)
elif(simbol ==mult):
  finalresult2 = (number1 * number2)
  p2 = ('O resultado da multiplicação é: ' + str(finalresult2))
  print(p2)
elif(simbol == div):
  finalresult3 = (number1 / number2)
  p3 = ('O resultado da divisão é: ' + str(finalresult3))
  print(p3)
  
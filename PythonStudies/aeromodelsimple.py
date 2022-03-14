#Aero Model


plane = float(input("Vamos pilotar um avião? Digite 1 para acelerar o avião: "))


if plane == 1:
  print('O avião está acelerando')
  continue1 = float(input("Digite 2 para decolar o avião: "))
else:
  print('O avião está parado')

if continue1 == 2:
  print('O avião decolou')
  continue2 = float(input('Digite 3 para ligar o piloto automático: '))
else:
  print('O avião ainda está decolando!')

if continue2 == 3:
  print('Você ligou o piloto automático!')
  continue3 = float(input('Digite 4 para desacelerar e pousar: '))
else:
  print('O avião ainda está decolando')

if continue3 == 4:
  print('O avião foi pousado!')
  continue4 = float(input('Digite 5 para desligar o avião: '))
else: 
  print('O avião continua funcionando')

if continue4 == 5:
  print('Parabéns, você pousou e desligou o avião com sucesso!!!')

  
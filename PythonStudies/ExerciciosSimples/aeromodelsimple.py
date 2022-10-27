#Aero Model

# Criação do primeiro loop, para o primeiro comando
while True:
  # Entrada do comando (numérico)
 plane = float(input("Vamos pilotar um avião? Digite 1 para acelerar o avião: "))
  # Uso de estrutura condicional para validar o comando
 if plane == 1:
  print('O avião está acelerando')
  continue1 = float(input("Digite 2 para decolar o avião: "))
  # Quebra do loop para saida, e também entrada no próximo loop
  break
 else:
  print('O avião está parado')
# Fim do primeiro loop

# Começo do segundo loop
while True: 
 if continue1 == 2:
  print('O avião decolou')
  continue2 = float(input('Digite 3 para ligar o piloto automático: '))
  break
 else:
  print('O avião ainda está decolando!')
# Fim do segundo loop

# Começo do terceiro loop
while True:
 if continue2 == 3:
  print('Você ligou o piloto automático!')
  continue3 = float(input('Digite 4 para desacelerar e pousar: '))
  break
 else:
  print('O avião ainda está decolando')
# Fim do terceiro loop

# Começo do quarto loop
while True: 
 if continue3 == 4:
  print('O avião foi pousado!')
  continue4 = float(input('Digite 5 para desligar o avião: '))
  break
 else: 
  print('O avião continua funcionando')
# Fim do quarto loop

# Começo do quinto loop
while True:
 if continue4 == 5:
  print('Parabéns, você pousou e desligou o avião com sucesso!!!')
  break
# fim do codigo
  
# ETE PORTO DIGITAL
# ATV LPC
# PROF: CLOVES ROCHA
# ALUNO: GUILHERME FREITAS

print('Vamos pilotar sua aeronave!')
print('1 = aceleração / 2 = Decolagem / 3 = Piloto Automático / 4 = Freio / 5 = Pouso / 6 = Desligar a aeronave')

aeromodel = True

while (aeromodel):
  choose = float(input('Execute o comando aqui: '))

  if (choose == 1):
    print('O avião está acelerando')
  if choose == 2:
      print('O avião está decolando!')
  if choose == 3:
      print('Você ligou o piloto automático')
  if choose == 4:
      print('O avião está freiando')
  if choose == 5:
      print('O avião está pousando')
  if choose == 6:
      print('O voo foi concluído com sucesso!!!')

    
    






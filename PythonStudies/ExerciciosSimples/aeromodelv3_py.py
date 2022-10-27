
# AeroProject w/ while function

print('Vamos pilotar sua aeronave!')
print('1 = aceleração / 2 = Decolagem / 3 = Piloto Automático / 4 = Freio / 5 = Pouso / 6 = Desligar a aeronave')



choose = float(input('Execute o comando aqui: '))

  
while choose != 1:
    print('Digite as ações em ordem válida')
    choose = float(input('Execute o comando aqui: '))

if (choose == 1):
    print('O avião está acelerando')
    choose1 = float(input('Execute o comando aqui: '))
while choose1 != 2:
    print('Digite as ações em ordem válida')
    choose1 = float(input('Execute o comando aqui: '))

if choose1 == 2:
      print('O avião está decolando!')
      choose2 = float(input('Execute o comando aqui: '))
while choose2 != 3:
    print('Digite as ações em ordem válida')
    choose2 = float(input('Execute o comando aqui: '))

if choose2 == 3:
      print('Você ligou o piloto automático')
      choose3 = float(input('Execute o comando aqui: '))
while choose3 != 4:
    print('Digite as ações em ordem válida')
    choose3 = float(input('Execute o comando aqui: '))


if choose3 == 4:
      print('O avião está freiando')
      choose4 = float(input('Execute o comando aqui: '))
while choose4 != 5:
    print('Digite as ações em ordem válida')
    choose3 = float(input('Execute o comando aqui: '))


if choose4 == 5:
      print('O avião está pousando')
      choose5 = float(input('Execute o comando aqui: '))
while choose5 != 6:
    print('Digite as ações em ordem válida')
    choose5 = float(input('Execute o comando aqui: '))



if choose5 == 6:
      print('O voo foi concluído com sucesso!!!')


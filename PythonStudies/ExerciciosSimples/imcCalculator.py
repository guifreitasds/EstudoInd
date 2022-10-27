# Estudo IND
# IMC Calculator
# Insira seu peso e altura e calcule seu Indice de Massa corporal!


print('Vamos calcular seu IMC?')
weight = float(input('Insira aqui seu peso em Kg: '))
height = float(input('Insira sua altura em metros: '))

imc = weight / (height * height)

p = ('Seu IMC é de: ' + str(imc))
print(p)

if(imc < 18.5):
  print('Você está abaixo do peso')
if (imc >= 18.6 and imc <= 24.9):
  print('Você está no peso ideal')
if (imc >= 25 and imc <= 29.9):
  print('Sobrepeso')
if (imc  > 29.9):
  print('Obesidade')
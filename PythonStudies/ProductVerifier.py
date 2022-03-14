# Verificador de Produtos!

local1 = 1
local2 = 2

print('Vamos verificar o preço do seu produto?')

print('Insira o nome do produto: ')
name = str(input())

print('Insira o valor do produto: ')
value = int(input())

print('Digite 1 para produto importado e 2 para nacional:')
local = int(input())

print('Digite a cotação atual do dólar: ')
cotation = int(input())



if(local == local1):
  finalvalue = (value * cotation)
  p = ('O valor final de ' + str(name) + ' é igual a: R$' + str(finalvalue))
  print(p)

elif(local == local2):
  p1 = ('O valor final de ' + str(name) + ' é igual a: R$' + str(value))
  print(p1)

else:
  print('Digite um valor de local válido!')



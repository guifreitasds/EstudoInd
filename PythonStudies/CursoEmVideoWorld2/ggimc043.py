# Descubra seu indice de massa corporal

print('\033[34m-=-'*20)
print('Vamos descobrir seu indice de massa corporal?\033[m')
weight = float(input('Para isso, me informe seu \033[4mpeso\033[m em Kg: '))
height = float(input('Também preciso que me informe sua \033[4maltura\033[m: '))

imc = weight/(height*height)

if imc < 18.5:
    print('\033[31mO seu IMC é de {:.2f} e você está abaixo do peso\033[m'.format(imc))
elif 18.5 <= imc < 25:
    print('\033[32mO seu IMC é de {:.2f} e você está no peso ideal!\033[m'.format(imc))
elif 25 <= imc < 30:
    print('\033[33mO seu IMC é de {:.2f} e você está em sobrepeso\033[m'.format(imc))
elif 30 <= imc < 40:
    print('\033[33mO seu IMC é de {:.2f} e você está obeso\033[m'.format(imc))
else:
    print('\033[31mO seu IMC é de {:.2f} e você está em obesidade mórbida\033[m'.format(imc))
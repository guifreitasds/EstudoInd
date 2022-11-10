
while True:
    name = str(input('Digite seu nome de usuário: '))
    passw = str(input('Digite sua senha: '))
    if(name!=passw):
        print('\033[35mSUCESSO!\033[m')
        break
    print('\033[31mERRO, nome e senha iguais.\033[m')
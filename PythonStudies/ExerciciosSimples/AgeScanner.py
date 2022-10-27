# Estudo IND
# AgeScanner
# Coloque sua idade em anos, meses e dias e veja qual sua quantidade total de dias em vida!

agey = float(input('Insira aqui quantos anos você tem: '))
agem = float(input('Insira aqui quantos meses você tem: '))
aged = float(input('Insira aqui quantos dias você tem: '))

yd = agey * 365
md = aged * 30
dd = aged * 1

scanner = yd + md + dd

print(scanner)
print('Acima a quantidade total de dias de vida que você tem!')

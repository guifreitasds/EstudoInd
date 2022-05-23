# Leitor de produtos

total = pmil = cont = cheapp = 0
cheap = ''

while True:
    n = str(input('Digite o nome do produto: ')).strip()
    p = float(input('Digite o preço do produto: R$'))
    total += p
    cont += 1
    if cont == 1 or p < cheapp:
        cheap = n
        cheapp = p
    if p >= 1000:
        pmil += 1
    confirm = ' '
    while confirm not in 'SN':
        confirm = str(input('Deseja adicionar um novo produto: [S/N] ')).strip().upper()[0]
    if confirm == 'N':
        break

print(f'O total da compra é: R${total}')
print(f'O número de produtos acima de R$1000 é: {pmil}')
print(f'E o nome do produto mais barato é: {cheap} que custa R${cheapp}')

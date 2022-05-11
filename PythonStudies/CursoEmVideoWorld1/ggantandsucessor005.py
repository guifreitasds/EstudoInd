# Antecessor e Sucessor
print('\033[34m-=\033[m' * 20)
n1 = int(input('\033[35mDigite um número: ')) # Pedido do número ao usuário

print('O antecessor de {} é {}'.format(n1, n1-1), end=' ') # Visualização do antecessor com end function
print('e o sucessor é {}'.format(n1+1)) # Mais a visualização do sucessor na mesma linha, pela end function
print('\033[34m-=' * 20)



# Packing
# def corrida(**podium):
#     for posicao, piloto in podium.items():
#         print(f'{posicao} -> {piloto}')

# corrida(pri='Carlinos Bala', seg='Neto Baiano', ter='Caça rato')

# # Unpacking
# def corrida(pri, seg, ter):
#     for posicao, piloto in podium.items():
#         print(f'{posicao} -> {piloto}')

# podium = {"pri":"Bala", "seg": "Neto Baiano", "ter":"Caça Rato"}

# corrida(**podium)


# Callable com Packing/Unpacking

def calc_preco(preco_bruto, calc_imposto, **params):
    return preco_bruto + preco_bruto * calc_imposto(**params)

def ipi(importado):
    return 0.21 if importado else 0.11

def explosive(is_explosive, fator=1):
    return 0.09*fator if is_explosive else 0

if __name__=="__main__":
    preco_final = calc_preco(134.98, ipi, importado=False)
    preco_final = calc_preco(preco_final, explosive, is_explosive=True, fator=1.5)
    print(f"Preço final: R${preco_final:.2f}")
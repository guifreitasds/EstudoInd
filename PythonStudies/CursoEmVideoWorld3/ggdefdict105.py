def notas(*n, sit=False):
    """
    -> Função que recebe infinitas notas para solucionar a situação
    do aluno requerido

    :param n: guarda todas as notas
    :param sit: (Opcional) Mostra a situação do aluno de acordo com a média
    :return: retorna o dicionário com as informações necessárias
    """
    dici = dict()
    dici['Total'] = len(n)
    dici['Maior nota'] = max(n)
    dici['Menor nota'] = min(n)
    dici['Média'] = (sum(n)/len(n))
    if sit:
        if dici['Média'] > 7:
            dici['Situação'] = 'BOA'
        elif dici['Média'] >= 7:
            dici['Situação'] = 'RAZOÁVEL'
        else:
            dici['Situação'] = 'RUIM'
    return dici


resp = notas(5.5, 2.5, 1.5, 10, sit=True)
print(resp)
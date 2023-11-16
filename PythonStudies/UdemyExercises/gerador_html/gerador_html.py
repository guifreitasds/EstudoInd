def tag_bloco(tag, conteudo, *args, **kwargs):
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} {kwargs}>{html}</{tag}>'


def tag_lista(*items, ordered=False):
    conteudo_lista = ''.join(f'<li>{item}</li>' for item in items)
    tipo_lista = 'ol' if ordered else 'ul'
    return f'<{tipo_lista}>{conteudo_lista}</{tipo_lista}>'

if __name__=="__main__":

    with open('gerador_html/teste.html', 'a', encoding='UTF-8') as arquivo:
        print(tag_bloco(tag_lista, 'Retrô', 'Afogados da Ingazeira', 'Vera Cruz', classe='lista_times'), file=arquivo)

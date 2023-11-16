def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop("html_class")
    attrs = ' '.join(f'{k}="{v}"' for k, v in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {attrs}>{inner}</{tag}>'


with open("gerador_html/teste.html", 'w') as arquivo:
    print(tag('p',
            tag('span', 'Curso de Python, por '),
            tag('strong', 'Guilherme Freitas', id='gf'),
            tag('span', ' e '),
            tag('strong', 'Maria Luiza', id='ml'),
            tag('span', '.'), 
            html_class='alert'
            ),
            file=arquivo
    )
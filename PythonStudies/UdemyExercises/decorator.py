def log(funcao):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da função: {funcao.__name__}')
        print(f"Args: {args}, Kwargs: {kwargs}")
        resultado = funcao(*args, **kwargs)
        print(f"Resultado da chamada: {resultado}")
        return resultado
    return decorator

@log
def soma(x, y):
    return x+y


@log
def subtracao(x, y):
    return x-y


soma(1,2)
subtracao(2,1)
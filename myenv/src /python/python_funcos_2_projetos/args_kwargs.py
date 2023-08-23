#numero variavel de argumentos posicionais
def minha_funcao(*args):
    for arg in args:
        print(arg)
      
minha_funcao('Jose', 'Maria', 'Joao')

#numero variavel de argumentos nomeados
def minha_funcao_nova(**kwargs):
    for key, values in kwargs.items():
        print(f'{key}:{values}')

minha_funcao_nova(nome='rafaela', idade=23, cidade='salvador')

#combinando *args e **kwargs
def minha_nova_funcao(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, values in kwargs.items():
        print(key, values)
minha_nova_funcao('curriculo', 'desenvolvedor', nome='alice', idade=25)
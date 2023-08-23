#Escreva uma função que receba uma lista de strings e retorne a quantidade de strings na lista

list_string = ['zero', 'um', 'dois']

def string_count(lista: list):
    '''Retorna quantidade de elementos em uma lista'''
    quantidade = len(lista)
    return quantidade
print(string_count(list_string))
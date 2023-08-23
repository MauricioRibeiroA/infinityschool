#Escreva uma função que receba uma lista de números e retorne o maior valor

num_list = [1,7,21]

def max__value_list(lista: list):
    '''Retorna maior valor de uma lista de números'''
    biggest_num = max(lista)
    return biggest_num
print(max__value_list(num_list))
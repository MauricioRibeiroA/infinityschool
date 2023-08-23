#Escreva uma função que receba uma lista de números e retorne a soma entre eles

list_num = [1,2,3]

def soma_numeros(lista: list):
    '''Retorna a soma de uma lista'''
    somatorio = sum(lista)
    return somatorio
print(soma_numeros(list_num))
#Escreva uma função que receba dois números e retorne o menor deles

def smallest(num1: int, num2: int):
    '''Retorna o menor dentre dois números'''
    smallest_num = min(num1, num2)
    return smallest_num
print(smallest(2, 5))
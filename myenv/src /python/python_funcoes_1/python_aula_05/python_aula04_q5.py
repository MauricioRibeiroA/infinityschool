import logging
from math import sin
from venv import logger
sinais = ['+','-','*','/']

operacao_usuario = input('Qual operacao deseja realizar? ')
while operacao_usuario not in sinais:
    print('Sinal não existente')
    operacao_usuario = input('Qual operacao deseja realizar? ')

num_1 = int(input('Digite o primeiro numero: '))
num_2 = int(input('Digite o segundo numero: '))


def soma(num_1: int, num_2:int):
    '''Retorna a soma de dois argumentos'''
    return(f'O resultado da soma é: {num_1+num_2}')

def subtracao(num_1: int, num_2:int):
    '''Retorna a diferença entre dois argumentos'''
    return(f'O resultado da subtração é: {num_1-num_2}')

def multiplicacao(num_1: int, num_2:int):
    '''Retorna o produto de dois argumentos'''
    return(f'O resultado da multiplicação é: {num_1*num_2}')

def divisao(num_1: int, num_2:int):
    '''Retorna a divisão entre dois argumentos'''
    return(f'O resultado da divisão é {num_1 / num_2}' if operacao_usuario != 0 else logger.exception)

def calculadora(operacao_usuario: str, num_1: int, num_2: int):
    match operacao_usuario:
        case '+':
            print(soma(num_1, num_2))          
        case '-':
            print(subtracao(num_1, num_2))    
        case '*':
            print(multiplicacao(num_1, num_2))
        case '/':
            print(divisao(num_1, num_2))
        case _:
            return('foo')
print(calculadora(operacao_usuario, num_1, num_2).__doc__)





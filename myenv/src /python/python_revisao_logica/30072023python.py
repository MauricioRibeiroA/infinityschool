from pickletools import int4
import re
import requests
from tkinter import *


resultados = []
dividendo = [2,3,4,5]
divisor = [1,2,3,4,5,6,7,8,9]

def popular():
    for i in dividendo:
        for n in divisor:
            divisao = i/n
            print(f'o resultado da divisao de {i} por {n} é igual a {divisao}')
            if i % n == 0:
                print('resto zero')
                resultados.append(divisao)           
            print(resultados)
            if len(resultados) == 2:
                print(f'{i} é um numero primo')
            
        
popular()
'''
def popularGrupo(qtd):  
    qtdNumeros = qtd
    for n in range(2, qtdNumeros):
        if 4 % n == 0 and n % 1 == 0:
            print(f'o numero {n} é primo')
        else:
            print(f'o numero {n} nao é primo')
popularGrupo(10)   
'''

#crie um método para escrever a sequência de fibo
def fiboSequence(times):
    n, n2 = 0, 1
    i = 0
    while i <=times:
        soma = n + n2
        n = n2
        n2 = soma
        i += 1
        print(soma)           
#fiboSequence(20)

#crie um método para escrever a tabuada de todos os números

primeiroTermoNumerico = []
segundoTermoNumerico = []

def populateGroups():
    for i in range(1, 10):
        primeiroTermoNumerico.append(i)
        segundoTermoNumerico.append(i)
    for n in primeiroTermoNumerico:
        for n2 in segundoTermoNumerico:
            resultadoMultiplicacao = n2 * n
            print('A multiplicacao de {} por {} é igual a {}'.format(n, n2, resultadoMultiplicacao))
            #texto = f'''A multiplicacao de {n} por {n2} é igual a {resultadoMultiplicacao}'''
            #return texto
            #resultado_tabuada['text'] = texto
#populateGroups()

'''
from tkinter import Button


janela = Tk()
janela.title('titulo da janela')
janela. geometry('400x400')

texto_orientacao = Label(janela, text='Clique no método que deseja executar')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

#estrutura da funcao tabuada
botaoTabuada = Button(janela, text='Clique aqui', command=populateGroups)
botaoTabuada.grid(column=0, row=1)
resultado_tabuada = Label(janela, text='')
resultado_tabuada.grid(column=0, row=2, padx=10, pady=10)

#estrutura da funcao fibonacci
botaoFibonacci = Button(janela, text='Clique aqui', command=populateGroups)
botaoFibonacci.grid(column=0, row=3)

#estrutura da funcao numero primo
botaoNumeroPrimo = Button(janela, text='Clique aqui', command=populateGroups)
botaoNumeroPrimo.grid(column=0, row=5)

janela.mainloop()
'''
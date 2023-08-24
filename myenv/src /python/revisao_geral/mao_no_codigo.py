#leia o salario de um trabalhador...
from functools import reduce
from math import prod
from operator import mul
import math
import json
from datetime import date, datetime
import time

salario = 1000
prestacao = 500

if prestacao > salario * 0.2:
    print('emprestimo nao concedido')

#calcular peso ideal
altura = 1.86
sexo = 'm'

if sexo == 'm':
    peso_ideal = 72.7 * altura - 58
    print(f'Seu peso idela é: {peso_ideal}')
else:
    peso_ideal = 62.1 * altura - 44.7
    print(f'Seu peso idela é: {peso_ideal}')


#media ponderada de 3 provas
#receber 3 notas e colocar em uma array
#cada uma das 3 notas na array sera multiplicada pelo seu peso e o resultado sera dividido pela soma dos pesos

#nota1 = int(input('Digite a primeira nota: '))
#nota2 = int(input('Digite a segundaa nota: '))
#nota3 = int(input('Digite a terceira nota: '))


def calc_media_pond(nota1:int, nota2:int, nota3:int):
    media = (nota1*1)+(nota2*1)+(nota3*3) / 5
    if media > 60:
        return f'Aprovado!'
    else:
        return f'Reprovado!'
    
#print(calc_media_pond(nota1, nota2, nota3))

#tabela de multiplicacao
lst_num = [1,2,3,4,5,6,7,8,9,10]
multiplicador = 4
for num in lst_num:
    print(f'{multiplicador} x {num} = {multiplicador * num}')

numero = 23487
print(f'São {len(str(numero))} digitos no numero digitado')

#fibonacci
lst = [1,1]
count_index = 0
for i in range(0, 10):
    lst.append((lst[i] + lst[i+1]))
    count_index += 1
print(lst)

#soma, multiplicacao e numeros de lista
lista_numeros = [1,2,3,4,5]
print(prod(lista_numeros))
print(reduce(mul, lista_numeros, 1))
print(sum(lista_numeros))

""" 5 alturas, armazena e imprimi em reverse
alturas = []
testar com append """
# alt1 = input('Digite a altura: ')
# alt2 = input('Digite a altura: ')
# alt3 = input('Digite a altura: ')
# alt4 = input('Digite a altura: ')
# alt5 = input('Digite a altura: ')

# alturas = [alt1, alt2, alt3, alt4, alt5]
# alturas.reverse()
# print(alturas)

""" leia 5 numeros inteiros, calcule e mostre a soma dos quadros dos elemtnso """
# numeros = [3,4,7,2,9]
# quadrados = []
# for i in numeros:
#     quadrados.append(math.sqrt(i))
# print(sum(quadrados))


""" crie um dicionario que é uma agenda e coloque nele os seguintes dados: cpf, nome e idade. o programa deve fcriar 5 agendas e iomprimir todos os itens de cada agenda """
# pessoas = []
# pessoa = {}

# def criar_agenda(nome: str, cpf: str, idade: str):
#     '''create key value pair for new agenda'''
#     pessoa['NOME'] = nome
#     pessoa['CPF'] = cpf
#     pessoa['IDADE'] = idade


# while True:
#     print(pessoas)
#     if len(pessoas) == 2:
#         break      
#     else:
#         nome = input('Digite nome: ')
#         cpf = input('Digite cpf: ')
#         idade = int(input('Digite idade: '))
#         pessoa = {}
#         criar_agenda(nome, cpf, idade)  
#         pessoas.append(pessoa)
# print(json.dumps(pessoas, indent=4)) 


""" dicionario com backup e clear after len 5 """
# dict = {}
# def sistema_backup(dict):
#     '''Faz um backup de um dicionario'''
#     backup_version = dict.copy()
#     return backup_version
# count = 0
# while True:
#     print(dict)
#     if len(dict) == 5:
#         print(f'O dicionario atingiu 5 itens e sera resetado {dict}')
#         dict.clear()
#         print(f'Felizmente fizendo o backup do db {save}')
#     else:
#         item = input('Digite  do item: ')
#         dict[count] = item
#         count +=1
#         save = sistema_backup(dict) 

""" dicionario com backup e clear after len 5,estudando como fazer backup de dicts nested inside array """
# pessoal = [{'NOME': 'm', 'CPF': '1', 'IDADE': 2}, {'NOME': 't', 'CPF': '5', 'IDADE': 6}]

# for i in range(0,1):
#     new = pessoal[i].copy()
# print(f'aqui esta o backup {new}')
# print(pessoal[0])


""" retorne o produto de 3 numeros """
# num1 = int(input('Digite numero: '))
# num2 = int(input('Digite numero: '))
# num3 = int(input('Digite numero: '))

# def produto(num1: int, num2: int, num3: int):
#     '''retorna o produto de 3 numeros'''
#     produto = num1 * num2 * num3
#     return produto
# print(produto(num1, num2, num3))

""" criar funcao chamada somaimposto """
# def somaImposto(taxa_imposto:int, custo: int):
#     tot = taxa_imposto * custo
#     res = tot + custo
#     return f'o valor do produto inicial era R${res}'
# print(somaImposto(0.5, 100))

""" converter de 24horas para 12horas """
def convert_hours(hora, minutos):
  horario = ':'.join([hora, minutos])
  time = datetime.strptime(horario, '%H:%M')
  return time.strftime('%r')

print(convert_hours('21', '30'))
    







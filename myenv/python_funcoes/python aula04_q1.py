#Crie uma função para calcular o IMC de 4 pessoas
from cgi import test
import json
import re
import string

nested_people = [
  {'name': 'Joao', 'peso': 87, 'altura': 1.76},
  {'name': 'Batista', 'peso': 96, 'altura': 1.86},
  {'name': 'Jose', 'peso': 78, 'altura': 1.66},
  {'name': 'Pedro', 'peso': 98, 'altura': 1.96},
  ]
#print(json.dumps(nested_people, indent=4))

def calc_imc(name: str, peso: int, altura: int):
  '''Retorna o IMC de uma pessoa'''
  imc = peso / altura**2
  return f'O IMC de {name} é {imc}'


#for i in range(4):
  print(calc_imc(nested_people[i]['name'], nested_people[i]['peso'], nested_people[i]['altura']))
######################################################
  #Faça uma função para calcular o valor/hora de um funcionario
'''nome_funcionario = input('Qual o nome do funcionário? ')
salario = int(input('Quanto o funcionário recebeu no período? '))
horas_trab = int(input('Quantas horas o funcionário trabalhou no período? '))'''


def calculate_valorhora(valor_recebido: int, funcionario_name: str, horas_trabalhadas: int):
    valor_hora = valor_recebido / horas_trabalhadas
    return f'O valor hora do funcionário {funcionario_name} é de R${valor_hora}'
  
#print(calculate_valorhora(salario, nome_funcionario, horas_trab))
######################################################
palavra_frase = 'm@uricio estuda python!'

qtd = len(palavra_frase)
#print(qtd)

def find_blank(palavra):
#tem que sair de n=1 porque significa que ele ja achou o primeiro espaço, caso contrário irá contabilizar um a menos
  n=1
  for i in palavra:
   if(i.isspace()):
      n+=1
      return n
find_blank(palavra_frase)


#using regex
print(re.sub(pattern='^\w\s', repl='$', string=palavra_frase))

print(re.sub(pattern='\W', repl='$', string=palavra_frase))

#removendo os espaços
palavra_without_blank = re.sub(r'[\s+]', '', palavra_frase)

#calculando a diferença 
print(f'A frase escrita sem espaços fica dessa forma {palavra_without_blank}')
qtd_spc = len(palavra_frase) - len(palavra_without_blank)

#removendo as pontuações
palavra_without_punc = re.sub(r'[^\w\s]', '', palavra_frase)

#calculando a diferença 
qtd_punc = len(palavra_frase) - len(palavra_without_punc)

print(f'A quantidade de acentos é: {qtd_punc}')
print(f'A quantidade de espaços é: {qtd_spc}')
   
#using string import and iteration
punctuations_list = string.punctuation

print(punctuations_list)


n = 0
testing = {letra for letra in palavra_frase}
print(testing)
for letra in testing:
  if letra in punctuations_list:
    print('ok')
  else:
    print('no')
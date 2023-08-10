#Crie uma função para calcular o IMC de 4 pessoas

import json

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


for i in range(4):
  print(calc_imc(nested_people[i]['name'], nested_people[i]['peso'], nested_people[i]['altura']))
pessoas = {'Joao': 83, 'Maria': 28, 'Pedro': 35, 'Lucas': 19}

#Acessando idade de João que é um value através da key e declarando uma variável para armazenar
idade_joao = pessoas['Joao']

#Adicionando um novo par key, value
pessoas['Ana'] = 31

#Criando função que aceita 1 argumento
def maior_idade(arg_dict):
    idade_max = max(pessoas, key=arg_dict.get) #Ref. readthedocs python: get() returns the value for key in the dictionary; if not found returns a defaltu value
    print(idade_max)
maior_idade(pessoas)
    
    
#CREATE
#list
#Lista é uma coleção ordenada e mutável. Permite membros duplicados
from collections import UserString
from xxlimited import new


lista = ['mauricio', 'ribeiro']
print(type(lista))

#tuple
#Tupla é uma coleção orndenada e imutável. Permite membros duplicados.
tupla = ('mauricio', 'ribeiro')
print(type(tupla))

#set
#Set é uma coleção não ordenada e não indexada. Nenhum membro duplicado.
setList = set(['mauricio', 'ribeiro'])
print(type(setList))

#dict
#O dicionário é uma coleção ordenada e mutável. Nenhum membro duplicado. 
dicionarioDados = {'nome': 'mauricio', 'sobrenome': 'ribeiro'}

def create_dict_from_keys(): #Returns a dictionary with the specified keys and value
  x = ('key1', 'key2', 'key3')
  y = ('value1')
  newDict = dict.fromkeys(x, y)
  print(newDict)
create_dict_from_keys()

print('-'*50)

#READ
print(lista)
print(tupla)
print(setList)
print(dicionarioDados)
print(type(dicionarioDados))

def read_dicts_key(dictionary):
  for k1 in dictionary.keys():
    print(k1)
    k = dictionary.keys()
    print(k)
read_dicts_key(dicionarioDados)

def read_dicts_value(dictionary):
  for v1 in dictionary.values():
    print(v1)
  v = dictionary.values()
  print(v)
read_dicts_value(dicionarioDados)
print('-'*50)
#UPDATE
def append_item(item): #Adds an element at the end of the list
  lista.append(item)
  return lista
print(append_item('azul'))

objetos = ['luva', 'computador']
def extend_list(itens): #Add the elements of a lista to the end of the current list
  lista.extend(itens)
  return lista
print(extend_list(objetos))
print('-'*50)

def insert_item(position, item): #Adds an element to a specified position
  lista.insert(position, item)
  return lista
print(insert_item(1, 'cadeira'))

'''def update_dict(dict, key, new_value):
  x = dict.get(key)
  dict[x] = new_value
  print(f'o novo dicionario é: {dict}')
update_dict(dicionarioDados, 'nome', 'jose')'''

def update_dict_square_brackets(dict, key, new_value): #Changes values from keys
  dict[key] = new_value
  print(f'o novo dicionario a partir de square brackets é: {dict}')
update_dict_square_brackets(dicionarioDados, 'nome', 'jose') 

def update_dict_key_value(dict, key, new_value): #Adds new key and value
  dict.update({key: new_value})
  print(f'novo dicionario a partir do built-in method update  é: {dict}')
update_dict_key_value(dicionarioDados, 'nome', 'Mau')
print('-'*50)
#DELETE
def clear_list(): #Removes all the elements from the list
  lista.clear()
  return lista
print(clear_list())

def pop_item(item): #Removes the element at the specified position
  pass

def remove_item(item): #Removes the first item with the specified value
  pass


dict_of_lists = {'nomes': ['Dunga', 'Zangado', 'Soneca'], 'cores': ['Azul', 'Vermelho', 'Amarelo']}
#print(dict_of_lists)
#print(dict_of_lists.keys())
#print(dict_of_lists.values())
nomesCadastrados = dict_of_lists['nomes']
print(nomesCadastrados)


#ternary operator && dictionary of lists
def userLogin():
  nome_usuario = input('Digite o seu nome para ter acesso ao sistema: ')
  print('Usuario logado') if nome_usuario in nomesCadastrados else print('Usuario não cadastrado')
userLogin()







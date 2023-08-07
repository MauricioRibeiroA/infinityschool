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



print('-'*50)

#READ
'''print(lista)
print(tupla)
print(setList)
print(dicionarioDados)
print(type(dicionarioDados))'''

#Read dict from a key data
def print_dict_from_key(arg1):
  print(dicionarioDados[arg1])
#print_dict_from_key('nome')

#Read dict items
def print_dict_items(dictionary):
  print(dicionarioDados.items())
#print_dict_items(dicionarioDados)

#Read dict with loop iteration for keys
def read_dicts_key(dictionary):
  for k1 in dictionary.keys(): #one way
    print(k1)
    k = dictionary.keys() #other way
    print(k)
#read_dicts_key(dicionarioDados)

#Read dict with loop iteration for values
def read_dicts_value(dictionary):
  for v1 in dictionary.values(): #one way
    print(v1)
  v = dictionary.values() #other way
  print(v)
#read_dicts_value(dicionarioDados)
print('-'*50)
#UPDATE
def append_item(item): #Adds an element at the end of the list
  lista.append(item)
  return lista
#print(append_item('azul'))

objetos = ['luva', 'computador']
def extend_list(itens): #Add the elements of a list to the end of the current list
  lista.extend(itens)
  return lista
print(extend_list(objetos))
print('-'*50)

def insert_item(position, item): #Adds an element to a specified position of the list
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

def del_item_dict(arg1):
  del dicionarioDados[arg1]
  print(dicionarioDados)
del_item_dict('sobrenome')


print('-'*50)
dict_of_lists = {'nomes': ['Dunga', 'Zangado', 'Soneca'], 'cores': ['Azul', 'Vermelho', 'Amarelo']}
nomesCadastrados = dict_of_lists['nomes']

nome_usuario = input('Digite o seu nome para ter acesso ao sistema: ')
#ternary operator && dictionary of lists
def userLogin(nome_usuario):
  print('Usuario logado') if nome_usuario in nomesCadastrados else print('Usuario não cadastrado')
userLogin(nome_usuario)







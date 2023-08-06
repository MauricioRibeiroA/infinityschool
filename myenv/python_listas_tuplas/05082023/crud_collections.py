#CREATE
#list
lista = ['mauricio', 'ribeiro']
print(type(lista))

#tuple
tupla = ('mauricio', 'ribeiro')
print(type(tupla))

#set
setList = set(['mauricio', 'ribeiro'])
print(type(setList))

#dict
dicionarioDados = {'nome': 'mauricio', 'sobrenome': 'ribeiro'}
print(type(dicionarioDados))
print('-'*50)
#READ
print(lista)
print(tupla)
print(setList)
print(dicionarioDados)
print('-'*50)
#UPDATE
#Lista é uma coleção ordenada e mutável. Permite membros duplicados
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

def insert_item(position, item):
  lista.insert(position, item)
  return lista
print(insert_item(1, 'cadeira'))
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




#Tupla é uma coleção orndenada e imutável. Permite membros duplicados.

#Set é uma coleção não ordenada e não indexada. Nenhum membro duplicado.

#O dicionário é uma coleção ordenada e mutável. Nenhum membro duplicado. 
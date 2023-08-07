#CREATE

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
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

#READ
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
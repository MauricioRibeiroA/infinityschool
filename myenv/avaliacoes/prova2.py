#declarando variaveis
list1 = []
list2 = []
resultado = []

#populando lista1 com inputs do usuario
for i in range(0, 4):
  item_list = int(input('Digite um item para a primeira lista: '))
  list1.append(item_list)
#populando lista2 com inputs do usuario
for i in range(0, 6):
  item_list = int(input('Digite um item para a segunda lista: '))
  list2.append(item_list)

#usando built-in method da <class 'set'> disponivel . Melhor estrutura para trabalhar com conjuntos e menor alocacação de memória Big O do que listas com iterations
intersecao = list(set(list1).intersection(list2))
intersecao1 = set(list1).intersection(list2)
#somando os elementos da nova lista
soma_da_intersecao = sum(intersecao)
#addicionando elementos especificios na lista que irá ser convertida em uma tuple
resultado.append(intersecao)
resultado.append(soma_da_intersecao)
#conversão para tuple já que ela seria imutável durante o tratamento dos dados
resu_tuple = tuple(resultado)
print(resultado)





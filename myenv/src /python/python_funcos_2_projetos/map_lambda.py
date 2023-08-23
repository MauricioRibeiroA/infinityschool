#util quando se quer aplicar uma determinada operacao a todos os elementos de uma sequencia



#map com lambda

numeros = [1,2,3,4,5]

quadrados = list(map(lambda num: num ** 2, numeros))

print(quadrados)

#a partir de uma lista de strings, utilize map() e uma funcao lambda para converter tdas as letras em maiusculas
list_strings = ['maria', 'joao', 'jose']

cap_strings = list(map(lambda x: x.upper(), list_strings))
print(cap_strings)


list_dict_person = [
    {'nome': 'mauricio','idade': 39},
    {'nome': 'joao','idade': 39}, 
    {'nome': 'maria','idade': 39}, 
    {'nome': 'jose','idade': 39}
    ]

only_val = list(map(lambda x: list_dict_person[list_dict_person.index(x)]['nome'], list_dict_person))
print(only_val)


#only_val = list(map(lambda (x, y): {'nome': x, 'idade': y}, enumerate(list_dict_person)))
#shoudl use parenthesis with parameters since the next() operation on enumerate returns a tuple. this lambda is equivalent to def foo((i,x))
#lambdas cant unpack tuple as list comprehensions do
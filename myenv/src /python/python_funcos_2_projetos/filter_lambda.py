#retorna apenas os elementos da sequencia para as quais a funcao retorna true

numeros = [1,2,3,4,5]
pares = list(filter(lambda num: num % 2 == 0, numeros))
print(pares)

#a partir de uma lista de palavras, utilçize filter() e uma funcao lambda para filtras apenas as palavras que possume mais de 5 letras

list_strings = ['maria', 'joao', 'jose', 'bonifacio']

greater_five = list(filter(lambda x: len(x) > 5, list_strings))
print(greater_five)
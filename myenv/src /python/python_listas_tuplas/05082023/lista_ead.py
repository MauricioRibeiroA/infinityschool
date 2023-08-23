import itertools
notas = []
index_qtd_notas = 3
retorno = 0.0


#Faça um programa que leia o nome de uma pessoa e imprima o mesmo invertido.
def invertName(nome):
    print(nome[::-1])
#invertName('Mauricio')

#Faça um programa que leia 4 notas de um aluno e imprima sua média. Após a média ser calculada, informe se o aluno foi ou não aprovado.
    
def calcularMedia():
    media = 0.0
    while len(notas) <= index_qtd_notas:
        nota = int(input('digite uma nota: '))
        notas.append(nota)
        media = sum(notas) / len(notas)
    return media
#retorno = calcularMedia()


def isAprovado():
    print(retorno)
    if retorno >= 7:
        print('Aprovado')
    elif retorno <= 5:
        print('Reprovado')
    elif retorno > 5 and retorno < 7:
        print('Em recuperação')
#isAprovado()

#Faça um programa que leia 10 números e depois mostre o maior e o menor números lidos
'''listaNumeros = [i for i in range(10)]
print(f'o maior número da lista é: {max(listaNumeros)}')
print(f'o menor número da lista é: {min(listaNumeros)}')'''


#Faça um programa que leia 10 números inteiros e separe os mesmos em pares e ímpares. Mostre quantos pares foram lidos, bem como o maior e o menor número par. Faça o mesmo para os ímpares.

#populating list
'''listaNumeros = [i for i in range(1, 11)]

#separating even numbers !! odd numbers
evenNumbers = []
oddNumbers = []
for number in listaNumeros:
    if number % 2 == 0:
        evenNumbers.append(number)
    elif number % 2 != 0:
        oddNumbers.append(number) 
   
print(f'o grupo dos números pares é {evenNumbers} sendo que o maior número par é {max(evenNumbers)} e o menor número par é {min(evenNumbers)}')
print(f'o grupo dos números ímpares é {oddNumbers} sendo que o maior número ímpart é {max(oddNumbers)} e o menor número ímpar é {min(oddNumbers)}')'''

#Façca um programa que leia 10 números inteiros e imprima a lista ordenada em ordem crescente e decrescente
#populating list
'''listaNumeros = [4,7,5,8,2,6,9,1,13,15]
listaNumeros.sort()
print(listaNumeros)
listaNumeros.sort(reverse=True)
print(listaNumeros)'''

#Faça um programa que leia o nome de 4 vendedores e o valor total de venda que cada um realizou. Imprima na tela os 2 vendedores que mais venderam, ordem decrescente.

'''contabilidade = {'mauricio': 1000, 'joao': 800, 'jose': 2900, 'pedro': 673}

testenovo = dict(sorted(contabilidade.items(), key=lambda item: item[1], reverse=True))

slicedct = dict(itertools.islice(testenovo.items(), 0, 2))
print(slicedct)

count = 0
for i in slicedct: 
  print(f'o vendedor #{count} é o {i}, e o seu faturamento foi de {slicedct[i]}')
  count += 1'''

#Faça um programa que leia os nomes dos 3 nadadores que subirão ao pódio na ordem do primero colocado para o terceiro. Imprima na tela a posiçao do nadador e seu nome.

nadadores = {'Xuxa': 1, 'Gustavo': 3, 'Cielo': 2}
nadadores_ordenados = dict(sorted(nadadores.items(), key=lambda item: item[1]))
print(nadadores_ordenados)



      


        
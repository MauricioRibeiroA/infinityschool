#nome = input('digite o seu nome: ')
notas = []
qtd_notas = 3
nomes = ['felipe', 22, 1.89, True]
#Using comprehensions to initialize the list in Python
lista1 = [i for i in range(10)]
nomes1 = []
qtd_nomes = 10

def populateNames():
        cadaNome = input('digite um nome: ')
        nomes1.append(cadaNome) if cadaNome != 'N' else print('ok')
            
       
        
populateNames()

def invertName(nome):
    print(nome[::-1])
#perguntar 4 vezes as notas
    
def calcularMedia():
    while len(notas) <= qtd_notas:
        nota = int(input('digite uma nota: '))
        notas.append(nota)
        media = sum(notas) / len(notas)
    return f'a média do aluno é {media}'

def checkType():
    for i in range(0, len(nomes)):
        print(f'o elemento {nomes[i]} corresponde ao tipo {type(nomes[i])}')
                    
infosUsuarios = ['mauricio', 'ribeiro', 'infinity', 'sabado']

def perguntaAluno():
    print(infosUsuarios)
    question = input('os dados inseridos estão corretos? S ou N ').upper()
    if question == 'S':
        return True
    else:
       newQuestion = input('O que esta errado?' )
       posicaoInfo = infosUsuarios.index(newQuestion)
       newElement = input('Por qual info gostaria de substituir? ')
       infosUsuarios[posicaoInfo] = newElement
       print(infosUsuarios)

#exemplo do professor    
'''dados = ['filipe', 22, 1.89]
print(f'bem vindo, {dados[0]}, {dados[1]}, {dados[2]}')

erro = input('Tem algo errado?(N)').upper()

if erro == 'N':
    dados[0] = 'Felipe'
print(f'bem vindo, {dados[0]}, {dados[1]}, {dados[2]}')'''


#control  + ponto e virgula comenta todo bloco selecionado
def createListWithAppend():
    for i in range(10):
        lista1.append(i)
        return lista1




dados = {'nome': 'mauricio'}
print(dados)
            
for k in dados.keys():
    print(k)

for v in dados.values():
    print(v)

# The keys() method returns dict_keys, which can be converted to a list with list()
# keys = d.keys()
# print(keys)
# print(type(keys))
# # dict_keys(['key1', 'key2', 'key3'])
# # <class 'dict_keys'>

# k_list = list(d.keys())
# print(k_list)
# print(type(k_list))
# # ['key1', 'key2', 'key3']
# # <class 'list'>

listateste = [1, 2, 3, 4, 2]

def cleanDuplicateds(nomeDaLista):
    inst_listateste = list(set(listateste))
    print(f'esta é a lista com itens duplicados {listateste} e o seu tipo é {type(listateste)}')
    print(f'esta é a lista sem itens duplicados {set(listateste)} e o seu tipo é {type(set(listateste))}')
    print(f'esta é a lista sem itens duplicados {inst_listateste} e o seu tipo é {type(inst_listateste)}')



listateste1234 = list()
print(type(listateste1234))

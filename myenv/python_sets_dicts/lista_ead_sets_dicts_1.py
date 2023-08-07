from enum import Enum

class infos(Enum):
    nome = 1
    sobrenome = 2
    idade = 3
    email =4

dados = dict.fromkeys(infos)

for i in dados:
    v = input(f'Responda qual seu(sua) {i}: ')
    #print(i)
    #print(dados[i])
    dados[i] = v
print(dados)


'''infos = ['nome', 'sobrenome', 'idade', 'email']
dados = dict.fromkeys(infos)
count = 0
for i in dados:
    v = input(f'Responda qual seu(sua) {i}: ')
    #print(i)
    #print(dados[i])
    dados[i] = v
print(dados)'''


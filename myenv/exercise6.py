
telefone = input('Telefonou para a vítima?')
local = input('Esteve no local do crime?')
moradia = input('Mora perto da vítima?')
divida = input('Devia para a vítima?')
trabalho = input('Já trabalhou para a vítima?')
respostas = []

if telefone == 'yes':
    telefone = True
    if telefone == True:
        respostas.append(telefone)

if local == "yes":
    local = True
    if local == True:
        respostas.append(local)

if moradia == "yes":
    moradia = True
    if moradia == True:
        respostas.append(moradia)

if divida == "yes":
    divida = True
    if divida == True:
        respostas.append(divida)

if trabalho == "yes":
    trabalho = True
    if trabalho == True:
        respostas.append(trabalho)

if len(respostas) == 2:
    print('Suspeita')
elif len(respostas) >= 3 and len(respostas) <= 4:
    print('Cúmplice')
elif len(respostas) == 5:
    print('Assassino')
else:
    print('Livre de suspeitas')

litros = int
combustivel = str
desconto = float
precoLitro = float

combustivel = input('Qual combustivel?')
litros = int(input('Quantos litros?'))

if combustivel == 'Alcool':
    precoLitro = 1.90
    if litros <= 20:
        desconto = 0.03
        print(desconto)
    elif litros > 20:
        desconto = 0.05
        print(desconto)
elif combustivel == 'Gasolina':
    precoLitro = 2.50
    if litros <= 20:
        desconto = 0.04
        print(desconto)
    elif litros > 20:
        desconto = 0.06
        print(desconto)

def gastoCliente(precoLitro, litros):
    total = precoLitro * litros
    print(total)

gastoCliente(precoLitro, litros)

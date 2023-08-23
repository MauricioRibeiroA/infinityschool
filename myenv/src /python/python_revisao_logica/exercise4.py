notas = []
length = 4



for i in range(length):
    nota = int(input("Digite uma nota do aluno:"))
    notas.append(nota)

#if(nota.is_integer == False):
#        print("difgite um numero")
        

print(notas)

soma = sum(notas)
media = soma / length

if(media >= 7 and media < 10):
    print("aprovado")
elif(media < 7):
    print("reprovado")
elif(media == 10):
    print("Foi aprovado com mérito Parabéns!")

    




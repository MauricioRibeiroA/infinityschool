#pedir a quantidade de alunos da turma
qtdAlunos = int(input('Digite a quantidade de alunos: '))
#defining variables
idades = []
media = float
idade = int

def averageAge(qtdAlunos):
  for i in range(0, qtdAlunos):
    #pedir as idades dos alunos da turma até que iguale a quantidade de alunos
    idade = int(input('Digite a idade do aluno: '))
    idades.append(idade)
    qtdIdades = len(idades)
    while qtdIdades <= qtdAlunos:
      #Calcular média de idade dos alunos
      media = sum(idades) / len(idades)
      qtdIdades += 1
  print(f'A média de idade da turma é {media}')
               
averageAge(qtdAlunos)

#criando o dicionario principal chamado nested students
nested_students = dict()
#criando o dicionario secundario que será populado com os dados dos estudantes e ficará dentro do dicionário principal
dados = ['nome', 'nota1', 'nota2', 'nota3', 'nota4', 'menor_nota', 'maior_nota', 'media', 'situacao', 'status']
students = dict.fromkeys(dados)
#criando as 7 keys para cada um dos sete alunos
for i in range(0, 4):
   nested_students['student'+'_'+str(i)] = students
   #print(students)
   
#UPDATE

def update_specific_student(key_name):
    value_name = input('Qual nome do aluno? ')
    nested_students['student_2'][key_name] = value_name
#update_specific_student('nome')
nested_students['student_2']['nome'] = 'mauricio'
print(nested_students['student_2']['nome'])


'''for i in range(0,2):
  #def get_infos_method(increment):
  nested_students['student'+'_'+str(i)]['nome'] = input('Digite o seu nome: ')
  students['nota1'] = int(input('Digite sua primeira nota: '))
  students['nota2'] = int(input('Digite sua segunda nota: '))
  students['nota3'] = int(input('Digite sua terceira nota: '))
  students['nota4'] = int(input('Digite sua quarta nota: '))
  notas = [students['nota1'], students['nota2'], students['nota3'], students['nota4']]
  students['menor_nota'] = __builtins__.min(notas) 
  students['maior_nota'] = __builtins__.max(notas) 
  grades_sum = __builtins__.sum(notas)
  students['media'] = grades_sum / len(notas)
  students['status'] = 'Aprovado' if students['media'] > 7 else 'Reprovado'  '''
  
   #return students
  #get_infos_method(i)
#get_infos_method()
#get_infos_method()
#print(nested_students)
#print(students)




#CRUD
#testando como criar uma chave dentro do grupo principal nested students
#nested_students['student1'] = students

#how to acsess student1
def access_one_student(student_position):
    print(f'esses são os dados do {student_position} {nested_students[student_position]}')
#access_one_student('student1')


def creating_notas_array():
  notas = [students['nota1'], students['nota2'], students['nota3'], students['nota4']]
  return notas
conjunto_notas = creating_notas_array()

'''iniciar = input('Gostaria de adicionar as informacoes de um aluno? S ou N? ')
if iniciar == 'Y':'''
   
   
'''for student in nested_students:
    nested_students['student'] = students'''

#DONE
from collections import defaultdict
import json

students = defaultdict(str)

students['1']
students['2']

StdsInfo = [{'name': 'mauricio', 'grade1': '8'},{'name': 'maumau', 'grade1': '6'}]
nested_students = dict(zip(students, StdsInfo))

def create_student(nested_students, std_nome, grade_1):
  ultimo_estudante = list(nested_students)[-1]
  ultimo_estudante_n = int(ultimo_estudante) + 1
  variavel_to_str = str(ultimo_estudante_n)
  nested_students[variavel_to_str] = {'name': std_nome, 'grade1': grade_1}
  nested_students = dict(zip(students, StdsInfo))
create_student(nested_students, 'foo bar', 9)
create_student(nested_students, 'lorem ipsum', 8.5)
create_student(nested_students, 'foo bar1', 7.3)

print(json.dumps(nested_students, indent=4))
  
  

   



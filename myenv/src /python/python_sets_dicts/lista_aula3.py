#criando o dicionario principal chamado nested students
nested_students = dict()

#criando o dicionario secundario que será populado com os dados dos estudantes e ficará dentro do dicionário principal
dados = ['nome', 'nota1', 'nota2', 'nota3', 'nota4', 'menor_nota', 'maior_nota', 'situacao', 'status']
students = dict.fromkeys(dados)

for i in range(0, 1):
  def get_infos_method():
    students['nome'] = input('Digite o seu nome: ')
    students['nota1'] = int(input('Digite sua primeira nota: '))
    students['nota2'] = int(input('Digite sua segunda nota: '))
    students['nota3'] = int(input('Digite sua terceira nota: '))
    students['nota4'] = int(input('Digite sua quarta nota: '))
    return students
  get_infos_method()




#CRUD
#testando como criar uma chave dentro do grupo principal nested students
nested_students['student1'] = students

#how to acsess student1
def access_one_student(student_position):
    print(f'esses são os dados do {student_position} {nested_students[student_position]}')
#access_one_student('student1')

for student in nested_students:
    nested_students[student] = students

print(nested_students)

def creating_notas_array():
  notas = [students['nota1'], students['nota2'], students['nota3'], students['nota4']]
  return notas
conjunto_notas = creating_notas_array()

'''def update_specific_student(student_name, key_name, value_name):
    nested_students[student_name][key_name] = value_name
update_specific_student('student1', 'nome', 'mauricio')
print(nested_students)'''


'''def calculate_max_grade():
  notas = [students['nota1'], students['nota2'], students['nota3'], students['nota4']]
  max_grade = __builtins__.max(notas)    
  return max_grade
maior_nota = calculate_max_grade()'''

def calculate_min_grade():
  notas = [students['nota1'], students['nota2'], students['nota3'], students['nota4']]
  min_grade = __builtins__.min(notas) 
  return min_grade
menor_nota = calculate_min_grade() 

def calculate_average_grade():
  notas = [students['nota1'], students['nota2'], students['nota3'], students['nota4']]
  grades_sum = __builtins__.sum(notas)
  average_grade = grades_sum / len(notas)
  return average_grade
media_aluno = calculate_average_grade()

def defining_situacao():
  if media_aluno >= 7:
    return 'Aprovado'
  else:
    return 'Reprovado'
situacao_aluno = defining_situacao()
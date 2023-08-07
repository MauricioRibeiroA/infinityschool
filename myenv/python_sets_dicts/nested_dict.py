nested_students = dict()
#criando o dicionario principal chamado nested students
print(nested_students)
#conferindo classe
print(type(nested_students))

#criando o dicionario secundario que será populado com os dados dos estudantes e ficará dentro do dicionário principal
dados = ['nome', 'sobrenome', 'idade']
students = dict.fromkeys(dados)
#conferindo classe
print(type(students))


#how to acsess student1

#how to access student1 key

#how to access student1 values

#CRUD
#testando como criar uma chave dentro do grupo principal nested students
nested_students['student1'] = students

#ADD
def create_student(student_name):
    nested_students[student_name] = {}
create_student('student2')

for student in nested_students:
    nested_students[student] = students

print(nested_students)

#UPDATE
def update_student(student_name, info_to_change, arg1):
    pass

#DELETE
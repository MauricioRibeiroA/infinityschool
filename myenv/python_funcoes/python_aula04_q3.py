import re
import string

palavra_frase = 'm@uricio estuda python!'

qtt = len(palavra_frase)

only_letters = len(re.sub(pattern='\W', repl='', string=palavra_frase))

#FIRST WAY
#removing spaces with for loop
def find_blank(palavra):
#tem que sair de n=1 porque significa que ele ja achou o primeiro espaço, caso contrário irá contabilizar um a menos
  n=1
  for i in palavra:
   if(i.isspace()):
      n+=1
      return f'Através de método encontrando a quantiade de espaços é {n}'
#print(find_blank(palavra_frase))

#SECOND WAY
#removing spaces with regex
palavra_without_blank = re.sub(r'[\s+]', '', palavra_frase)

qtt_spc = qtt - len(palavra_without_blank)

#FIRST WAY
#removing punctuations with regex
palavra_without_punc = re.sub(r'[^\w\s]', '', palavra_frase)

qtt_punc = qtt - len(palavra_without_punc)
   
#SECOND WAY
#using string import and iteration para remover as pontuações
punctuations_list = string.punctuation

acentos = []
testing_string_punc = {letra for letra in palavra_frase}
for letra in testing_string_punc:
  if letra in punctuations_list:
    acentos.append(letra)


print(f'A quantidade de letras é: {only_letters}')
print(f'A quantidade de acentos é: {qtt_punc}')
print(f'A quantidade de espaços é: {qtt_spc}')

#using regex
'''print(re.sub(pattern='^\w\s', repl='$', string=palavra_frase))'''


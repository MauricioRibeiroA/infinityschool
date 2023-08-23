#Crie uma função para calcular o IMC de 4 pessoas
from cgi import test
import json
import re
import string




palavra_frase = 'm@uricio estuda python!'

qtd = len(palavra_frase)
#print(qtd)

def find_blank(palavra):
#tem que sair de n=1 porque significa que ele ja achou o primeiro espaço, caso contrário irá contabilizar um a menos
  n=1
  for i in palavra:
   if(i.isspace()):
      n+=1
      return n
find_blank(palavra_frase)


#using regex
print(re.sub(pattern='^\w\s', repl='$', string=palavra_frase))

print(re.sub(pattern='\W', repl='$', string=palavra_frase))

#removendo os espaços
palavra_without_blank = re.sub(r'[\s+]', '', palavra_frase)

#calculando a diferença 
print(f'A frase escrita sem espaços fica dessa forma {palavra_without_blank}')
qtd_spc = len(palavra_frase) - len(palavra_without_blank)

#removendo as pontuações
palavra_without_punc = re.sub(r'[^\w\s]', '', palavra_frase)

#calculando a diferença 
qtd_punc = len(palavra_frase) - len(palavra_without_punc)

print(f'A quantidade de acentos é: {qtd_punc}')
print(f'A quantidade de espaços é: {qtd_spc}')
   
#using string import and iteration
punctuations_list = string.punctuation

print(punctuations_list)


n = 0
testing = {letra for letra in palavra_frase}
print(testing)
for letra in testing:
  if letra in punctuations_list:
    print('ok')
  else:
    print('no')
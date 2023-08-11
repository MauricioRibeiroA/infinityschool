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
      return f'Através de método encontrando a quantiade de espaços é {n}'
print(find_blank(palavra_frase))

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

acentos = []
testing_string_punc = {letra for letra in palavra_frase}
print(testing_string_punc)
for letra in testing_string_punc:
  if letra in punctuations_list:
    acentos.append(letra)
print(len(acentos))



'''Estudar

#using regex
print(re.sub(pattern='^\w\s', repl='$', string=palavra_frase))

print(re.sub(pattern='\W', repl='$', string=palavra_frase))'''

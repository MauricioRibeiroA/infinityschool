#Escreva uma função que receba uma string e verifique se ela é um palíndromo

def palindrome_test(word: str):
    '''Testa palindromos'''
    return word[::-1]

reverse_word = palindrome_test('mauricio')

print(reverse_word)

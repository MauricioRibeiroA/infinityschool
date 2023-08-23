#par ou impar
its_even = lambda num: 'par' if num % 2 == 0 else 'impar'
print(its_even(61))

#recebe duas strings e concatena, caso contrario exibir msg de erro
string_1 = input('Digite uma palavra: ')
string_2 = input('Digite uma palavra: ')

size_string1 = len(string_1) 
size_string2 = len(string_2) 

res = string_1 + string_2

check_strings = lambda arg1, arg2: res if arg1 and arg2 > 5 else 'ERR MSG'

#print(check_strings(size_string1, size_string2))

greater_10 = lambda num: num if num > 10 else num/2

print(greater_10(12))

by_5_3 = lambda num: 'divisivel' if num % 3 == 0 and num % 5 == 0 else 'nao divisivel'

print(by_5_3(15))




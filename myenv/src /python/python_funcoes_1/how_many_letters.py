from hmac import new


user_phrase = input('Digite aqui uma palavra ou frase: ')

phrase_to_split = user_phrase.split()
new_phrase = "".join(phrase_to_split)

lst = []
for letter in new_phrase:
    lst.append(letter)
print(len(lst))
    
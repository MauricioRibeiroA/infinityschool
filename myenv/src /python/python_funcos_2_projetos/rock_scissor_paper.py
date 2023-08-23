import random
from re import match

#rock > scissors
#scissors > paper
#paper > rock
lst = ['pedra', 'papel', 'tesoura']

player_choice = input('Escolha entre pedra, papel e tesoura:' )
pc_choice = (random.choice(lst))

def jogada(player_choice:str, pc_choice:str):
    if player_choice == pc_choice:
        return f'empatou'
    elif player_choice == 'pedra' and pc_choice == 'tesoura':
        return 'jogador venceu'
    elif player_choice == 'tesoura' and pc_choice == 'papel':
        return 'jogador venceu'
    elif player_choice == 'papel' and pc_choice == 'pedra':
        return 'jogador venceu'
    else:
        return f'pc venceu'

print(jogada(player_choice, pc_choice))


 #if player_choice == pc_choice:
 #       return f'Empate'
 #   elif 
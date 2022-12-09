import random
import colorama

guide_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list_tuples = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]


def visible(l):
    result = f' {l[0]} | {l[1]} | {l[2]} \n-----------\n' \
             f' {l[3]} | {l[4]} | {l[5]} \n-----------\n' \
             f' {l[6]} | {l[7]} | {l[8]} \n'
    return result


def check_winner(l):
    result = 'none'
    for t in list_tuples:
        if l[t[0]-1] == l[t[1]-1] and l[t[1]-1] == l[t[2]-1] and l[t[0]-1] != ' ':
            result = l[t[0]-1]
            break
    return result


print(f'Welcome to Tic-Tac-Toe Game:\n{visible(guide_list)}')
gamer_sign = input('Please choose "X" or "O" to play: ')
while gamer_sign not in ['X', 'O']:
    gamer_sign = input('Please choose again: "X" or "O" to play: ')
comp_sign = 'X' if gamer_sign == 'O' else 'O'

game_state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
blue = colorama.Fore.BLUE
red = colorama.Fore.RED
while True:
    game_pos = input('Please select position (1 to 9): ')
    game_state[int(game_pos) - 1] = gamer_sign
    if check_winner(game_state) == gamer_sign:
        print(blue + visible(game_state))
        print(blue + 'Congratulations. You Won!')
        break
    else:
        list_index_empty = [i for i in range(9) if game_state[i] == ' ']
        game_state[random.choice(list_index_empty)] = comp_sign
        if check_winner(game_state) == comp_sign:
            print(red + visible(game_state))
            print(red + 'Oops. Computer Won!')
            break
    print(visible(game_state))

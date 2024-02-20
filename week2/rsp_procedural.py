import random as rd

def play():
    player_wins = 0
    computer_wins = 0
    n_turns = 5

    for i in range(n_turns):
        print(f'Round {i+1}')

        com_choice = computer_choose()
        player_choice = player_choose()

        status = compare(player_choice, com_choice)

        if status == 0: # draw
            print(f'Draw! Both players chose {player_choice}')
        elif status == 1: # player wins
            print(f'Player wins! {player_choice} beats {com_choice}')
            player_wins += 1
        else:
            print(f'Player loses! {player_choice} loses to {com_choice}')
            computer_wins += 1
    
    print(f'Player wins {player_wins} times')
    print(f'Computer wins {computer_wins} times')
    print(f'Draw {n_turns - player_wins - computer_wins} times')
    print('Game over!')

def computer_choose():
    choices = ['rock', 'paper', 'scissors']
    return rd.choice(choices)

def player_choose():
    invalid = True
    choices = ['rock', 'paper', 'scissors']
    while invalid:
        choice = input('Enter your choice (rock/paper/scissors): ')
        if choice in choices:
            invalid = False
        else:
            print('Invalid choice! Please try again.')
    return choice

def compare(player_choice, com_choice):
    if player_choice == com_choice:
        return 0
    elif (player_choice == 'rock'       and com_choice == 'scissors')   or \
         (player_choice == 'paper'      and com_choice == 'rock')       or \
         (player_choice == 'scissors'   and com_choice == 'paper'):
        return 1
    else:
        return -1
    

if __name__ == '__main__':
    play()
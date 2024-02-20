import random as rd

class Player:
    def __init__(self):
        self.wins = 0
    
    def choose(self):
        invalid = True
        choices = ['rock', 'paper', 'scissors']
        while invalid:
            choice = input('Enter your choice (rock/paper/scissors): ')
            if choice in choices:
                invalid = False
            else:
                print('Invalid choice! Please try again.')
        return choice

class Computer:
    def __init__(self):
        self.wins = 0
    
    def choose(self):
        choices = ['rock', 'paper', 'scissors']
        return rd.choice(choices)

class GameSystem:
    def __init__(self):
        self.player = Player() # create a Player object
        self.computer = Computer() # create a Computer object
    
    def play(self):
        n_turns = 5
        for i in range(n_turns):
            print('Round', i+1)
            player_choice = self.player.choose()
            computer_choice = self.computer.choose()
            self.compare(player_choice, computer_choice)
        
        print(f'Player wins {self.player.wins} times')
        print(f'Computer wins {self.computer.wins} times')
        print(f'Draw {n_turns - self.player.wins - self.computer.wins} times')
    
    def compare(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            print(f'Draw! Both players chose {player_choice}')
        elif (player_choice == 'rock'       and computer_choice == 'scissors')   or \
             (player_choice == 'paper'      and computer_choice == 'rock')       or \
             (player_choice == 'scissors'   and computer_choice == 'paper'):
            print(f'Player wins! {player_choice} beats {computer_choice}')
            self.player.wins += 1
        else:
            print(f'Player loses! {player_choice} loses to {computer_choice}')
            self.computer.wins += 1

if __name__ == '__main__':
    game = GameSystem()
    game.play()
#!/usr/bin/env python3
from random import randint

class Player:
    def __init__(self):
        self.deice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3): # make 3 rolls
            self.dice.append(randint(1,6)) # 1 to 6 inclusive random int generated
 
    def get_dice(self): # returns the doce rolls
        return self.dice

def main():
    """called at runtime"""

    # create our players
    player1 = Player()
    player2 = Player()

    # roll the dice
    player1.roll()
    player2.roll()

    print(f"Player 1 rolled {player1.get_dice()}")
    print(f"Player 2 rolled {player2.get_dice()}")

    if sum(player1.get_dice()) == sum(player2.get_dice()):
      print("Draw")
    elif sum(player1.get_dice()) > sum(player2.get_dice()):
      print("Player 1 wins")
    else:
      print("Player 2 wins")

if __name__ == "__main__":
    main()

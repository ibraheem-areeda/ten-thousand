import random
from game_logic import GameLogic

class Game:

    def __init__(self):
        self.round = 1
        self.score = 0
        self.rolls = []
        self.unbanked_points = 0

    def welcome(self):
        start = input("""
Welcome to Ten Thousand
(y)es to play or (n)o to decline 
> """) 
        if start == "y":
            Game.play(self)
        elif start == "n":
            print("OK. Maybe another time")
        else:
            Game.welcome(self)
    
    def print_cheater(self):
        print("Cheater!!! Or possibly made a typo...")
        print("*** " + " ".join(map(str, self.rolls)) + " ***")

    def play(self):
        # rolls = [(2,4,1,4,1,2),(4,4),(1,1,2,5, 1, 6)] #for testing purposes

        while True:
            # self.rolls = Game.mock_roller(rolls) #for testing purposes
            self.rolls = GameLogic.roll_dice(6)
            print(f"Starting round {self.round}")
            print(f"Rolling 6 dice...")
            print("*** " + " ".join(map(str, self.rolls)) + " ***")

            while True:

                if GameLogic.calculate_score(self.rolls) == 0:
                    print("""****************************************
**        Zilch!!! Round over         **
****************************************""")
                    self.unbanked_points = 0
                    print(f"You banked 0 points in round {self.round}")
                    print(f"Total score is {self.score} points")
                    self.round += 1
                    break

                keep = input("""Enter dice to keep, or (q)uit: 
> """)
                if keep.lower() == "q":
                    print(f"Thanks for playing. You earned {self.score} points")
                    return
                if not keep.isdigit():
                    Game.print_cheater(self)
                    continue
    
                keep = tuple(map(int, keep.replace(" ", "")))  # Remove any spaces in the input
                if not GameLogic.validate_keepers(self.rolls, keep):
                    Game.print_cheater(self)
                    continue  # Go back to the beginning of the loop

                scorers = GameLogic.get_scorers(keep)
                if not scorers:
                    Game.print_cheater(self)
                    continue # Go back to the beginning of the loop

                score = GameLogic.calculate_score(keep)
                self.unbanked_points += score
                dice_to_roll = len(self.rolls) - len(keep)
                print(f"You have {self.unbanked_points} unbanked points and {dice_to_roll} dice remaining")

                if len(keep) == 6:  # All dice kept
                    print("Hot dice! Rolling 6 new dice...")
                    self.rolls = GameLogic.roll_dice(6)
                    print("*** " + " ".join(map(str, self.rolls)) + " ***")
                    continue
                
                # self.unbanked_points += GameLogic.calculate_score(keep)

                action = input("""(r)oll again, (b)ank your points or (q)uit: 
> """)
                if action.lower() == "r":
                    dice_to_roll = len(self.rolls) - len(keep)
                    print(f"Rolling {dice_to_roll} dice...")
                    # self.rolls = Game.mock_roller(rolls)
                    self.rolls = GameLogic.roll_dice(dice_to_roll)
                    print("*** " + " ".join(map(str, self.rolls)) + " ***")

                if action.lower() == "q":
                    print(f"Thanks for playing. You earned {self.score} points")
                    return
                elif action.lower() == "b":
                    self.score += self.unbanked_points
                    print(f"You banked {self.unbanked_points} points in round {self.round}")
                    print(f"Total score is {self.score} points")
                    self.round += 1
                    self.unbanked_points = 0

                    break
    @staticmethod
    def mock_roller(rolls):
        return rolls.pop(0) if rolls else GameLogic.roll_dice

if __name__ == "__main__":
    game = Game()
    game.welcome()
import random
from game_logic import GameLogic

class Game:

    def __init__(self):
        self.round = 1
        self.score = 0
        self.rolls = []
        self.unbanked_points = 0

    def play(self):
        while True:
            self.rolls = GameLogic.roll_dice(6)
            print(f"Starting round {self.round}")
            print("Rolling 6 dice...")
            print("*** " + " ".join(map(str, self.rolls)) + " ***")

            while True:
                keep = input("Enter dice to keep, or (q)uit: ")
                if keep.lower() == "q":
                    print(f"Thanks for playing. You earned {self.score} points")
                    return
                
                keep = tuple(map(int, keep))
                self.unbanked_points = GameLogic.calculate_score(keep)
                print(f"You have {self.unbanked_points} unbanked points and {6-len(keep)} dice remaining")

                action = input("(r)oll again, (b)ank your points or (q)uit: ")
                if action.lower() == "q":
                    print(f"Thanks for playing. You earned {self.score} points")
                    return
                elif action.lower() == "b":
                    self.score += self.unbanked_points
                    print(f"You banked {self.unbanked_points} points in round {self.round}")
                    print(f"Total score is {self.score} points")
                    self.round += 1
                    break


if __name__ == "__main__":
    game = Game()
    game.play()

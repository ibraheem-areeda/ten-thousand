import random

class GameLogic:
  
    @staticmethod
    def roll_dice(n):
        """Return a tuple of n random dice rolls."""
        return tuple(random.randint(1, 6) for dice in range(n))

    @staticmethod
    def calculate_score(dice):
        pass
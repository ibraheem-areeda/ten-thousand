import random

class GameLogic:
  
    @staticmethod
    def roll_dice(n):
        """Return a tuple of n random dice rolls."""
        return tuple(random.randint(1, 6) for dice in range(n))

    @staticmethod
    def calculate_score(dice):
        """Calculate the score for a roll of dice."""
        if not dice: # if dice == None return 0, 
            return 0

        counts = []
        for value in range(1, 7):
          counts.append(dice.count(value))
        score = 0

        # Handle 1's and 5's
        score += counts[0] * 100
        score += counts[4] * 50

        # Handle 3 or more of a kind
        for i in range(1, 7):
            if counts[i-1] >= 3:
                if i == 1:
                    score += 1000 * (counts[i-1] // 3)
                else:
                    score += 100 * i * (counts[i-1] // 3)
                counts[i-1] %= 3

        # Handle straight
        if all(count == 1 for count in counts):
            score = 1500

        # Handle 3 pairs
        if len([count for count in counts if count == 2]) == 3:
            score = 1500

        # Handle 2 triplets
        if len([count for count in counts if count == 3]) == 2:
            score = 2500

        return score
        
import random

class GameLogic:

    @staticmethod
    def roll_dice(n):
        """Return a tuple of n random dice rolls."""
        # A list comprehension is used inside a tuple() function to generate n random numbers between 1 and 6.
        # random.randint(1, 6) generates a random integer between 1 and 6.
        # The underscore _ is a convention for a variable that we don't care about its actual value.
        # We do this operation n times, hence for _ in range(n).
        return tuple(random.randint(1, 6) for _ in range(n))

    @staticmethod
    def calculate_score(dice):
        # Returns 0 if the dice tuple is empty or None.
        if not dice: 
            return 0

        # Creates a list that counts the occurrences of each dice value (1 to 6).
        counts = [dice.count(value) for value in range(1, 7)]
        print(counts)
        # Initializes the score to 0.
        score = 0

        
        for i in range(1, 7): # Loops through each possible dice value.
            
            if counts[i-1] >= 3: # Checks if the current value occurs 3 or more times in the dice roll.
                
                if i == 1: # If the current value is 1, adds 1000 points for each set of three 1's.
                    score += 1000 * (counts[i-1] - 2)
                # For any other value, adds 100 times the value for each set of three.
                else:
                    score += 100 * i * (counts[i-1] - 2)
                # If there are more than 3 of a value, only the first 3 count for extra points.
                counts[i-1] %= 3

        # Adds 100 points for each individual 1 (that's not part of a set of three).
        score += counts[0] * 100
        # Adds 50 points for each individual 5 (that's not part of a set of three).
        score += counts[4] * 50

        # If there is exactly one of each value, the score is 1500.
        if all(count == 1 for count in counts):
            score = 1500

        # If there are exactly three pairs, the score is 1500.
        if len([count for count in counts if count == 2]) == 3:
            score = 1500

        # If there are exactly two sets of three of a kind, the score is 2500.
        if len([count for count in counts if count == 3]) == 2:
            score = 2500

        # Returns the final calculated score.
        return score
    
if __name__ == "__main__":
    GameLogic.calculate_score(5)
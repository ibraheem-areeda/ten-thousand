import random

class GameLogic:

    @staticmethod
    def roll_dice(n):
        """
        input : n --> number of dice you want to roll.
        output -----> a tuple of n random dice rolls.
        """
        # A list comprehension is used inside a tuple() function to generate n random numbers between 1 and 6.
        # random.randint(1, 6) generates a random integer between 1 and 6.
        # The underscore _ is a convention for a variable that we don't care about its actual value.
        # We do this operation n times, hence for _ in range(n).
        return tuple(random.randint(1, 6) for _ in range(n))

    @staticmethod
    def calculate_score(dice):
        """
      input : dice ---> list that returned from dice rolls function 
      output -------> integer number represents the score you git from your dice based on the game rules
        """
        
        if not dice: 
            return 0  # Returns 0 if the dice tuple is empty or None.
        
        counts_list = [dice.count(value) for value in range(1, 7)] # Creates a list that counts the occurrences of each dice value (1 to 6).
       #ex: counts = ["count_1s","count_2s","count_3s","count_4s","count_5s","count_6s"]
        score = 0 # Initializes the score to 0.
        value_one_is_counted = False # this variable declared because I will need it later when score calculation for the value of one occurrence
        value_five_is_counted = False # this variable declared because I will need it later when score calculation for the value of five occurrence

        for i in range(1, 7): # Loops through each possible dice value.
            if counts_list[i-1] >= 3: # Checks if the current value occurs 3 or more times in the dice roll.
                if i == 1: # If the current value is 1, adds 1000 points for each set of three 1's.
                    score += 1000 * (counts_list[i-1] - 2) # For any other value, adds 100 times the value for each set of three.
                    value_one_is_counted = True # set to true to prvent recalcuation for the "one" values in the if statment after the loop
                else:
                    score += 100 * i * (counts_list[i-1] - 2) 
                    if i == 5: value_five_is_counted = True # set to true to prvent recalcuation for the "five" values in the if statment after the loop
                counts_list[i-1] %= 3 # If there are more than 3 of a value, only the first 3 count for extra points.
        
        if value_one_is_counted == False : score += counts_list[0] * 100 # Adds 100 points for each individual 1 (that's not part of a set of 3 or set of 4 or set of 5).
        if value_five_is_counted == False :score += counts_list[4] * 50 # Adds 50 points for each individual 5 (that's not part of a set of 3 or set of 4 or set of 5).
        if all(count == 1 for count in counts_list): score = 1500 # If there is exactly one of each value, the score is 1500.
        if len([count for count in counts_list if count == 2]) == 3:score = 1500 # If there are exactly three pairs, the score is 1500.
        if len([count for count in counts_list if count == 3]) == 2:score = 2500 # If there are exactly two sets of three of a kind, the score is 2500.
        
        return score # Returns the final calculated score.
    
    @staticmethod
    def validate_keepers(roll, keepers):
        """
        input : roll ---> tuple representing the rolled dice
                keepers ---> tuple representing the selected dice to keep
        output ---> boolean indicating whether the selected keepers are valid or not
        """
        roll_counts = [roll.count(value) for value in range(1, 7)]
        keepers_counts = [keepers.count(value) for value in range(1, 7)]

        for i in range(1, 7):
            if keepers_counts[i-1] > roll_counts[i-1]:
                return False
        
        return True
    
    @staticmethod
    def get_scorers(dice):
        """
        input : dice ---> tuple representing the rolled dice
        output ---> tuple representing the selected scoring dice
        """
        counts_list = [dice.count(value) for value in range(1, 7)]
        scorers = []

        for i in range(6):
            if counts_list[i] >= 3:
                scorers.extend([i+1] * 3)
        
        scorers.extend([1] * counts_list[0])
        scorers.extend([5] * counts_list[4])

        return tuple(scorers)
    
if __name__ == "__main__":
    print (GameLogic.calculate_score(GameLogic.roll_dice(6)))
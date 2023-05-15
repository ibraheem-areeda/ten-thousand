### prompt-01 : 
> Write me a python code for Handle rolling dice
    Add roll_dice static method to GameLogic class.
    The input to roll_dice is an integer between 1 and 6.
    The output of roll_dice is a tuple with random values between 1 and 6.
    The length of tuple must match the argument given to roll_dice method.


- result : 
```python
    @staticmethod
    def roll_dice(n):
        """Return a tuple of n random dice rolls."""
        return tuple(random.randint(1, 6) for _ in range(n))
```

### prompt-02 :
>  write me a python code for Handle calculating score for dice roll
    Add calculate_score static method to GameLogic class.
    The input to calculate_score is a tuple of integers that represent a dice roll.
    The output from calculate_score is an integer representing the roll's score according to rules of game.


- result : 
```python 
    @staticmethod
    def calculate_score(dice):
        """Calculate the score for a roll of dice."""
        if not dice:
            return 0

        counts = [dice.count(value) for value in range(1, 7)]
        score = 0

        score += counts[0] * 100
        score += counts[4] * 50

        for i in range(1, 7):
            if counts[i-1] >= 3:
                if i == 1:
                    score += 1000 * (counts[i-1] // 3)
                else:
                    score += 100 * i * (counts[i-1] // 3)
                counts[i-1] %= 3

        if all(count == 1 for count in counts):
            score = 1500

        if len([count for count in counts if count == 2]) == 3:
            score = 1500

        if len([count for count in counts if count == 3]) == 2:
            score = 2500

        return score
```

### prompt-03 :
> can you write it in simpler way without using comprehinsive? counts = [dice.count(value) for value in range(1, 7)]

- result : 
```python 
counts = []
for value in range(1, 7):
    count = dice.count(value)
    counts.append(count)
```

### prompt-04 :
> the code is failing because the score for the 1's and 5's is being counted twice. Once as individual scores and once as three of a kind. reduce the count of 1's and 5's before you calculate the score for individual 1's and 5's. This should be done after the loop where you calculate the score for three of a kind.
the scoring for four, five, and six of a kind is not implemented correctly. According to the rules, the score should be double for each additional dice beyond three of a kind. This means four of a kind should be double the score of three of a kind, five of a kind should be quadruple, and six of a kind should be octuple.

- result : 
```python 
    @staticmethod
    def calculate_score(dice):
        if not dice: 
            return 0

        counts = []
        for value in range(1, 7):
            count = dice.count(value)
            counts.append(count)
        score = 0

        for i in range(1, 7):
            if counts[i-1] >= 3:
                if i == 1:
                    score += 1000 * (2 ** (counts[i-1] - 3))  # Double the score for each dice beyond 3
                else:
                    score += 100 * i * (2 ** (counts[i-1] - 3))
                counts[i-1] %= 3

        score += counts[0] * 100  # Score for individual 1's
        score += counts[4] * 50  # Score for individual 5's

        if all(count == 1 for count in counts):
            score = 1500

        if len([count for count in counts if count == 2]) == 3:
            score = 1500

        if len([count for count in counts if count == 3]) == 2:
            score = 2500

        return score

```
### prompt-05 :
>  the scoring rules for four, five, and six of a kind. The score should be doubled for each additional dice beyond three of a kind, but the initial score for three of a kind should not be doubled. This means four of a kind should be twice the score of three of a kind, five of a kind should be three times, and six of a kind should be four times the score of three of a kind.

- result : 
```python 
    @staticmethod
    def calculate_score(dice):
        if not dice: 
            return 0

        counts = []
        for value in range(1, 7):
            count = dice.count(value)
            counts.append(count)
        score = 0

        for i in range(1, 7):
            if counts[i-1] >= 3:
                if i == 1:
                    score += 1000 * (counts[i-1] - 2)  # score is multiplied by the number of dice beyond 2
                else:
                    score += 100 * i * (counts[i-1] - 2)
                counts[i-1] %= 3

        score += counts[0] * 100  # Score for individual 1's
        score += counts[4] * 50  # Score for individual 5's

        if all(count == 1 for count in counts):
            score = 1500

        if len([count for count in counts if count == 2]) == 3:
            score = 1500

        if len([count for count in counts if count == 3]) == 2:
            score = 2500

        return score

```
### prompt-06 :
> Add this function and the roll dice function to class GameLogic

- result : 
```python 
class GameLogic:

    @staticmethod
    def roll_dice(n):
        return tuple(random.randint(1, 6) for _ in range(n))

    @staticmethod
    def calculate_score(dice):
        if not dice: 
            return 0

        counts = []
        for value in range(1, 7):
            count = dice.count(value)
            counts.append(count)
        score = 0

        for i in range(1, 7):
            if counts[i-1] >= 3:
                if i == 1:
                    score += 1000 * (counts[i-1] - 2)  # score is multiplied by the number of dice beyond 2
                else:
                    score += 100 * i * (counts[i-1] - 2)
                counts[i-1] %= 3

        score += counts[0] * 100  # Score for individual 1's
        score += counts[4] * 50  # Score for individual 5's

        if all(count == 1 for count in counts):
            score = 1500

        if len([count for count in counts if count == 2]) == 3:
            score = 1500

        if len([count for count in counts if count == 3]) == 2:
            score = 2500

        return score
```
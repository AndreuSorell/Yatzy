class Yatzy:
    
    def __init__(self, *dices):
        self.dices = list(dices)

    @staticmethod
    def chance(*dices):
        total = 0
        for dice in dices:
            total += dice
        return total

    @staticmethod
    def yatzy(*dices):
        if dices.count(dices[0]) == 5:
            return 50
        return 0
    
    @staticmethod
    def ones(*dices):
        return dices.count(1)
    

    @staticmethod
    def twos(*dices):
        return dices.count(2) * 2
    
    @staticmethod
    def threes(*dices):
        return dices.count(3) * 3
    
    def fours(self):
        return self.dices.count(4) * 4

    def fives(self):
        return self.dices.count(5) * 5

    def sixes(self):
        return self.dices.count(6) * 6
    
    @staticmethod
    def pair(*dices):
        pairs = [0]*6
        for dice in dices:
            pairs[dice-1] += 1
        for num in range(6):
            if (pairs[6-num-1] >= 2):
                return (6-num)*2
        return 0
    
    @staticmethod
    def two_pairs(*dices):
        pairs = [0]*6
        for dice in dices:
            pairs[dice-1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (pairs[6-i-1] >= 2):
                n += 1
                score += (6-i)
        if (n == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def three_of_a_kind(*dices):
        for dice in range(6):
            if dices.count(dice) >= 3:
                return dice * 3
        return 0

    @staticmethod
    def four_of_a_kind(*dices):
        for dice in range(6):
            if dices.count(dice) >= 4:
                return dice * 4
        return 0

    @staticmethod
    def smallStraight( dice1,  dice2,  dice3,  dice4,  dice5):
        tallies = [0]*6
        tallies[dice1-1] += 1
        tallies[dice2-1] += 1
        tallies[dice3-1] += 1
        tallies[dice4-1] += 1
        tallies[dice5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( dice1,  dice2,  dice3,  dice4,  dice5):
        tallies = [0]*6
        tallies[dice1-1] += 1
        tallies[dice2-1] += 1
        tallies[dice3-1] += 1
        tallies[dice4-1] += 1
        tallies[dice5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( dice1,  dice2,  dice3,  dice4,  dice5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[dice1-1] += 1
        tallies[dice2-1] += 1
        tallies[dice3-1] += 1
        tallies[dice4-1] += 1
        tallies[dice5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
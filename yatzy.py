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
    def yatzy(dice):
        counts = [0]*(len(dice)+1)
        for die in dice:
            counts[die-1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0
    
    @staticmethod
    def ones( dice1,  dice2,  dice3,  dice4,  dice5):
        sum = 0
        if (dice1 == 1):
            sum += 1
        if (dice2 == 1):
            sum += 1
        if (dice3 == 1):
            sum += 1
        if (dice4 == 1):
            sum += 1
        if (dice5 == 1): 
            sum += 1

        return sum
    

    @staticmethod
    def twos( dice1,  dice2,  dice3,  dice4,  dice5):
        sum = 0
        if (dice1 == 2):
             sum += 2
        if (dice2 == 2):
             sum += 2
        if (dice3 == 2):
             sum += 2
        if (dice4 == 2):
             sum += 2
        if (dice5 == 2):
             sum += 2
        return sum
    
    @staticmethod
    def threes( dice1,  dice2,  dice3,  dice4,  dice5):
        s = 0
        if (dice1 == 3):
             s += 3
        if (dice2 == 3):
             s += 3
        if (dice3 == 3):
             s += 3
        if (dice4 == 3):
             s += 3
        if (dice5 == 3):
             s += 3
        return s


    
    def fours(self):
        sum = 0
        for at in range(5):
            if (self.dices[at] == 4): 
                sum += 4
        return sum
    

    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dices)): 
            if (self.dices[i] == 5):
                s = s + 5
        return s
    

    def sixes(self):
        sum = 0
        for at in range(len(self.dices)): 
            if (self.dices[at] == 6):
                sum = sum + 6
        return sum
    
    @staticmethod
    def score_pair( dice1,  dice2,  dice3,  dice4,  dice5):
        counts = [0]*6
        counts[dice1-1] += 1
        counts[dice2-1] += 1
        counts[dice3-1] += 1
        counts[dice4-1] += 1
        counts[dice5-1] += 1
        at = 0
        for at in range(6):
            if (counts[6-at-1] == 2):
                return (6-at)*2
        return 0
    
    @staticmethod
    def two_pair( dice1,  dice2,  dice3,  dice4,  dice5):
        counts = [0]*6
        counts[dice1-1] += 1
        counts[dice2-1] += 1
        counts[dice3-1] += 1
        counts[dice4-1] += 1
        counts[dice5-1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6-i-1] >= 2):
                n = n+1
                score += (6-i)
                    
        if (n == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind( _1,  _2,  dice3,  dice4,  dice5):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[dice3-1] += 1
        tallies[dice4-1] += 1
        tallies[dice5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0
    

    @staticmethod
    def three_of_a_kind( dice1,  dice2,  dice3,  dice4,  dice5):
        t = [0]*6
        t[dice1-1] += 1
        t[dice2-1] += 1
        t[dice3-1] += 1
        t[dice4-1] += 1
        t[dice5-1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
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
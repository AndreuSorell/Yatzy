class Yatzy:
    
    def __init__(self, *dices):
        self.dices = list(dices)

    @staticmethod
    def chance(*dices):
        total = 0
        for pip in dices:
            total += pip
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
        for pip in dices:
            pairs[pip-1] += 1
        for num in range(6):
            if (pairs[6-num-1] >= 2):
                return (6-num)*2
        return 0
    
    @staticmethod
    def two_pairs(*dices):
        pairs = [0]*6
        for pip in dices:
            pairs[pip-1] += 1
        n = 0
        score = 0
        for num in range(6):
            if (pairs[6-num-1] >= 2):
                n += 1
                score += (6-num)
        if (n == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def three_of_a_kind(*dices):
        for pip in range(6):
            if dices.count(pip) >= 3:
                return pip * 3
        return 0

    @staticmethod
    def four_of_a_kind(*dices):
        for pip in range(6):
            if dices.count(pip) >= 4:
                return pip * 4
        return 0

    @staticmethod
    def small_straight(*dices):
        for die, pip in enumerate(sorted(dices), 1):
            if die != pip:
                return 0
        return 15
        # return [0 for die, pip in enumerate(sorted(dices), 1) if die != pip else 15]

    @staticmethod
    def large_straight(*dices):
        for die, pip in enumerate(sorted(dices), 2):
            if die != pip:
                return 0
        return 20
    
    @staticmethod
    def full_house(*dices):
        pair = False
        three = False
        score = 0
        full = [0]*6
        for pip in dices:
            full[pip-1] += 1
        for num in range(6):
            if (full[num] == 2): 
                pair = True
                score += (num+1) *2
        for num in range(6):
            if (full[num] == 3): 
                three = True
                score += (num+1) * 3
        if (pair and three):
            return score
        else:
            return 0
from pips import Pips
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
        ONE = Pips.ONE.value
        return dices.count(ONE)
    
    @staticmethod
    def twos(*dices):
        TWO = Pips.TWO.value
        return dices.count(TWO) * TWO
    
    @staticmethod
    def threes(*dices):
        THREE = Pips.THREE.value
        return dices.count(THREE) * THREE

    def fours(self):
        FOUR = Pips.FOUR.value
        return self.dices.count(FOUR) * FOUR

    def fives(self):
        FIVE = Pips.FIVE.value
        return self.dices.count(FIVE) * FIVE

    def sixes(self):
        SIX = Pips.SIX.value
        return self.dices.count(SIX) * SIX
    
    @staticmethod
    def pair(*dices):
        PAIR = 2
        for pip in Pips.sorted_values():
            if dices.count(pip) >= PAIR:
                return PAIR * pip
        return 0

    @classmethod
    def __filter_pips_repeated(cls, dices, times):
        return list(filter(lambda pip: dices.count(pip) >= times, Pips.sorted_values()))
    
    @classmethod
    def two_pairs(cls, *dices):
        PAIR = 2
        pips_pairs = cls.__filter_pips_repeated(dices, PAIR)
        return sum(pips_pairs) * PAIR if len(pips_pairs) == 2 else 0
    
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
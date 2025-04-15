
import unittest

from typing import List
import random

# Mocking Yatzy class with manual dice control for testing
class Yatzy:
    def __init__(self, dice: List[int] = None):
        self.dice = dice if dice else [random.randint(1, 6) for _ in range(5)]
        self.locked = [False] * 5

    def roll(self):
        for i in range(5):
            if not self.locked[i]:
                self.dice[i] = random.randint(1, 6)
        return self.dice

    def toggle_lock(self, index):
        self.locked[index] = not self.locked[index]

    def Ones(self): return self.dice.count(1) * 1
    def Twos(self): return self.dice.count(2) * 2
    def Threes(self): return self.dice.count(3) * 3
    def Fours(self): return self.dice.count(4) * 4
    def Fives(self): return self.dice.count(5) * 5
    def Sixes(self): return self.dice.count(6) * 6

    def OnePair(self):
        counts = [self.dice.count(val) for val in range(1, 7)]
        pairs = [val * 2 for val, count in enumerate(counts, 1) if count >= 2]
        return max(pairs) if pairs else 0

    def TwoPairs(self):
        counts = [self.dice.count(val) for val in set(self.dice)]
        pairs = [val for val, count in zip(set(self.dice), counts) if count >= 2]
        return sum(pairs) * 2 if len(pairs) == 2 else 0

    def ThreeAlike(self):
        for val in set(self.dice):
            if self.dice.count(val) >= 3:
                return val * 3
        return 0

    def FourAlike(self):
        for val in set(self.dice):
            if self.dice.count(val) >= 4:
                return val * 4
        return 0

    def Small(self): return 15 if sorted(self.dice) == [1, 2, 3, 4, 5] else 0
    def Large(self): return 20 if sorted(self.dice) == [2, 3, 4, 5, 6] else 0

    def FullHouse(self):
        counts = sorted([self.dice.count(val) for val in set(self.dice)])
        return sum(self.dice) if counts == [2, 3] else 0

    def Chance(self): return sum(self.dice)
    def Yatzy(self): return 50 if len(set(self.dice)) == 1 else 0


class TestYatzy(unittest.TestCase):
    def test_ones(self): self.assertEqual(Yatzy([1, 1, 2, 4, 6]).Ones(), 2)
    def test_twos(self): self.assertEqual(Yatzy([2, 2, 2, 4, 6]).Twos(), 6)
    def test_threes(self): self.assertEqual(Yatzy([3, 3, 4, 5, 6]).Threes(), 6)
    def test_fours(self): self.assertEqual(Yatzy([4, 4, 4, 5, 6]).Fours(), 12)
    def test_fives(self): self.assertEqual(Yatzy([5, 5, 5, 5, 6]).Fives(), 20)
    def test_sixes(self): self.assertEqual(Yatzy([6, 6, 1, 2, 3]).Sixes(), 12)
    
    def test_one_pair(self): self.assertEqual(Yatzy([1, 2, 3, 4, 4]).OnePair(), 8)
    def test_two_pairs(self): self.assertEqual(Yatzy([1, 1, 2, 2, 5]).TwoPairs(), 6)
    def test_two_pairs_fail(self): self.assertEqual(Yatzy([1, 1, 1, 2, 3]).TwoPairs(), 0)
    
    def test_three_of_a_kind(self): self.assertEqual(Yatzy([3, 3, 3, 2, 1]).ThreeAlike(), 9)
    def test_four_of_a_kind(self): self.assertEqual(Yatzy([4, 4, 4, 4, 5]).FourAlike(), 16)
    def test_small_straight(self): self.assertEqual(Yatzy([1, 2, 3, 4, 5]).Small(), 15)
    def test_large_straight(self): self.assertEqual(Yatzy([2, 3, 4, 5, 6]).Large(), 20)
    def test_full_house(self): self.assertEqual(Yatzy([2, 2, 3, 3, 3]).FullHouse(), 13)
    def test_chance(self): self.assertEqual(Yatzy([1, 2, 3, 4, 5]).Chance(), 15)
    def test_yatzy(self): self.assertEqual(Yatzy([6, 6, 6, 6, 6]).Yatzy(), 50)


# Run the tests and collect output
unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(TestYatzy))


from src.stream import DataStream
from src.Misra_Gries import MG
from src.universalHashing import UniversalHash

import unittest

class TestMisra_Gries(unittest.TestCase):
    def setUp(self):
        self.mg = MG(4)
        self.seq = {}
        self.d = DataStream({'A': 1, 'B': 5, 'C': 100, 'D': 100}, 500)

    def test_frequency(self):
        for x in self.d:
            self.seq.setdefault(x, 0)
            self.seq[x] += 1
            self.mg.process(x)
        _sum = sum(self.seq.values()) + 0.0
        for x in self.seq.keys():
            ef = self.mg.frequency(x)
            f = self.seq[x]
            self.assertTrue(f - _sum / self.mg._k <= ef <= f)

class TestUniversalHash(unittest.TestCase):
    def setUp(self):
        uhash = UniversalHash(1000)
        self.hs = uhash.pickHash()
        
    def test_calc(self):
        for x in range(10):
            self.assertTrue(self.hs._calc(x + 100) == self.hs._calc(x + 100))
            

if __name__ == '__main__':
    unittest.main()

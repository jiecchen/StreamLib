from src.stream import DataStream
from src.Misra_Gries import MG
from src.universalHashing import UniversalHash

import unittest
import random
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
        self.uhash = UniversalHash(100)
        
        
    def test_calc(self):
        random.seed()
        x = random.choice(['xxxx1', 'sd2', 'zz3', 'www4', 'ddd5'])
        y = x + "dsfaeare"
        # hs = self.uhash.pickHash()
        # self.assertTrue(hs.hash(x) == hs.hash(x))
        ct = 0
        for i in range(3 * self.uhash._M):
            hs = self.uhash.pickHash()
            if hs.hash(x) == hs.hash(y):
                ct += 1
        print ct
        self.assertTrue((ct + 0.) / self.uhash._M <= 4. / self.uhash._M)
            

if __name__ == '__main__':
    unittest.main()

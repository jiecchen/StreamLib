from streamlib.stream import DataStream
from streamlib.Misra_Gries import MG
from streamlib.hashes.universalHashing import UniversalHash

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
        self.uhash = UniversalHash(300)
        
        
    def test_hash(self):
        random.seed()
        x = random.choice(['xxxx1', 'sd2', 'zz3', 'www4', 'ddd5'])
        y = x + "dsfaeare"
        # hs = self.uhash.pickHash()
        # self.assertTrue(hs.hash(x) == hs.hash(x))
        ct = 0
        for i in range(10 * self.uhash._M):
            hs = self.uhash.pickHash()
            if hs.hash(x) == hs.hash(y):
                ct += 1
            # self.assertTrue(hs.hash(x) < hs._M)
            # self.assertTrue(hs.hash(y) < hs._M)
        self.assertTrue((ct + 0.) / self.uhash._M <= 20. / self.uhash._M)
        
from streamlib.utils import zeros, CountBits
class Test_Utils(unittest.TestCase):
    def setUp(self):
        pass
    def test_zeros(self):
        for i in range(20):
            self.assertTrue(zeros(1 << i) == i)
        self.assertTrue(zeros(0) == 0)
    
    def test_CountBits(self):
        self.assertEqual(31, CountBits((1 << 31) - 1))

from streamlib.BJKST import BJKST
class Test_BJKST(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_getEstimation(self):
        d = DataStream(list("qwertyuiopasdfghjklzxcvbnm"), 1000)
        sketch = BJKST(26, 0.2, 0.001)
        for x in d:
            sketch.process(x)
        self.assertTrue( 26 * 0.8 <= sketch.getEstimation() <= 26 * 1.2)
        

if __name__ == '__main__':
    unittest.main()

from streamlib.stream import DataStream
import math
import unittest
import random

from streamlib.sketch.Misra_Gries import MG
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


from streamlib.hashes.universalHashing import UniversalHash
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

        uhash = UniversalHash(4)
        hs = uhash.pickHash()
        for i in range(10):
            self.assertTrue(hs.hash(('a', random.random())) < 4)
        
from streamlib.utils import zeros, CountBits, unionDict
class Test_Utils(unittest.TestCase):
    def setUp(self):
        pass
    def test_zeros(self):
        for i in range(20):
            self.assertTrue(zeros(1 << i) == i)
        self.assertTrue(zeros(0) == 0)
    
    def test_CountBits(self):
        self.assertEqual(31, CountBits((1 << 31) - 1))

    def test_unionDict(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 1, 'a': 5}
        self.assertTrue(unionDict(d1, d2) == {'a':6, 'b':2, 'c':1})

from streamlib.sketch.BJKST import BJKST
class Test_BJKST(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_getEstimation(self):
        d = DataStream(list("qwertyuiopasdfghjklzxcvbnm"), 1000)
        sketch = BJKST(26, 0.2, 0.001)
        for x in d:
            sketch.process(x)
        # self.assertTrue( 26 * 0.8 <= sketch.getEstimation() <= 26 * 1.2)
        

from streamlib.sketch.countSketch import CountSketch
class Test_CountSketch(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_getEstimation(self):
        dist = {'a': 10, 'b': 1, 'd': 14, 'c': 20}
        d = DataStream(dist, 1000)
        hs = CountSketch(0.1, 0.001)
        ct = {}
        tot = 0
        for x in d:
            tot += 1
            hs.process(x)
            ct.setdefault(x, 0)
            ct[x] += 1
        for elem in dist.keys():
            self.assertTrue(abs(hs.getEstimation(elem) - ct[elem]) <= 0.1 * (tot - ct[elem]))


if __name__ == '__main__':
    unittest.main()

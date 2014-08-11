from sketch import Sketch, BasicEstimator
from streamlib.wrappers import inherit_docs
from streamlib.hashes.universalHashing import UniversalHash
from streamlib.utils import median

@inherit_docs
class _F2_estimator(BasicEstimator):
    """  Basic estimator for 2-frequencey moment """
    
    def __init__(self, uhash):
        self.h = uhash.pickHash()
        self.x = 0

    def process(self, itm):
        try:
            i, c = itm
        except (ValueError, TypeError):
            i = itm
            c = 1
        self.x += c * (1 - 2 * self.h.hash(i))

    def getEstimation(self):
        return self.x ** 2

    def merge(self, skc):
        self.x += skc.x

import math
@inherit_docs
class F2(Sketch):
    def __init__(self, eps, delta = 0.001):
        n = int(1 + 1 / eps**2)
        m = int(math.log(1/delta, 2) + 1)
        uhash = UniversalHash(2)
        self.n = n
        self.m = m
        self.estimators = [ [ _F2_estimator(uhash) for j in range(n)] for i in range(m) ]
    
    def process(self, itm):
        for arr in self.estimators:
            for est in arr:
                est.process(itm)
            
    def _mean(self, arr):
        """ given an array of BsicEstimators,
        return the mean of their estimations """
        return sum([est.getEstimation() for est in arr]) / float(len(arr))

    def getEstimation(self):
        return median([self._mean(arr) for arr in self.estimators])
        
    def merge(self, skc):
        for i in range(self.m):
            for j in range(self.n):
                self.estimators[i][j].merge(skc.estimators[i][j])

from streamlib.sketch.sketch import Sketch, BasicEstimator
from streamlib.hashes.universalHashing import UniversalHash
from streamlib.utils import zeros, median
from streamlib.wrappers import inherit_docs
import math
import random


@inherit_docs
class _CountSketch_estimator(BasicEstimator):
    """ Basic estimator for Count Sketch """
    def __init__(self, k, uhash_h, uhash_g):
        """  
        @args
        eps      :  control accuracy
        uhash_h  : an instance of random.Random
        """
        self.k = k
        self.C = [0 for i in range(self.k)]
        self.h = uhash_h.pickHash()
        self.g = uhash_g.pickHash()
    
    def process(self, key):
        self.C[self.h.hash(key)] +=  1 - 2 * self.g.hash(key)
        

    def getEstimation(self, key):
        return (1 - 2 * self.g.hash(key)) * self.C[self.h.hash(key)]
    

    def merge(self, skc):
        pass
        
        

@inherit_docs
class CountSketch(Sketch):
    def __init__(self, eps, delta = 0.01):
        """
        @args
        @return
        """
        k = 3. * eps**(-2)
        # make sure self.k in the form 2^m
        self.k = 1 << (int(math.log(k, 2)) + 1)
        uhash_h = UniversalHash(self.k)
        uhash_g = UniversalHash(2)
        n_hash = int(math.log(1. / delta, 2)) + 1
        self.estimators = [_CountSketch_estimator(self.k, uhash_h, uhash_g) for i in range(n_hash)]


    def process(self, key):
        """ process the key """
        for est in self.estimators:
            est.process(key)


    def getEstimation(self, key):
        """ return the (eps, delta)-approximation """
        return median( [est.getEstimation(key) for est in self.estimators] )


    def merge(self, skc):
        pass

from universalHashing import UniversalHash
from utils import zeros, median
import math
class _BJKST_Estimator:
    """
    Basic BJKST-Estimator to esimate # of distinct elements in a data stream.
    It gives a (eps, O(1))-approximation, and the "Constant Probability" can
    be amplified to high probability using Median Trick
    """
    def __init__(self, eps, thresh, uhash_h, uhash_g):
        """
        @args
        eps  : constrol the quality of estimation
        n    : the size of the universe
        uhash_x: a universal hash family to pick hash function x
        """
        self.h = uhash_h.pickHash()
        self.g = uhash_g.pickHash()
        self.z = 0
        self.B = {}
        self.thresh = thresh
        # print self.thresh


    def process(self, key):
        """ process the given item """
        hs = zeros(self.h.hash(key))
        if hs >= self.z:
            self.B[self.g.hash(key)] = hs
        
        while len(self.B) >= self.thresh:
            self.z += 1
            self.B = {k:v for k, v in self.B.items() if v >= self.z}

    def getEstimation(self):
        """
        return a integer as an (eps, O(1))-approximation of #
        of distinct elements in the data stream
        """
        return len(self.B) * (2**self.z)





class BJKST:
    def __init__(self, n, eps, delta = 0.01):
        uhash_h = UniversalHash(n)
        uhash_g = UniversalHash(int(math.log(n, 2)**2 * eps**(-4)))
        thresh = eps**(-2)
        n_hash = int(math.log(1. / delta)) + 1
        # print "n_hash = ", n_hash
        self.estimators = [_BJKST_Estimator(eps, thresh, uhash_h, uhash_g) for i in range(n_hash)]
    
    def process(self, key):
        for est in self.estimators:
            est.process(key)
            
    def getEstimation(self):
        return median( [est.getEstimation() for est in self.estimators] )















from streamlib.hashes.universalHashing import UniversalHash
from streamlib.utils import zeros, median, unionDict
from sketch import Sketch, BasicEstimator
from streamlib.wrappers import inherit_docs
import math


@inherit_docs
class _BJKST_Estimator(BasicEstimator):
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

    def _shrinkB(self):
        while len(self.B) >= self.thresh:
            self.z += 1
            self.B = {k:v for k, v in self.B.items() if v >= self.z}


    def process(self, key):
        """ process the given item """
        hs = zeros(self.h.hash(key))
        if hs >= self.z:
            self.B[self.g.hash(key)] = hs
        
        
    def getEstimation(self):
        """
        return a integer as an (eps, O(1))-approximation of #
        of distinct elements in the data stream
        """
        return len(self.B) * (2**self.z)

    
    def merge(self, skc):
        self.B = unionDict(self.B, skc.B)
        self._shrinkB()



@inherit_docs
class BJKST(Sketch):
    """
    BJKST sketch for estimation the distinct frequency.
    Algorithm and Analysis can be found in:
    http://www.cs.dartmouth.edu/~ac/Teach/CS49-Fall11/Notes/lecnotes.pdf
    or 
    https://github.com/jiecchen/references/blob/master/lecnotes.pdf

    Usage:
    @args
    n           :  the size of universe
    eps, delta  :  control the quality of estimation
    @return
    BJKST(n, eps, delta) returns  an (eps, delta) - BJKST sketch with para eps and delta.

    Example:
    ------------------
    d = DataStream(list("qwertyuiopasdfghjklzxcvbnm"), 1000)
    sketch = BJKST(26, 0.1, 0.001)
    for x in d:
        sketch.process(x)
    print sketch.getEstimation()
    ------------------
    """
    def __init__(self, n, eps, delta = 0.01):
        """
        @args
        n    :  the size of universe
        eps, delta: control the quality of estimation
        @return
        BJKST(n, eps, delta) returns  an (eps, delta) - BJKST sketch with para eps and delta.
        """
        uhash_h = UniversalHash(n)
        uhash_g = UniversalHash(int(math.log(n, 2)**2 * eps**(-4)))
        thresh = eps**(-2)
        n_hash = int(math.log(1. / delta)) + 1
        # print "n_hash = ", n_hash
        self.estimators = [_BJKST_Estimator(eps, thresh, uhash_h, uhash_g) for i in range(n_hash)]
    
    def process(self, key):
        """ process the key """
        for est in self.estimators:
            est.process(key)

            
    def getEstimation(self):
        """ return the (eps, delta)-approximation """
        return median( [est.getEstimation() for est in self.estimators] )

    def merge(self, skc):
        """ To be check """
        un = zip(self.estimators, skc.estimators)
        self.estimators = [u.merge(v) for u, v in un]

        












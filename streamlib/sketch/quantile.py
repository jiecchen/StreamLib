# Algorithm Designed by myself

from sketch import Sketch
from bisect import bisect_left, bisect_right


class Quantile(Sketch):
    """
    Deterministic single pass approximate algorithm for quantile problem
    in streaming model. Mergable sketch.
    
    Usage:
    q = Quantile(eps, a, b) requires all items appeares in the data stream is in [a, b]
    q.getEstimation(k) then return an (1 + eps)-approximation to the k_th smallest item
    in the data stream.
    Example:
    --------------
    >>> q = Quantile(0.001, 0, 100.0)
    >>> d = [1, 2, 3, 4, 1, 1, 100, 2, 5, 8]
    >>> q.batchProcess(d)
    >>> print q.getEstimation(4) 
    2.00251528703
    -------------
    """
    # when all items \in [a, b + n]
    # Space usage: O(log n / eps) to give (1 + eps) - approximation
    # Processing time per item: O(log log n - log eps) 
    # Time per query: O(log n / eps) -- reasonable because # of queries << # of items


    def __init__(self, eps, a, b):
        t = a 
        # a_i = a -1 + (1 + eps)^i
        # C_i : # of < a_i
        self.a = []
        self.C = []
        self.n = 0
        b = a + 2 * (b - a)
        while t <= b:
            self.a.append(t)
            self.C.append(0)
            t = (t - a + 1) * (1 + eps) + a - 1

    def process(self, itm):
        """
        process an item in the data stream
        """
        try:
            i, c = itm
        except (ValueError, TypeError):
            i = itm
            c = 1
        self.n += c
        pos = bisect_right(self.a, i)
        self.C[pos] += c
        

    def getEstimation(self, k):
        """ Given k, return k_th smallest number ever appeared """
        if k < 1 or k > self.n:
            raise ValueError("k should be an int and between [1, n]!")
        cum = 0
        i = 0
        while cum < k:
            cum += self.C[i]
            i += 1
        return self.a[i - 1]


    def merge(self, skc):
        for i in range(len(self.a)):
            self.C[i] += skc.C[i]
        self.n +=  skc.n














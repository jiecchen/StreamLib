from interface import MergeableSketch
import math
from array import array
from hashes import MurmurHash

class CountMinInt(MergeableSketch):
    """
    Basic version of Count-Min Sketch, only support data stream consist of integers
    """

    def __init__(self, double eps=0.1, double fail_prob=0.01):
        """
        The relative error of the estimation is bounded by eps
        Args:
            eps:  relative error
            fail_prob: default=0.01
        """
        cdef int _mu, _w
        # set number of copies
        if 0. < fail_prob < 1:
            _mu = int(3 * math.log(1. / fail_prob))
        else:
            _mu = 10
        self._mu = _mu

        # set eps
        if 0. < eps < 1.:
            _w = int(2. / eps)
        else:
            _w = 20
        self._w = _w

        # create sketches and hash functions
        self._sketch = [array('i', [0] * _w) for i in xrange(_mu)]
        self._hashes = [MurmurHash() for i in xrange(_mu)]

    def process_item(self, int item):
        """
        process an item (int)
        Args:
            item: the given item, should be int

        Returns: none
        """
        cdef int pos
        for i in xrange(self._mu):
            # where the item is mapped by the i_th hash
            pos = self._hashes[i].hash(item) % self._w
            # increment the bucket
            self._sketch[i][pos] += 1

    def merge(self, other_sketch):
        pass

    def estimate(self, int item):
        """
        Given an item, return its estimated frequency
        Args:
            item: the given item, should be int

        Returns: the estimated frequency of the given item

        """
        all_estimators = [self._sketch[i][self._hashes[i].hash(item) % self._w]
                          for i in xrange(self._mu)]
        return min(all_estimators)
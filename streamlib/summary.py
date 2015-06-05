"""

"""
from hashes import MurmurHash

class CountMin:
    """
    Count-Min sketch.
    """
    def __init__(self, w=20, mu=5):
        """
        Create a new instance of CountMin.

        :param w: The number of buckets.
        :type w: int

        :param mu: The number of repeated copies. Used to control the
                   failure probability ~= 2^{-mu}
        :type mu: int
        """
        self._w = w
        self._mu = mu
        self._sketch = [[0] * w for i in xrange(mu)]
        self._hashes = [MurmurHash() for i in xrange(mu)]

    def process(self, dataStream, weighted=False):
        """
        Summarize the given data stream.

        :param dataStream: any iterable object with hashable elements. 
                           e.g. a list of integers.
        :param weighted: if weighted, each item in dataStream should
                         be (key, weight) pair, where weight > 0
        """
        for item in dataStream:
            for i in xrange(self._mu):
                # where the item is mapped by the i_th hash
                pos = self._hashes[i].hash(item) % self._w
                # increment the bucket
                self._sketch[i][pos] += 1

    
    def estimate(self, item):
        """
        Estimate the frequency of given item.

        :param item: same type as elements in dataStream
        
        :return: estimated frequency of the given item.
        :rtype: int/real
        """
        all_estimators = [self._sketch[i][self._hashes[i].hash(item) % self._w]
                          for i in xrange(self._mu)]
        return min(all_estimators)



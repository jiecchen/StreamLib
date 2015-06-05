"""

"""
import mmh3

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

    def process(self, dataStream):
        """
        Summarize the given data stream.

        :param dataStream: any iterable, hashable object. e.g. a list
        """
        for item in dataStream:
            
    



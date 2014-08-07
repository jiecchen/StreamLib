from collections import Iterable
_Default_Distribution = [0, 1]


from bisect import bisect_left
import random
class Distribution:
    """
    The class to represent a distribution
    """
    def __init__(self, _dict = _Default_Distribution):
        # if _dict is a list, use uniform distribution
        if isinstance(_dict, list):
            _dc = {}
            for x in _dict: 
                _dc[x] = 1.0
            _dict = _dc
        self._dict = _dict

        # use private coin for each instance
        self._random = random.Random()        
        self._random.seed()
        self._dict = {}
        self._index = [0]
        cumm = 0.
        for key, value in _dict.items():
            self._dict[cumm] = key
            cumm += value
            self._index.append(cumm)
        # normalization factor
        self._cumm = cumm

    
    def getSample(self):
        """
        Usage:
        >>> d = Distribution({'A': 0.1, 'B': 0.9})
        >>> print d.getSample()
        A
        """
        rd = self._random.random() * self._cumm
        pos = bisect_left(self._index, rd)
        return self._dict[self._index[pos - 1]]
        



class DataStream:
    """
    The class for data stream, defined as an iterator

    Example 1:
    >>> d = DataStream([1, 2, 3, 4], 10)
    >>> for s in d:
    ...    print s
    
    """
    def __init__(self, _distribution=None, _size = 100):
        self._size = _size
        self._distribution = Distribution(_distribution)

    def __iter__(self):
        return self

    def next(self):
        if self._size <= 0:
            raise StopIteration
        self._size -= 1
        return self._distribution.getSample()

_Default_Distribution = [0, 1]


from bisect import bisect_left
from abc import abstractmethod, ABCMeta
from wrappers import inherit_docs
import random

class ABDataSrteam:
    """ Interface for Abstract DataStream """
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def next(self):
        """ return next item in the DataStream """
        pass
        
    @abstractmethod
    def __iter__(self):
        pass










# TODO: + extend to continuous distribution
#       + add more flexible constructors
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
        


# TODO: + turnstile model 
#       + strict turnstile model 
#       + cash register model

class Turnstile(ABDataSrteam):
    """ 
    An iterator of Turrnstile model,
    return (a_i, w_i) each time 
    here w_i = weightFunc(a_i) and weightFunc can be a stochastic function
    """
    def __init__(self, distribution=None, weightFunc = 1,  size = 100):
        # function used to construct the weight for each item
        if weightFunc == 0:
            self.weightFunc = lambda x: 1
        else:
            self.weightFunc = weightFunc

        self._size = size
        self._distribution = Distribution(distribution)

    def __iter__(self):
        return self

    def next(self):
        if self._size <= 0:
            raise StopIteration
        self._size -= 1
        sp = self._distribution.getSample()
        return (sp, self.weightFunc(sp))











@inherit_docs
class DataStream(ABDataSrteam):
    """
    The class for data stream, defined as an iterator

    Example 1:
    >>> d = DataStream([1, 2, 3, 4], 10)
    >>> for s in d:
    ...    print s
    
    """
    def __init__(self, distribution=None, size = 100, model = 'simple'):
        self._size = size
        self._distribution = Distribution(distribution)

    def __iter__(self):
        return self

    def next(self):
        if self._size <= 0:
            raise StopIteration
        self._size -= 1
        return self._distribution.getSample()

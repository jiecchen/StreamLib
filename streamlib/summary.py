"""

"""
from streamlib import MurmurHash
import copy
from array import array

class CountMin:
    """
    Count-Min sketch.
    """
    def __init__(self, w=20, mu=5, typecode='i'):
        """
        Create a new instance of CountMin.

        :param w: The number of buckets.
        :type w: int

        :param mu: The number of repeated copies. Used to control the
                   failure probability ~= 2^{-mu}
        :type mu: int

        :param typecode: type to represent the frequencies, check
                         docs.python.org for module `array`
        """
        self._w = w
        self._mu = mu
        self._sketch = [array(typecode, [0] * w) for i in xrange(mu)]
        self._hashes = [MurmurHash() for i in xrange(mu)]
        self._hash = hash(self) 

    def processBatch(self, dataStream, weighted=False):
        """
        Summarize the given data stream.

        :param dataStream: any iterable object with hashable elements. 
                           e.g. a list of integers.
        :param weighted: if weighted, each item in dataStream should
                         be (key, weight) pair, where weight > 0
        """
        if weighted:
            for key, weight in dataStream:
                for i in xrange(self._mu):
                    # where the item is mapped by the i_th hash
                    pos = self._hashes[i].hash(key) % self._w
                    # increment the bucket
                    self._sketch[i][pos] += weight            
        else:
            for item in dataStream:
                for i in xrange(self._mu):
                    # where the item is mapped by the i_th hash
                    pos = self._hashes[i].hash(item) % self._w
                    # increment the bucket
                    self._sketch[i][pos] += 1

    def processItem(self, item, weighted=False):
        """
        Summarize the given data stream, but only process one
        item.

        :param item: hashable object to be processed
                           e.g. an integer
        :param weighted: if weighted, item  should
                         be a (key, weight) pair, where weight > 0
        """
        if weighted:
            for key, weight in dataStream:
                for i in xrange(self._mu):
                    # where the item is mapped by the i_th hash
                    pos = self._hashes[i].hash(key) % self._w
                    # increment the bucket
                    self._sketch[i][pos] += weight            
        else:
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



    def reproduce(self, num=1):
        """
        Reproduce CountMin instance(s) to have the same
        internal status.

        :param num: number of instances to be reproduced
        :type num: int

        :return: reproduced instance. if num > 1, a list 
                 of instances will be returned
        """
        if type(num) is not int:
            raise TypeError('num should be int')
        if num < 1:
            raise ValueError('num should >= 1')

        if num == 1:
            return copy.deepcopy(self)
        else:
            return [copy.deepcopy(self)]
            
        


    def merge(self, other):
        """
        Merge two CountMin instances if they are compatible.

        :param other: an instance of CountMin, 
        """
        if other._hash != self._hash:
            raise ValueError('two instances are not compatible')

        res = CountMin(w=1, mu=1)
        res._sketch = copy.deepcopy(self._sketch)
        res._hashes = copy.deepcopy(self._hashes)
        res._w = self._w
        res._mu = self._mu
        for i in xrange(self._mu):
            for j in xrange(self._w):
                res._sketch[i][j] += other._sketch[i][j]

        return res

                
    def __add__(self, other):
        """
        Overload + for self.merge
        """
        return self.merge(other)


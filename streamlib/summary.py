"""

"""
from streamlib import MurmurHash
import copy
from array import array
from abc import ABCMeta, abstractmethod
from random import randint
from streamlib.utils import doc_inherit
import streamlib.utils as utils



class CountSketch(object):
    """
    Count Sketch.
    """
    def __init__(self, w=20, mu=5, typecode='i'):
        """
        Create a new instance for CountSketch.

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
                         be (key, weight) pair
        """

        for item in dataStream:
            self.processItem(item, weighted)

    def processItem(self, item, weighted=False):
        """
        Summarize the given data stream, but only process one
        item.

        :param item: hashable object to be processed
                           e.g. an integer
        :param weighted: if weighted, item  should
                         be a (key, weight) pair
        """
        if weighted:
            key, weight = item
            for i in xrange(self._mu):
                # where the item is mapped by the i_th hash
                pos = self._hashes[i].hash(key) % self._w
                # increment the bucket
                self._sketch[i][pos] += weight * (randint(-1, 0) * 2 + 1)
        else:
            for i in xrange(self._mu):
                # where the item is mapped by the i_th hash
                pos = self._hashes[i].hash(item) % self._w
                # increment the bucket
                self._sketch[i][pos] += (randint(-1, 0) * 2 + 1)


    def estimate(self, key):
        pass

    def merge(self, other):
        pass
    
    def __add__(self, other):
        return self.merge(other)



class CountMin(object):
    """
    Count-Min sketch.
    support non-negative weighted data stream.
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

        for item in dataStream:
            self.processItem(item, weighted)

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
            key, weight = item
            for i in xrange(self._mu):
                # where the item is mapped by the i_th hash
                pos = self._hashes[i].hash(key) % self._w
                # increment the bucket
                self._sketch[i][pos] += weight            
        else:
            for i in xrange(self._mu):
                # where the item is mapped by the i_th hash
                pos = self._hashes[i].hash(item) % self._w
                # increment the bucket
                self._sketch[i][pos] += 1


    def estimate(self, key):
        """
        Estimate the frequency of given item.

        :param key: key/item in the data stream
        
        :return: estimated frequency of the given key.
        :rtype: int/real
        """
        all_estimators = [self._sketch[i][self._hashes[i].hash(key) % self._w]
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



class CountMedian(CountMin):
    """
    Count-Median sketch.
    support negative weighted data stream.
    """

    @doc_inherit
    def __init__(self, w=20, mu=5, typecode='i'):
        super(CountMedian, self).__init__(w, mu, typecode)


    
    def processBatch(self, dataStream, weighted=False):
        """
        Summarize the given data stream.

        :param dataStream: any iterable object with hashable elements. 
                           e.g. a list of integers.
        :param weighted: if weighted, each item in dataStream should
                         be (key, weight) pair, weight can be positive
                         or negtive
        """

        for item in dataStream:
            self.processItem(item, weighted)


    def processItem(self, item, weighted=False):
        """
        Summarize the given data stream, but only process one
        item.

        :param item: hashable object to be processed
                           e.g. an integer
        :param weighted: if weighted, item  should
                         be a (key, weight) pair, weight can be postive
                         or negative
        """
        super(CountMedian, self).processItem(item, weighted)


    def estimate(self, key):
        """
        Estimate the frequency of given item.

        :param key: key/item in the data stream
        
        :return: estimated frequency of the given key.
        :rtype: int/real
        """
        all_estimators = [self._sketch[i][self._hashes[i].hash(key) % self._w]
                          for i in xrange(self._mu)]
        return utils.median(all_estimators)


            
        



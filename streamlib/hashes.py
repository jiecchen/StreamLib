"""
Interface and implementation for hash functions.
"""

from abc import ABCMeta, abstractmethod
import mmh3
import random

class _Hash(object):
    """ 
    Interface for Hash Object. 
    """
    @abstractmethod
    def hash(self, key):
        """
        Map the given key to an integer.

        :param key: a hashable object
        
        :return:
        :rtype: int
        """
        raise NotImplementedError('To be overwritten!')

class MurmurHash(_Hash):
    """
    Murmur Hash Function.
    """
    def __init__(self):
        self._seed = random.randint(0, 1 << 31)
    
    def hash(self, key):
        """
        Return the hash value of key.

        :param key: can be any hashable object
        
        :return:
        :rtype: int 
        """
        v = mmh3.hash(str(key.__hash__()), self._seed)
        return -(v + 1) if v < 0 else v


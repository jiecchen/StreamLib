"""
Interface and implementation for hash functions.
"""
import mmh3
import random


class MurmurHash:
    """
    Wrapper for mmh3
    """
    def __init__(self):
        self._seed = random.randint(0, 1 << 31)
    
    def hash(self, key):
        """
        Return the hash value of key.

        :param key: int
        
        :return:
        :rtype: int 
        """
        v = mmh3.hash(str(key), self._seed)
        return -(v + 1) if v < 0 else v


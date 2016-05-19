"""
Interface and implementation for hash functions.
"""
import mmh3
import random


cdef class MurmurHash:
    """
    Wrapper for mmh3
    """
    def __init__(self):
        self._seed = random.randint(0, 1 << 31)
    
    cdef int hash(self, int key):
        """
        Return the hash value of key.

        :param key: int
        
        :return:
        :rtype: int 
        """
        cdef int v
        v = mmh3.hash(str(key), self._seed)
        return -(v + 1) if v < 0 else v


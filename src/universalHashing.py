# Implementation for Universal Hash Gamily.
# Analysis of the algorithm can be found in (sec 10.6.1)
# http://www.cs.cmu.edu/~avrim/451f11/lectures/lect1004.pdf
# or
# https://github.com/jiecchen/references/blob/master/lect1004.pdf




from bisect import bisect_left
import math 
import random

Primes = (3, 7, 13, 19, 29, 37, 43, 53, 61, 71, 79, 89, 101, 107, 113, 131, 
          139, 151, 163, 173, 181, 193, 199, 223, 229, 239, 251, 263, 271, 281, 
          293, 311, 317, 337, 349, 359, 373, 383, 397, 409, 421, 433, 443, 457, 
          463, 479, 491, 503, 521, 541, 557, 569, 577, 593, 601, 613, 619, 641, 
          647, 659, 673, 683, 701, 719, 733, 743, 757, 769, 787, 809, 821, 827, 839, 
          857, 863, 881, 887, 911, 929, 941, 953, 971, 983, 997, 1013, 1021, 1033,
          1049, 1061, 1069, 1091, 1097, 1109, 1123, 1151, 1163, 1181, 1193, 1213, 1223,
          1289, 1999, 2551, 3023, 3469, 3851, 4217, 4561, 4909, 5197, 5501, 
          5779, 6053, 6301, 6569, 6823, 7027, 7297, 7541, 7727, 7951, 8209, 
          8419, 8629, 8807, 9007, 9203, 9397, 9547, 9743, 9907, 10111, 10273, 
          10459, 10651, 10847, 11003, 11173, 11353, 11519, 11717, 11887, 12011, 
          12163, 12343, 12487, 12611, 12757, 12917, 13043, 13183, 13337, 13499, 
          13679, 13781, 13907, 14071, 14249, 14407, 14537, 14653, 14767, 14887, 
          15053, 15173, 15287, 15391, 15527, 15649, 15767, 15889, 16033, 16139, 
          16273, 16421, 16553, 16673, 16823, 16937, 17041, 17183, 17317, 17417, 
          17509, 17627, 17761, 17891, 17981, 18097, 18199, 18301, 18413, 18517, 
          18661, 18787, 18919, 19069, 19183, 19289, 19417)

# TODO: fix the bug that the returned hash value might be larger than M
#       This bug is due to the gap between M and its nearest prime number
class _LinearHash:
    """
    hash function use linear combination % M,
    for internal use only
    """
    def __init__(self, _M, _rd):
        # make sure self._M is a prime number right rather than _M
        _M = 19289 if _M > 19289 else _M
        pos = bisect_left(Primes, _M)
        self._M = _M #Primes[pos]
        # make sure self._base < self._M
        b = int(math.log(self._M, 2)) - 1
        self._base = (1 << b) - 1
        self._b = b
        self._para = [_rd.choice(range(self._M)) for i in range(100 / self._b + 1)]
        # print (self._M, self._base, self._b, self._para)
    
    
    def hash(self, key):
        """
        Given a key (should be hashable type),
        return the hashed value
        """
        try:
            x_int = key.__hash__()
        except AttributeError:
            x_int = hash(key)

        if x_int < 0:
            x_int = -x_int - 1

        i = 0
        hash_value = 0
        while (x_int):
            current = x_int & self._base
            x_int = (x_int >> self._b)
            hash_value = (hash_value + self._para[i] * current) % self._M
            i += 1
        return hash_value 
            
        




class UniversalHash:
    """
    Example:
    ----------------
    # construct a universal hash family map: [?] -> [M]
    # here M should be a prime number
    uhash = UniversalHash(M)
    hs = uhash.pickHash()
    ----------------
    hs.hash(hashable_obj) will give the hash value of hashable_obj which is \in [M]
    """
    def __init__(self, _M):
        self._random = random.Random()
        self._random.seed()
        self._M = _M

    def pickHash(self):
        """ 
        Randomly return a hash function belongs to 
        this Universal Hash Family. Such hash function is
        an instance of _LinearHash hence has the method .hash(hashable_object)
        """
        return _LinearHash(self._M, self._random)

            
            

    
        


class UniversalHash:
    """
    Example:
    ----------------
    # construct a universal hash family map: [?] -> [M]
    # here M should be a prime number
    uhash = UniversalHash(M)
    hs = uhash.pickHash()
    ----------------
    hs(hashable_obj) will give the hash value of hashable_obj which is \in [M]
    """
    

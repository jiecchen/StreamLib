from sketch import Sketch
from streamlib.wrappers import inherit_docs

class MG(Sketch):
    """
    Misra-Gries Algorithm for Frequency-Estimation.
    
    Usage:
    -------------------------
    mg = MG(k)
    for x in data_stream:
        mg.process(x)
    ------------------------
    mg.frequency(i) will give an estimation of the frequency of item i, 
    with error at most m/k, here the m is the size of the data_stream.
    More detail can be found in 
    http://www.cs.dartmouth.edu/~ac/Teach/CS49-Fall11/Notes/lecnotes.pdf
    or
    https://github.com/jiecchen/references/blob/master/lecnotes.pdf
    """
    def __init__(self, _k):
        self.A = {}
        self._k = _k 
        
    def process(self, _item):
        """
        Process for each item,
        Worst-case processing time: O(k) per item
        Amortized processing time: O(1) per item
        """
        if _item in self.A.keys():
            self.A[_item] += 1
        elif len(self.A.keys()) < self._k - 1:
            self.A[_item] = 1
        else:
            self.A = {_k : (_v - 1) for _k, _v in self.A.items() if _v > 1}

    def getEstimation(self, _item):
        """ Return the estimation of the frequncy of _item """
        return self.A[_item] if _item in self.A.keys() else 0
    
    def frequency(self, _item):
        """ Return the estimation of the frequncy of _item """
        return self.getEstimation(_item)

    def merge(self, skc):
        """ MG sketch is not mergable """
        raise AttributeError(" MG sketch is not mergable ")

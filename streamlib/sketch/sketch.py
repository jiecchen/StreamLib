from abc import ABCMeta, abstractmethod

class BasicEstimator():
    """ Interface for basic sketch estimator """
    __metaclass__ = ABCMeta
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def process(self, *args, **kwargs):
        """ process each item """
        pass

    @abstractmethod
    def batchProcess(self, dataStream):
        """ process the dataStream in batch """
        pass

    @abstractmethod
    def getEstimation(self, *args, **kwargs):
        """ return the estimation """
        pass

    @abstractmethod
    def merge(self, estimator):
        """
        @args
        estimator  :  basic estimator that copied from self but has processed different dataString
        @return
        Suppose est1.batchProcess(dataStream1), est2.batchProcess(dataStream2),
        est1.merge(est2) returns a estimator that has processed dataStream1 concatenates dataStream2
        """
        pass
    

class Sketch:
    """ Interface for sketch classes """
    __metaclass__ = ABCMeta
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass
        
    @abstractmethod
    def process(self, *args, **kwargs):
        """ process each item """
        pass

    @abstractmethod    
    def batchProcess(self, dataStream):
        """ process the dataStream in batch """
        pass

    @abstractmethod
    def getEstimation(self, *args, **kwargs):
        """ return the estimation """
        pass
    
    @abstractmethod
    def merge(self, sketch):
        """
        @args
        sketch  :  sketch that copied from self but has processed different dataString
        @return
        Suppose sketch1.batchProcess(dataStream1), sketch2.batchProcess(dataStream2),
        sketch1.merge(sketch2) returns a sketch that has processed dataStream1 concatenates dataStream2
        """
        pass

class BasicEstimator:
    """ Interface for basic sketch estimator """
    def __init__(self, *args, **kwargs):
        pass

    def process(self, *args, **kwargs):
        """ process each item """
        pass

    def batchProcess(self, dataStream):
        """ process the dataStream in batch """
        pass

    def getEstimation(self, *args, **kwargs):
        """ return the estimation """
        pass

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
    def __init__(self, *args, **kwargs):
        pass

    def process(self, *args, **kwargs):
        """ process each item """
        pass

    def batchProcess(self, dataStream):
        """ process the dataStream in batch """
        pass

    def getEstimation(self, *args, **kwargs):
        """ return the estimation """
        pass

    def merge(self, sketch):
        """
        @args
        sketch  :  sketch that copied from self but has processed different dataString
        @return
        Suppose sketch1.batchProcess(dataStream1), sketch2.batchProcess(dataStream2),
        sketch1.merge(sketch2) returns a sketch that has processed dataStream1 concatenates dataStream2
        """
        pass

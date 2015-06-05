import pytest


from streamlib import CountMin
class Test_CountMin:
    
    def test_process(self):
        a = CountMin(w=10, mu=10)
        ls = [1, 1, 1, 2, 1, 1, 1]
        a.processBatch(ls)
        assert a.estimate(1) == 6
        assert a.estimate(2) == 1


    def test_merge(self):
        a = CountMin(w=10, mu=10)
        b = a.reproduce()
        c = CountMin()
        
        with pytest.raises(ValueError):
            a + c         

        l1 = [1, 1, 1, 2, 1, 1, 1]
        l2 = [1, 1, 1, 3, 3]
        a.processBatch(l1)
        b.processBatch(l2)

        c = a + b

        assert c.estimate(1) == 9
        assert c.estimate(2) == 1
        assert c.estimate(3) == 2
        

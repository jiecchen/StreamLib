import pytest
import math

from streamlib import CountMin
class Test_CountMin(object):
    
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
        


from streamlib import CountMedian
class Test_CountMedian(object):
    
    def test_estimate(self):
        a = CountMedian(w=10, mu=10)
        ls = [1, 1, 1, 2, 1, 1, 1]
        a.processBatch(ls)
        assert a.estimate(1) == 6
        assert a.estimate(2) == 1

    def test_merge(self):
        a = CountMedian(w=10, mu=10)
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


from streamlib import F2
class Test_F2(object):
    
    def test(self):
        w = 300
        f2 = F2(w)
        items = [1, 2, 3, 4]
        weights = [5, 1, 1, 6]
        f2.processBatch(zip(items, weights), True)
        new_f2 = f2.merge(f2.reproduce())

        #    items.extend(items)
        weights = map(lambda x: x * 2, weights)
        exact_f2 = sum(map(lambda x: x**2, weights))

        assert abs(new_f2.estimate() - exact_f2) <=  exact_f2 / math.sqrt(w)

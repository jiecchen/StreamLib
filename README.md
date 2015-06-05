StreamLib
=========

A Python library for streaming algorithms

## Description
Algorithms included:

   * Sketch
	  * Count Min Sketch [cm05] -- DONE
	  * Count Sketch [ccfc04]
	  * BJKST Sketch [bjkst]
	  * Misra-Gries Sketch [mg82]
	  * F2 Sketch [ams]
	  * Quantile Sketch [myblog]
	  * ...

## Usage
### DataStream
Any **iterable** object with **hashable** elements can be considered as a data stream. Here are some examples.

+ a list of integers: `[1, 10, 20, 1, 5]`
+ a generator that yields tuples, see the instance `demo` as follows,

~~~python
def demoGen(N = 1000):
    i = 0
    while i < N:
        yield random.randint(0, 10);
        i += 1
demo = demoGen()




~~~python
from streamlib.stream import DataStream
#############################################################
# use dict to represents discrete distribution
# each key appears with probability in proportion to its value
dist = {'A': 10,  'B': 1, 'C': 100}
d = DataStream(dist, 1000) # the second para is total number of items d will yield
# now we can print the items in d:
for itm in d:
	print itm

############################################################
# to generate elements from a list uniformly
ls = list('qwertyuiopasdfghjklzxcvbnm')
d = DataStream(ls, 10000)

############################################################
# create instance from file
d = DataStream('file_name')
~~~
For more details, please check the document.

### Sketch
Each sketch implemented in our library inherits abstract class *Sketch*. Following are the common methods they share:

~~~python
	@abstractmethod
	def process(self, *args, **kwargs):
	""" process each item """

    def batchProcess(self, dataStream):
        """ process the dataStream in batch """

    @abstractmethod
    def getEstimation(self, *args, **kwargs):
        """ return the estimation """
    
    @abstractmethod
    def merge(self, sketch):
		""" merge self & sketch if mergable """
~~~
Take F2 Sketch (which gives the estimation of second frequency moment of a data stream)
as an example:


~~~python
from streamlib.stream import DataStream
from streamlib.sketch import F2
d = DataStream({'A':1, 'B':2, 'C':10}, 100)
# construct the F2 sketch
f2 = F2(0.1, 0.001) # F2(eps, delta) returns an (eps, delta) estimator
for x in d:   # or simply write as `f2.batchProcess(d)`
	f2.process(x)
# print the estimation	
print f2.getEstimation()
~~~


## Dependency

  * Python = 2.x (x >= 6).
  * mmh3 >= 2.0


## TODO
- Need to redesign and generalize the interface, any *iteratable*, *hashable* object should be considered as "data stream".
- Try to use CPython to speed up the implementation.
- Add more streaming algorithms.
- Minimize dependencies.

## References
[ccfc04]: Charikar, Moses, Kevin Chen, and Martin Farach-Colton. "Finding frequent items in data streams." Automata, Languages and Programming. Springer Berlin Heidelberg, 2002. 693-703.

[ams]: Alon, Noga, Yossi Matias, and Mario Szegedy. "The space complexity of approximating the frequency moments." Proceedings of the twenty-eighth annual ACM symposium on Theory of computing. ACM, 1996.

[bjskt]: Bar-Yossef, Ziv, et al. "Counting distinct elements in a data stream." Randomization and Approximation Techniques in Computer Science. Springer Berlin Heidelberg, 2002. 1-10.

[cm05]: Cormode, Graham, and S. Muthukrishnan. "An improved data stream summary: the count-min sketch and its applications." Journal of Algorithms 55.1 (2005): 58-75.

[mg82]: Misra, Jayadev, and David Gries. "Finding repeated elements." Science of computer programming 2.2 (1982): 143-152.

[myblog]: http://jiecchen.github.io/blog/2014/08/13/quantile-sketch/

## Contributors

  * jiecchen `chenjiecao@gmail.com`
  * Rachel Lowden `ralowden@imail.iu.edu`

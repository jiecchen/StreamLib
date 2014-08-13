StreamLib
=========

A Python library for streaming algorithms - Implemented in pure python

## Description
Algorithms included:

   * Sketch
      * Count Sketch 
	  * Count Min Sketch
	  * BJKST Sketch
	  * Misra-Gries Sketch
	  * F2 Sketch 
	  * Quantile Sketch
   * Hash
	  * Strong Universal Hash Family ( provide k-wise independent hash functions )

## Usage
### DataStream
The class `DataStream` defined in `streamlib.stream` is the object that our algorithms
can process/manipulate. There are two pre-defined models:

   * turnsitle model :
	 each item is in the form `(i, c)`, where `i` is the element
	 and `c` is the weight.
   * vanilla model :
	 special case of turnsitle model, each item has the form `(i, 1)`, or equivalently, `i`.
	 In other words, each item has the same weight.

By add some extra restrictions to turnsitle model, one can also get some other models, e.g. **Cash Register model**, **Strict Turnsitle model**, users are responsible for the restrictions they added.
	 
For our library, if a streaming algorithm is able work under turnsitle model, it will automatically work under vanilla model.

An instance of DataStream can be constructed use the following ways:

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
Take F2 Sketch (which give the estimation of second frequency moment of a data stream)
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


## References


## Contributors

  * jiecchen `chenjiecao@gmail.com`

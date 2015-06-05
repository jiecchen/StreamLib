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
+ a generator that yields tuples, see the instance `dataStream` as follows,

~~~python
import random
def demoGen(N = 1000):
    i = 0
    while i < N:
        yield random.randint(0, 10);
        i += 1

dataStream = demoGen()
~~~
+ a tuple of strings: `('fix', 'the', 'bug', please', '...')`
+ a string: `'abcdefgdahfahdfajkhfkahfsahfjksfhjk'`
+ many more

## Summarize the data stream
Many algorithms that are popular to summarize data streams are included
in the module **streamlib**. We give some examples to show their basic usage.

### Count-Min Sketch
Count-Min sketch[CM05] is used to summarize the data stream and estimate the frequency of each element in the data stream. This sketch give high accurate estimation to heavy hitters (elements that have high frequencies) while relatively large error may induced for light elements. See following example for the basic usage.

~~~python
from streamlib import CountMin
cm = CountMin() # create a instance of CountMin, see docs for more detail
cm.processBatch([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 3, 4])
for i in xrange(5):
    print 'Estimated frequency of', i, 'is', cm.estimate(i)
~~~
result of above code,

	Estimated frequency of 0 is 4
	Estimated frequency of 1 is 6
	Estimated frequency of 2 is 1
	Estimated frequency of 3 is 2
	Estimated frequency of 4 is 1


An instance of `CountMin` can be initialized by two parameters, see docs for detail.

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

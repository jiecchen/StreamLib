Getting Started
=================

Data Stream
------------
Any **iterable** object with **hashable** elements can be considered as a data stream. Here are some examples.

* a list of integers: :code:`[1, 10, 20, 1, 5]`
* a generator that yields tuples, see the instance :code:`dataStream` as follows,

.. code-block:: python
   
   import random

   def demoGen(N = 1000):
       i = 0
       while i < N:
           yield random.randint(0, 10);
           i += 1

   dataStream = demoGen()

* a tuple of strings: :code:`('fix', 'the', 'bug', please', '...')`
* a string: :code:`'abcdefgdahfahdfajkhfkahfsahfjksfhjk'`
* many more


Summarize the data stream
-------------------------
Many algorithms that are popular to summarize data streams are included
in the module **streamlib**. We give some examples to show their basic usage. Most sketches have similar methods, e.g. `processBatch`, `estimate`, `reproduce`, `merge` etc.

Count-Min Sketch
#################
Count-Min sketch [cm05]_ is used to summarize the data stream and estimate the frequency of each element in the data stream. This sketch give high accurate estimation to heavy hitters (elements that have high frequencies) while relatively large error may induced for light elements. See following example for the basic usage.

.. code-block:: python

    from streamlib import CountMin
    cm = CountMin() # create a instance of CountMin, see document for more detail
    cm.processBatch([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 3, 4])
    for i in xrange(5):
	print 'Estimated frequency of', i, 'is', cm.estimate(i)

result of above code, ::

	Estimated frequency of 0 is 4
	Estimated frequency of 1 is 6
	Estimated frequency of 2 is 1
	Estimated frequency of 3 is 2
	Estimated frequency of 4 is 1

One can also create multiple instances of CountMin, each handle a substream (thus can be run in multi-threads).
By merging those instances, we obtain a summary of the joint stream of all substreams. See the following example.

.. code-block:: python


    from streamlib import CountMin
    cm0 = CountMin() # create a instance of CountMin, see document for more detail
    cm1 = cm0.reproduce() # reproduce a compatible sketch of cm0 
    

    cm0.processBatch([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 3, 4])
    cm1.processBatch([1, 2, 3, 4])
    cm = cm0.merge(cm1)
    for i in xrange(5):
	print 'Estimated frequency of', i, 'is', cm.estimate(i)

which gives, ::

    Estimated frequency of 0 is 4
    Estimated frequency of 1 is 6
    Estimated frequency of 2 is 4
    Estimated frequency of 3 is 1
    Estimated frequency of 4 is 1


Most sketches included in `summary` module can also handle **weighted** data stream, let's consider
the following case, 

.. code-block:: python

    from streamlib import CountMin
    cm = CountMin()
    dataStream = [(0, 20), (1, 4), (2, 1), (3, 1), (4, 5), (1, 100), (0, 500)]
    cm.processBatch(dataStream, weighted=True) # set weighted=True

    for i in xrange(5):
	print 'Estimated frequency of', i, 'is', cm.estimate(i)

it gives ::

    Estimated frequency of 0 is 520
    Estimated frequency of 1 is 104
    Estimated frequency of 2 is 1
    Estimated frequency of 3 is 1
    Estimated frequency of 4 is 5
    



AMS F2 Sketch
#############
AMS F2 Sketch can be used to estimate the second moment of the frequency vector of a data stream.
For example, when a data stream is `[1, 1, 1, 2, 2, 3]`, there are three 1, two 2 and one 3, its second moment of the frequency vector then be `3^2 + 2^2 + 1^2 = 14`. Here we show its most basic usage.

.. code-block:: python

    from streamlib import F2
    # set the bucket size as w=100
    # the |EstimatedValue - TrueValue| <= TrueValue / sqrt(w)
    f2 = F2(w=100) 
    dataStream = [1, 1, 1, 2, 2, 3]
    f2.processBatch(dataStream)
    print 'Estimated F2 =', f2.estimate()

 
which gives, ::

    Estimated F2 = 13


Bibliography
-------------
.. [ccfc04] Charikar, Moses, Kevin Chen, and Martin Farach-Colton. "Finding frequent items in data streams." Automata, Languages and Programming. Springer Berlin Heidelberg, 2002. 693-703.

.. [ams] Alon, Noga, Yossi Matias, and Mario Szegedy. "The space complexity of approximating the frequency moments." Proceedings of the twenty-eighth annual ACM symposium on Theory of computing. ACM, 1996.

.. [bjkst] Bar-Yossef, Ziv, et al. "Counting distinct elements in a data stream." Randomization and Approximation Techniques in Computer Science. Springer Berlin Heidelberg, 2002. 1-10.

.. [cm05] Cormode, Graham, and S. Muthukrishnan. "An improved data stream summary: the count-min sketch and its applications." Journal of Algorithms 55.1 (2005): 58-75.

.. [mg82] Misra, Jayadev, and David Gries. "Finding repeated elements." Science of computer programming 2.2 (1982): 143-152.

.. [myblog] http://jiecchen.github.io/blog/2014/08/13/quantile-sketch/

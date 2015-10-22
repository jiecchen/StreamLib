Principles of Design
==================

## Levels of Implementation
+ Use Cython or C/C++ to implement the low-level streaming algorithm, which only works for data stream with each item being integer.
+ Any **iterable**, **hashable** object can be considered as a data stream. Each item can be converted to integer using proper hash function on the fly, then feed into the low-level api.



## Unify the Implementation
There are many common aspects of those popular streaming algorithms, e.g., most of them use **median trick** to boost the success probability; many streaming algorithms can be thought as a type of sketch.

Try to address those common features and unify the implementation of various of streaming algorithms.




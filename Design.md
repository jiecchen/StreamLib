Principles of Design
==================

## Data Stream
Any **iterable**, **hashable** object can be considered as a data stream.

## Unify the Implementation
There are many common aspects of those popular streaming algorithms, e.g., most of them use **median trick** to boost the success probability; many streaming algorithms can be thought as a type of sketch.

Try to address those common features and unify the implementation of various of streaming algorithms.

## Speedup
Maybe use CPython to speedup the implementation.

# coding=utf-8
"""
Interface for streaming algorithm
"""
from abc import ABCMeta, abstractmethod
from copy import deepcopy


class StreamingAlgorithm(object):
    """
    Abstract class for streaming algorithms
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def process_item(self, item):
        pass


class Sketch(StreamingAlgorithm):
    """
    Abstract class for sketches
    """
    __metaclass__ = ABCMeta

    def process_items_batch(self, items):
        for itm in items:
            self.process_item(itm)


class MergeableSketch(Sketch):
    """
    Abstract for sketches that are mergeable
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def merge(self, other_sketch):
        """
        merge a compatible sketch into this one
        :return this
        """

    @abstractmethod
    def __add__(self, other_sketch):
        """
        this + other_sketch results a merge sketch
        :return this + other_sketch
        """
        tmp = deepcopy(self)
        return tmp.merge(other_sketch)

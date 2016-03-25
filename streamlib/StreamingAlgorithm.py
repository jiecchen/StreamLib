"""
Interface for streaming algorithm
"""
from abc import ABCMeta, abstractmethod


class StreamingAlgorithm(object):
    """
    Abstract class for streaming algorithm
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def process_item(self, item):
        pass



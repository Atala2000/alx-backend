#!/usr/bin/env python3
"""
Module that creates a FIFO class
"""
from base_caching import BaseCaching

from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    Class that implements a first in
    and first out caching algorithm
    """

    def __init__(self):
        """
        Initializes the object
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key, _)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)

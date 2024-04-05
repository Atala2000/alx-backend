#!/usr/bin/env python3
"""
Module that creates a FIFO class
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):

    def __init__(self):
        super().__init__()
        self.insertion_order = []

    def put(self, key, item):
        """
        Inserts a key value pair in the dictionary
        Args:
            key (str): key for the item
            item (str): value for the item
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            self.insertion_order.append(key)
        self.cache_data[key] = item
        if BaseCaching.MAX_ITEMS < len(self.cache_data):
            print(f"DISCARD: {self.insertion_order[0]}")
            del self.cache_data[self.insertion_order[0]]
            self.insertion_order.pop(0)

    def get(self, key):
        """
        Retrieves the value of an item in the cache
        Args:
            key (str): The key of the item in the dictionary
        """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]

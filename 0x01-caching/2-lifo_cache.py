#!/usr/bin/env python3
"""
Module that implements LIFO cache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.insertion_order = []

    def put(self, key: str, item: str):
        """
        Method that inserts an item and deletes the last one inserted
        Args:
            key (str): Key for the item
            value (str): Value for the item
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.insertion_order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print(f"DISCARD: {self.insertion_order[-2]}")
            del self.cache_data[self.insertion_order[-2]]

    def get(self, key):
        """
        Method that retrieves the vale of an itemusing its key
        Args:
            key (str): Key for the item
        """
        if key is None or key not in self.cache_data:
            return self.cache_data[key]

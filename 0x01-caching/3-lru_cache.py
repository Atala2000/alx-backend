#!/usr/bin/env python3
"""
Module for creating a least recently used cache
"""
from base_caching import BaseCaching
from collections import Counter


class LRUCache(BaseCaching):
    """
    Creates objects for a least recently used cache
    """

    def __init__(self):
        """
        Initializes the object
        """
        super().__init__()
        self.cache_counter = {}

    def put(self, key, item):
        """
        Inserts items into the cache and removes the least recently used item
        """
        if key is None or item is None:
            return

        # Check if the key already exists
        if key in self.cache_data:
            # If it exists, update the item
            self.cache_data[key] = item
        else:
            # If it doesn't exist, add the item
            self.cache_data[key] = item

            # Evict the least recently used item if the cache is full
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = min(self.cache_counter, key=self.cache_counter.get)
                del self.cache_data[lru_key]
                del self.cache_counter[lru_key]

        # Update the access count for the key
        self.cache_counter[key] = max(self.cache_counter.values(),
                                      default=0) + 1

    def get(self, key):
        """
        Retrieves a key and also increases the count when key is used
        """
        if key in self.cache_data:
            # Update the access count for the key
            self.cache_counter[key] = max(self.cache_counter.values(),
                                          default=0) + 1
            return self.cache_data[key]
        return None

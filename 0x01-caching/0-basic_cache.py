#!/usr/bin/env python3
"""
Module that inhertis from base caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class that defines a caching algorithm
    from a dictionary
    """

    def put(self, key: str, item: str):
        """
        Method that inserts items
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key: str):
        """
        Method that retrieves items
        """
        return self.cache_data.get(key, None)

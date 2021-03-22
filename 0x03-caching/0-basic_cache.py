#!/usr/bin/env python3
"""
This module create a basic cache -dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Class that inherits from BaseChaching and is a caching system
    """

    def put(self, key, item):
        """
        Method that fills the dictionary using the provided key and value
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Method that works as a getter for the basic dictionary
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data[key]

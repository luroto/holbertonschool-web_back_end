#!/usr/bin/env python3
"""
Implementing the MRU caching police
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Class for handling MRU caching system
    """
    def __init__(self):
        """
        Constructor for the class
        """
        super().__init__()
        self.recent_keys = []

    def put(self, key, item):
        """
            Method for adding key and value to the dict
        """
        self.cache_data[key] = item
        if key not in self.recent_keys:
            self.recent_keys.append(key)
        else:
            if key != self.recent_keys[-1]:
                self.recent_keys.remove(key)
                self.recent_keys.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            recent = self.recent_keys[-2]
            self.recent_keys.pop(-2)
            del self.cache_data[recent]
            print("Discard: {}".format(recent))
            

    def get(self, key):
        """
        Method for getting a value from dict and tracks its use
        """
        if key is None or key not in self.cache_data:
            return None
        if key in self.recent_keys:
            if key != self.recent_keys[-1]:
                self.recent_keys.remove(key)
                self.recent_keys.append(key)
        return self.cache_data[key]

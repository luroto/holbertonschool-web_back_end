#!/usr/bin/env python3
"""
Implementing the LRU caching police
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Implementing the LRU Caching system
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.keys_use = []

    def put(self, key, item):
        """
        Method to add entries on dict
        """
        if key is not None and item is not None:
            if key not in self.keys_use:
                self.keys_use.append(key)
            else:
                if key != self.keys_use[-1]:
                    self.keys_use.remove(key)
                    self.keys_use.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removing = self.keys_use[0]
                del self.cache_data[removing]
                self.keys_use.remove(removing)
                print("DISCARD: {}".format(removing))

    def get(self, key):
        """
        Getter of LRU cache system
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key not in self.keys_use:
            self.keys_use.append(key)
        else:
            if key != self.keys_use[-1]:
                self.keys_use.remove(key)
                self.keys_use.append(key)
        return self.cache_data[key]

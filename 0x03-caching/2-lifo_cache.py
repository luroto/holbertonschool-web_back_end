#!/usr/bin/env python3
"""
Implementing the LIFO cache police
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Implementing the LIFO Caching system
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.all_keys = []

    def put(self, key, item):
        """
        Method to add entries on dict
        """
        if key is not None and item is not None:
            last = len(self.all_keys) - 1
            self.all_keys.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removing = self.all_keys.pop(last)
                del self.cache_data[removing]
                print("DISCARD: {}".format(removing))

    def get(self, key):
        """
        Getter of LIFO cache system
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]

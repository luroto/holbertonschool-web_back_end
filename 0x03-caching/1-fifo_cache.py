#!/usr/bin/env python3
"""
Implementing the FIFO cache police
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Class for implementing the FIFO caching system
    """

    def __init__(self):
        """
        ¿Constructor? method
        """
        super().__init__()
        FIFOCache.all_keys = []

    def put(self, key, item):
        """
        Method to add new values using the FIFO queue
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                FIFOCache.all_keys.append(key)
                self.cache_data[key] = item
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    removing = FIFOCache.all_keys.pop(0)
                    del self.cache_data[removing]
                    print("DISCARD:{}".format(removing))
                

    def get(self, key):
        """
        The getter for any key in the dictionary
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]

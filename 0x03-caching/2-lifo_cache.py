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
        LIFOCache.all_keys = []

    def put(self, key, item):
        """
        Method to add entries on dict
        """
        if key is not None and item is not None:
            last = len(LIFOCache.all_keys) - 1
            LIFOCache.all_keys.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removing = LIFOCache.all_keys.pop(last)
                del self.cache_data[removing]
                print("DISCARD: {}".format(removing))

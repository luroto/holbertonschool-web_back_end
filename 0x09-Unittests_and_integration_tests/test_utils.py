#!/usr/bin/env python3
"""
Different tests for utils.py
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    Class for testing AccessNestedMap instances
    """
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def TestAccessNestedMap(self, fullmap, path, value):
        """
        Testing AccessNestedMap using unittest
        """
        result = access_nested_map(fullmap, path)
        self.assertEqual(result, value)

    @parameterized.expand([
        (KeyError, {}, ("a",)),
        (KeyError, {"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, value, fullmap, path):
        """
        Testing for Key Error 
        """
        with self.assertRaises(value) as error:
            access_nested_map(fullmap, path)
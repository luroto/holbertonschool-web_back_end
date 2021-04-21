#!/usr/bin/env python3
"""
Different tests for utils.py
"""

import unittest
from unittest import mock
from parameterized import parameterized
import requests
import utils
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    """
    Class for testing get json utility function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ]
    )
    def test_get_json(self, url, test_payload):
        """
        Method for testing get json
        """
        mock_response = mock.Mock()
        mock_response.json = test_payload
        with mock.patch('utils.get_json', return_value=mock_response):
            expected = get_json(url)
            self.assertEqual(expected, test_payload)

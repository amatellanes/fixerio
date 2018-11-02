from __future__ import unicode_literals

import unittest

from fixerio.client import Fixerio


class FixerioInitTestCase(unittest.TestCase):
    def test_raises_if_access_key_is_not_passed(self):
        with self.assertRaises(TypeError):
            Fixerio()

    def test_sets_access_key(self):
        access_key = 'test-access-key'

        client = Fixerio(access_key)

        self.assertEqual(client.access_key, access_key)

    def test_sets_none_symbols_attribute_if_it_is_not_passed(self):
        client = Fixerio('test-access-key')

        self.assertIsNone(client._symbols)

    def test_sets_symbols_attribute(self):
        symbols = ['USD', 'GBP']

        client = Fixerio('test-access-key', symbols=symbols)

        self.assertEqual(client._symbols, symbols)

    def test_sets_none_timeout_attribute_if_it_is_not_passed(self):
        client = Fixerio('test-access-key')

        self.assertIsNone(client.timeout)

    def test_sets_timeout_attribute(self):
        timeout = 0.001

        client = Fixerio('test-access-key', timeout=timeout)

        self.assertEqual(client.timeout, timeout)

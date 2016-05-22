from __future__ import unicode_literals

import unittest
from fixerio.client import Fixerio


class FixerioInitTestCase(unittest.TestCase):
    def test_sets_none_base_attribute_if_default_base_passed(self):
        self.default_base = 'EUR'

        client = Fixerio(base=self.default_base)

        self.assertIsNone(client.base)

    def test_sets_none_base_attribute_if_it_not_passed(self):
        client = Fixerio()

        self.assertIsNone(client.base)

    def test_sets_base_attribute(self):
        self.base = 'USD'

        client = Fixerio(base=self.base)

        self.assertEqual(client.base, self.base)

    def test_sets_none_symbols_attribute_if_it_not_passed(self):
        client = Fixerio()

        self.assertIsNone(client.symbols)

    def test_sets_symbols_attribute(self):
        self.symbols = ['USD', 'GBP']

        client = Fixerio(symbols=self.symbols)

        self.assertEqual(client.symbols, self.symbols)

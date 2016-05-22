from __future__ import unicode_literals

import unittest
from fixerio.client import Fixerio


class FixerioInitTestCase(unittest.TestCase):
    def test_sets_none_base_attribute_if_default_base_is_passed(self):
        default_base = 'EUR'

        client = Fixerio(base=default_base)

        self.assertIsNone(client.base)

    def test_sets_none_base_attribute_if_it_is_not_passed(self):
        client = Fixerio()

        self.assertIsNone(client.base)

    def test_sets_base_attribute(self):
        base = 'USD'

        client = Fixerio(base=base)

        self.assertEqual(client.base, base)

    def test_sets_none_symbols_attribute_if_it_is_not_passed(self):
        client = Fixerio()

        self.assertIsNone(client.symbols)

    def test_sets_symbols_attribute(self):
        symbols = ['USD', 'GBP']

        client = Fixerio(symbols=symbols)

        self.assertEqual(client.symbols, symbols)

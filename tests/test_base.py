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

    def test_sets_none_base_attribute_if_default_base_is_passed(self):
        default_base = 'EUR'

        client = Fixerio('test-access-key', base=default_base)

        self.assertIsNone(client.base)

    def test_sets_none_base_attribute_if_it_is_not_passed(self):
        client = Fixerio('test-access-key')

        self.assertIsNone(client.base)

    def test_sets_base_attribute(self):
        base = 'USD'

        client = Fixerio('test-access-key', base=base)

        self.assertEqual(client.base, base)

    def test_sets_none_symbols_attribute_if_it_is_not_passed(self):
        client = Fixerio('test-access-key')

        self.assertIsNone(client.symbols)

    def test_sets_symbols_attribute(self):
        symbols = ['USD', 'GBP']

        client = Fixerio('test-access-key', symbols=symbols)

        self.assertEqual(client.symbols, symbols)

    def test_sets_no_secure_attribute_if_it_is_not_passed(self):
        client = Fixerio('test-access-key')

        self.assertFalse(client.secure)

    def test_sets_secure_attribute(self):
        secure = True

        client = Fixerio('test-access-key', secure=secure)

        self.assertEqual(client.secure, secure)

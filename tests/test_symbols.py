from __future__ import unicode_literals

import unittest

try:
    from unittest import mock
    from urllib.parse import urljoin  # noqa: F401
    from urllib.parse import urlencode  # noqa: F401
except ImportError:  # For Python 2
    import mock
    from urlparse import urljoin  # noqa: F401
    from urllib import urlencode  # noqa: F401

import responses

from fixerio.client import Fixerio
from fixerio.exceptions import FixerioException

BASE_URL = 'http://data.fixer.io/api/'


class FixerioGetSymbolsTestCase(unittest.TestCase):
    def setUp(self):
        self.access_key = 'test-access-key'
        self.path = 'symbols'
        query = urlencode({'access_key': self.access_key})
        self.url = BASE_URL + self.path + '?' + query

    @responses.activate
    def test_returns_symbols(self):
        expected_response = {'symbols': {'AED': 'United Arab Emirates Dirham',
                                         'AFN': 'Afghan Afghani'}}
        responses.add(responses.GET, self.url, json=expected_response)

        client = Fixerio(self.access_key)
        response = client.symbols()

        self.assertDictEqual(response, expected_response)
        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.url, self.url)
        self.assertIsNone(request.body)

    @responses.activate
    def test_raises_exception_if_bad_request(self):
        responses.add(responses.GET, self.url, json={'success': False},
                      status=400)

        with self.assertRaises(FixerioException)as ex:
            client = Fixerio(self.access_key)
            client.symbols()

        expected_message = (('400 Client Error: Bad Request for url: '
                             '{0}').format(self.url))
        self.assertEqual(str(ex.exception), expected_message)


class FixerioSymbolsTimeoutTestCase(unittest.TestCase):
    def setUp(self):
        self.access_key = 'test-access-key'
        self.path = 'symbols'
        self.timeout = 0.001
        query = urlencode({'access_key': self.access_key})
        self.url = BASE_URL + self.path + '?' + query

    @mock.patch('requests.get')
    def test_returns_symbols_for_timeout_in_constructor(self, mock_get):
        client = Fixerio(self.access_key, timeout=self.timeout)
        client.symbols()

        self.assertEqual(mock_get.call_count, 1)
        self.assertEqual(mock_get.call_args[1]['timeout'], self.timeout)

    @mock.patch('requests.get')
    def test_returns_symbols_for_timeout_in_method(self, mock_get):
        client = Fixerio(self.access_key)
        client.symbols(timeout=self.timeout)

        self.assertEqual(mock_get.call_count, 1)
        self.assertEqual(mock_get.call_args[1]['timeout'], self.timeout)

    @mock.patch('requests.get')
    def test_returns_symbols_for_timeout_passed_if_both(self, mock_get):
        client = Fixerio(self.access_key, timeout=not self.timeout)
        client.symbols(timeout=self.timeout)

        self.assertEqual(mock_get.call_count, 1)
        self.assertEqual(mock_get.call_args[1]['timeout'], self.timeout)

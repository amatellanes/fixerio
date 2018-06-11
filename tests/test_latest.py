from __future__ import unicode_literals

import json
import unittest

try:
    from urllib.parse import urljoin  # noqa: F401
    from urllib.parse import urlencode  # noqa: F401
except ImportError:  # For Python 2
    from urlparse import urljoin  # noqa: F401
    from urllib import urlencode  # noqa: F401

import responses

from fixerio.client import Fixerio
from fixerio.exceptions import FixerioException

BASE_URL = 'http://data.fixer.io/api/'


class FixerioLatestTestCase(unittest.TestCase):
    def setUp(self):
        self.access_key = 'test-access-key'
        self.path = 'latest'
        query = urlencode({'access_key': self.access_key})
        self.url = BASE_URL + self.path + '?' + query

    @responses.activate
    def test_returns_latest_rates(self):
        expected_response = {'base': 'EUR', 'date': '2016-04-29',
                             'rates': {'GBP': 0.78025}}
        responses.add(responses.GET,
                      self.url,
                      body=json.dumps(expected_response),
                      content_type='application/json')

        client = Fixerio(self.access_key)
        response = client.latest()

        self.assertDictEqual(response, expected_response)
        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.url, self.url)
        self.assertIsNone(request.body)

    @responses.activate
    def test_raises_exception_if_bad_request(self):
        responses.add(responses.GET,
                      self.url,
                      body="{'success': false}",
                      status=400,
                      content_type='text/json')

        with self.assertRaises(FixerioException)as ex:
            client = Fixerio(self.access_key)
            client.latest()

        expected_message = (('400 Client Error: Bad Request for url: '
                             '{0}').format(self.url))
        self.assertEqual(str(ex.exception), expected_message)


class FixerioLatestSymbolsTestCase(unittest.TestCase):
    def setUp(self):
        self.access_key = 'test-access-key'
        self.path = 'latest'
        query = urlencode({'access_key': self.access_key})
        self.url = BASE_URL + self.path + '?' + query

    @responses.activate
    def test_returns_latest_rates_for_symbols_passed_in_constructor(self):
        symbols = ['USD', 'GBP']
        expected_response = {
            "base": "EUR",
            "date": "2016-05-19",
            "rates": {"GBP": 0.76585, "USD": 1.1197}
        }
        responses.add(responses.GET,
                      self.url,
                      body=json.dumps(expected_response),
                      content_type='application/json')

        client = Fixerio(self.access_key, symbols=symbols)
        response = client.latest()

        self.assertDictEqual(response, expected_response)
        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        symbols_str = ','.join(symbols)
        params = urlencode(
            {'access_key': self.access_key, 'symbols': symbols_str})
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        expected_url = BASE_URL + expected_path
        self.assertEqual(request.url, expected_url)
        self.assertIsNone(request.body)

    @responses.activate
    def test_returns_latest_rates_for_symbols_passed_in_method(self):
        symbols = ['USD', 'GBP']
        expected_response = {
            "base": "EUR",
            "date": "2016-05-19",
            "rates": {"GBP": 0.76585, "USD": 1.1197}
        }
        responses.add(responses.GET,
                      self.url,
                      body=json.dumps(expected_response),
                      content_type='application/json')

        client = Fixerio(self.access_key)
        response = client.latest(symbols=symbols)

        self.assertDictEqual(response, expected_response)
        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        symbols_str = ','.join(symbols)
        params = urlencode(
            {'access_key': self.access_key, 'symbols': symbols_str})
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        expected_url = BASE_URL + expected_path
        self.assertEqual(request.url, expected_url)
        self.assertIsNone(request.body)

    @responses.activate
    def test_returns_latest_rates_for_symbols_passed_in_method_if_both(self):
        symbols = ['USD', 'GBP']
        other_symbols = ['JPY', 'EUR']
        expected_response = {
            "base": "EUR",
            "date": "2016-05-19",
            "rates": {"GBP": 0.76585, "USD": 1.1197}
        }
        responses.add(responses.GET,
                      self.url,
                      body=json.dumps(expected_response),
                      content_type='application/json')

        client = Fixerio(self.access_key, symbols=other_symbols)
        response = client.latest(symbols=symbols)

        self.assertDictEqual(response, expected_response)
        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        symbols_str = ','.join(symbols)
        params = urlencode(
            {'access_key': self.access_key, 'symbols': symbols_str})
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        expected_url = BASE_URL + expected_path
        self.assertEqual(request.url, expected_url)
        self.assertIsNone(request.body)

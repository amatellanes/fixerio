from __future__ import unicode_literals

import json
import unittest
from datetime import date

try:
    from urllib.parse import urljoin  # noqa: F401
    from urllib.parse import urlencode  # noqa: F401
except ImportError:  # For Python 2
    from urlparse import urljoin  # noqa: F401
    from urllib import urlencode  # noqa: F401

import responses

from fixerio.client import Fixerio
from fixerio.exceptions import FixerioException

BASE_URL = 'http://data.fixer.io/api'


class FixerioHistoricalRatesTestCase(unittest.TestCase):
    def setUp(self):
        self.access_key = 'test-access-key'
        self.date = date(2000, 1, 3)
        self.path = '/{0}'.format(self.date.isoformat())
        query = urlencode({'access_key': self.access_key})
        self.url = BASE_URL + self.path + '?' + query

    @responses.activate
    def test_returns_historical_rates(self):
        expected_response = {'base': 'EUR',
                             'date': '2000-01-03',
                             'rates': {'GBP': 0.6246}}
        responses.add(responses.GET,
                      self.url,
                      body=json.dumps(expected_response),
                      content_type='application/json')
        client = Fixerio(self.access_key)
        response = client.historical_rates(date=self.date.isoformat())

        self.assertDictEqual(response, expected_response)
        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.url, self.url)
        self.assertIsNone(request.body)

        client = Fixerio(self.access_key)
        response = client.historical_rates(date=self.date)

        self.assertDictEqual(response, expected_response)
        request = responses.calls[1].request
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
            client.historical_rates(date=self.date)

        expected_message = (('400 Client Error: Bad Request for url: '
                             '{0}').format(self.url))
        self.assertEqual(str(ex.exception), expected_message)


class FixerioHistoricalRatesSymbolsTestCase(unittest.TestCase):
    def setUp(self):
        self.access_key = 'test-access-key'
        self.date = date(2000, 1, 3)
        self.path = '/{0}'.format(self.date.isoformat())
        query = urlencode({'access_key': self.access_key})
        self.url = BASE_URL + self.path + '?' + query

    @responses.activate
    def test_returns_historical_rates_for_symbols_passed_in_constructor(self):
        symbols = ['USD', 'GBP']
        expected_response = {"base": "EUR",
                             "date": "2000-01-03",
                             "rates": {"GBP": 0.6246, "USD": 1.009}}
        responses.add(responses.GET,
                      self.url,
                      body=json.dumps(expected_response),
                      content_type='application/json')

        client = Fixerio(self.access_key, symbols=symbols)
        response = client.historical_rates(date=self.date)

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
    def test_returns_historical_rates_for_symbols_passed_in_method(self):
        symbols = ['USD', 'GBP']
        expected_response = {"base": "EUR",
                             "date": "2000-01-03",
                             "rates": {"GBP": 0.6246, "USD": 1.009}}
        responses.add(responses.GET,
                      self.url,
                      body=json.dumps(expected_response),
                      content_type='application/json')

        client = Fixerio(self.access_key)
        response = client.historical_rates(date=self.date, symbols=symbols)

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
    def test_returns_historical_rates_for_symbols_passed_if_both(self):
        symbols = ['USD', 'GBP']
        other_symbols = ['JPY', 'EUR']
        expected_response = {"base": "EUR",
                             "date": "2000-01-03",
                             "rates": {"GBP": 0.6246, "USD": 1.009}}
        responses.add(responses.GET,
                      self.url,
                      body=json.dumps(expected_response),
                      content_type='application/json')

        client = Fixerio(self.access_key, symbols=other_symbols)
        response = client.historical_rates(date=self.date, symbols=symbols)

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

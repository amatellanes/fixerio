from __future__ import unicode_literals

import unittest
from datetime import date
from unittest import mock

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
    def test_returns_historical_rates_using_date_string(self):
        expected_response = {'base': 'EUR', 'date': '2000-01-03',
                             'rates': {'GBP': 0.6246}}
        responses.add(responses.GET, self.url, json=expected_response)

        client = Fixerio(self.access_key)

        response = client.historical_rates(date=self.date.isoformat())
        self.assertDictEqual(response, expected_response)
        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.url, self.url)
        self.assertIsNone(request.body)

    @responses.activate
    def test_returns_historical_rates_using_date_object(self):
        expected_response = {'base': 'EUR', 'date': '2000-01-03',
                             'rates': {'GBP': 0.6246}}
        responses.add(responses.GET, self.url, json=expected_response)

        client = Fixerio(self.access_key)

        response = client.historical_rates(date=self.date)
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
            client.historical_rates(date=self.date)

        expected_message = (('400 Client Error: Bad Request for url: '
                             '{0}').format(self.url))
        self.assertEqual(str(ex.exception), expected_message)


class FixerioHistoricalRatesSymbolsTestCase(unittest.TestCase):
    def setUp(self):
        self.access_key = 'test-access-key'
        self.date = date(2000, 1, 3)
        self.path = '/{0}'.format(self.date.isoformat())
        self.symbols = ['USD', 'GBP']
        query = urlencode({
            'access_key': self.access_key,
            'symbols': ','.join(self.symbols)
        })
        self.url = BASE_URL + self.path + '?' + query

    @responses.activate
    def test_returns_historical_rates_for_symbols_passed_in_constructor(self):
        expected_response = {'base': 'EUR', 'date': '2000-01-03',
                             'rates': {'GBP': 0.6246, 'USD': 1.009}}
        responses.add(responses.GET, self.url, json=expected_response)

        client = Fixerio(self.access_key, symbols=self.symbols)
        response = client.historical_rates(date=self.date)

        self.assertDictEqual(response, expected_response)
        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        params = urlencode({
            'access_key': self.access_key,
            'symbols': ','.join(self.symbols)
        })
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        expected_url = BASE_URL + expected_path
        self.assertEqual(request.url, expected_url)
        self.assertIsNone(request.body)

    @responses.activate
    def test_returns_historical_rates_for_symbols_passed_in_method(self):
        expected_response = {'base': 'EUR', 'date': '2000-01-03',
                             'rates': {'GBP': 0.6246, 'USD': 1.009}}
        responses.add(responses.GET, self.url, json=expected_response)

        client = Fixerio(self.access_key)
        response = client.historical_rates(date=self.date,
                                           symbols=self.symbols)

        self.assertDictEqual(response, expected_response)
        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        symbols_str = ','.join(self.symbols)
        params = urlencode({
            'access_key': self.access_key,
            'symbols': symbols_str
        })
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        expected_url = BASE_URL + expected_path
        self.assertEqual(request.url, expected_url)
        self.assertIsNone(request.body)

    @responses.activate
    def test_returns_historical_rates_for_symbols_passed_if_both(self):
        other_symbols = ['JPY', 'EUR']
        expected_response = {'base': 'EUR', 'date': '2000-01-03',
                             'rates': {'GBP': 0.6246, 'USD': 1.009}}
        responses.add(responses.GET, self.url, json=expected_response)

        client = Fixerio(self.access_key, symbols=other_symbols)
        response = client.historical_rates(date=self.date,
                                           symbols=self.symbols)

        self.assertDictEqual(response, expected_response)
        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        symbols_str = ','.join(self.symbols)
        params = urlencode({
            'access_key': self.access_key,
            'symbols': symbols_str
        })
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        expected_url = BASE_URL + expected_path
        self.assertEqual(request.url, expected_url)
        self.assertIsNone(request.body)


class FixerioHistoricalRatesTimeoutTestCase(unittest.TestCase):
    def setUp(self):
        self.access_key = 'test-access-key'
        self.date = date(2000, 1, 3)
        self.path = '/{0}'.format(self.date.isoformat())
        self.timeout = 0.001
        query = urlencode({
            'access_key': self.access_key,
        })
        self.url = BASE_URL + self.path + '?' + query

    @mock.patch('requests.get')
    def test_returns_historical_rates_for_timeout_passed_in_constructor(self,
                                                                        mock_get):
        client = Fixerio(self.access_key, timeout=self.timeout)
        client.historical_rates(date=self.date)

        self.assertEqual(mock_get.call_count, 1)
        self.assertEqual(mock_get.call_args[1]['timeout'], self.timeout)

    @mock.patch('requests.get')
    def test_returns_historical_rates_for_symbols_passed_in_method(self,
                                                                   mock_get):
        client = Fixerio(self.access_key)
        client.historical_rates(date=self.date, timeout=self.timeout)

        self.assertEqual(mock_get.call_count, 1)
        self.assertEqual(mock_get.call_args[1]['timeout'], self.timeout)

    @mock.patch('requests.get')
    def test_returns_historical_rates_for_symbols_passed_if_both(self,
                                                                 mock_get):
        client = Fixerio(self.access_key, timeout=not self.timeout)
        client.historical_rates(date=self.date, timeout=self.timeout)

        self.assertEqual(mock_get.call_count, 1)
        self.assertEqual(mock_get.call_args[1]['timeout'], self.timeout)

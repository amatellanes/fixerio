from __future__ import unicode_literals

import json
import unittest
from datetime import date

try:
    from urllib.parse import urljoin
    from urllib.parse import urlencode
except ImportError:  # For Python 2
    from urlparse import urljoin
    from urllib import urlencode

import httpretty

from fixerio.client import Fixerio, FixerioException

BASE_URL = 'http://api.fixer.io'


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


class FixerioLatestTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Fixerio()

        self.path = '/latest'
        self.url = urljoin(BASE_URL, self.path)

    @httpretty.activate
    def test_returns_latest_rates(self):
        expected_response = {'base': 'EUR', 'date': '2016-04-29',
                             'rates': {'GBP': 0.78025}}
        httpretty.register_uri(httpretty.GET,
                               self.url,
                               body=json.dumps(expected_response),
                               content_type='application/json')

        response = self.client.latest()

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.path, self.path)
        self.assertEqual(request.querystring, {})
        self.assertEqual(request.body, b'')

    @httpretty.activate
    def test_returns_latest_rates_for_base_passed_in_constructor(self):
        base = 'USD'
        expected_response = {'base': base, 'date': '2016-05-13',
                             'rates': {'GBP': 0.69403}}
        httpretty.register_uri(httpretty.GET,
                               self.url,
                               body=json.dumps(expected_response),
                               content_type='application/json')

        client = Fixerio(base=base)
        response = client.latest(base=base)

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        params = urlencode({'base': base})
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        self.assertEqual(request.path, expected_path)
        self.assertEqual(request.querystring, {'base': [base]})
        self.assertEqual(request.body, b'')

    @httpretty.activate
    def test_returns_latest_rates_for_base_passed(self):
        base = 'USD'
        expected_response = {'base': base, 'date': '2016-05-13',
                             'rates': {'GBP': 0.69403}}
        httpretty.register_uri(httpretty.GET,
                               self.url,
                               body=json.dumps(expected_response),
                               content_type='application/json')

        response = self.client.latest(base=base)

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        params = urlencode({'base': base})
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        self.assertEqual(request.path, expected_path)
        self.assertEqual(request.querystring, {'base': [base]})
        self.assertEqual(request.body, b'')

    @httpretty.activate
    def test_raises_exception_if_bad_request(self):
        httpretty.register_uri(httpretty.GET,
                               self.url,
                               body="{'success': false}",
                               status=400,
                               content_type='text/json')

        with self.assertRaises(FixerioException)as ex:
            self.client.latest()

        expected_message = (('400 Client Error: Bad Request for url: '
                             '{0}').format(self.url))
        self.assertEqual(str(ex.exception), expected_message)


class FixerioHistoricalRatesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Fixerio()

        self.date = date(2000, 1, 3)
        self.path = '/{0}'.format(self.date.isoformat())
        self.url = urljoin(BASE_URL, self.path)

    @httpretty.activate
    def test_returns_historical_rates(self):
        expected_response = {'base': 'EUR',
                             'date': '2000-01-03',
                             'rates': {'GBP': 0.6246}}
        httpretty.register_uri(httpretty.GET,
                               self.url,
                               body=json.dumps(expected_response),
                               content_type='application/json')

        response = self.client.historical_rates(date=self.date.isoformat())

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.path, self.path)
        self.assertEqual(request.querystring, {})
        self.assertEqual(request.body, b'')

        response = self.client.historical_rates(date=self.date)

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.path, self.path)
        self.assertEqual(request.querystring, {})
        self.assertEqual(request.body, b'')

    @httpretty.activate
    def test_returns_historical_rates_for_base_passed_in_constructor(self):
        base = 'USD'
        expected_response = {'base': base,
                             'date': '2000-01-03',
                             'rates': {'GBP': 0.6246}}
        httpretty.register_uri(httpretty.GET,
                               self.url,
                               body=json.dumps(expected_response),
                               content_type='application/json')

        client = Fixerio(base=base)
        response = client.historical_rates(date=self.date)

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        params = urlencode({'base': base})
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        self.assertEqual(request.path, expected_path)
        self.assertEqual(request.querystring, {'base': [base]})
        self.assertEqual(request.body, b'')

    @httpretty.activate
    def test_returns_historical_rates_for_base_passed(self):
        base = 'USD'
        expected_response = {'base': base, 'date': '2016-05-13',
                             'rates': {'GBP': 0.69403}}
        httpretty.register_uri(httpretty.GET,
                               self.url,
                               body=json.dumps(expected_response),
                               content_type='application/json')

        response = self.client.historical_rates(date=self.date, base=base)

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        params = urlencode({'base': base})
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        self.assertEqual(request.path, expected_path)
        self.assertEqual(request.querystring, {'base': [base]})
        self.assertEqual(request.body, b'')

    @httpretty.activate
    def test_raises_exception_if_bad_request(self):
        httpretty.register_uri(httpretty.GET,
                               self.url,
                               body="{'success': false}",
                               status=400,
                               content_type='text/json')

        with self.assertRaises(FixerioException)as ex:
            self.client.historical_rates(date=self.date)

        expected_message = (('400 Client Error: Bad Request for url: '
                             '{0}').format(self.url))
        self.assertEqual(str(ex.exception), expected_message)

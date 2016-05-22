from __future__ import unicode_literals

import json
import unittest

try:
    from urllib.parse import urljoin
    from urllib.parse import urlencode
except ImportError:  # For Python 2
    from urlparse import urljoin
    from urllib import urlencode

import httpretty

from fixerio.client import Fixerio, FixerioException

BASE_URL = 'http://api.fixer.io'
SECURE_BASE_URL = 'https://api.fixer.io'


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
        response = client.latest()

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
    def test_returns_latest_rates_for_symbols_passed_in_constructor(self):
        symbols = ['USD', 'GBP']
        expected_response = {
            "base": "EUR",
            "date": "2016-05-19",
            "rates": {"GBP": 0.76585, "USD": 1.1197}
        }
        httpretty.register_uri(httpretty.GET,
                               self.url,
                               body=json.dumps(expected_response),
                               content_type='application/json')

        client = Fixerio(symbols=symbols)
        response = client.latest()

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        symbols_str = ','.join(symbols)
        params = urlencode({'symbols': symbols_str})
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        self.assertEqual(request.path, expected_path)
        self.assertEqual(request.querystring, {'symbols': [symbols_str]})
        self.assertEqual(request.body, b'')

    @httpretty.activate
    def test_returns_latest_rates_for_symbols_passed(self):
        symbols = ['USD', 'GBP']
        expected_response = {
            "base": "EUR",
            "date": "2016-05-19",
            "rates": {"GBP": 0.76585, "USD": 1.1197}
        }
        httpretty.register_uri(httpretty.GET,
                               self.url,
                               body=json.dumps(expected_response),
                               content_type='application/json')

        response = self.client.latest(symbols=symbols)

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        symbols_str = ','.join(symbols)
        params = urlencode({'symbols': symbols_str})
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        self.assertEqual(request.path, expected_path)
        self.assertEqual(request.querystring, {'symbols': [symbols_str]})
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


class FixerioSecureLatestTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Fixerio()

        self.path = '/latest'
        self.secure_url = urljoin(SECURE_BASE_URL, self.path)

    @httpretty.activate
    def test_returns_latest_rates(self):
        expected_response = {'base': 'EUR', 'date': '2016-04-29',
                             'rates': {'GBP': 0.78025}}
        httpretty.register_uri(httpretty.GET,
                               self.secure_url,
                               body=json.dumps(expected_response),
                               content_type='application/json')

        response = self.client.latest(secure=True)

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
                               self.secure_url,
                               body=json.dumps(expected_response),
                               content_type='application/json')

        client = Fixerio(base=base)
        response = client.latest(secure=True)

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
                               self.secure_url,
                               body=json.dumps(expected_response),
                               content_type='application/json')

        response = self.client.latest(base=base, secure=True)

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        params = urlencode({'base': base})
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        self.assertEqual(request.path, expected_path)
        self.assertEqual(request.querystring, {'base': [base]})
        self.assertEqual(request.body, b'')

    @httpretty.activate
    def test_returns_latest_rates_for_symbols_passed_in_constructor(self):
        symbols = ['USD', 'GBP']
        expected_response = {
            "base": "EUR",
            "date": "2016-05-19",
            "rates": {"GBP": 0.76585, "USD": 1.1197}
        }
        httpretty.register_uri(httpretty.GET,
                               self.secure_url,
                               body=json.dumps(expected_response),
                               content_type='application/json')

        client = Fixerio(symbols=symbols)
        response = client.latest(secure=True)

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        symbols_str = ','.join(symbols)
        params = urlencode({'symbols': symbols_str})
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        self.assertEqual(request.path, expected_path)
        self.assertEqual(request.querystring, {'symbols': [symbols_str]})
        self.assertEqual(request.body, b'')

    @httpretty.activate
    def test_returns_latest_rates_for_symbols_passed(self):
        symbols = ['USD', 'GBP']
        expected_response = {
            "base": "EUR",
            "date": "2016-05-19",
            "rates": {"GBP": 0.76585, "USD": 1.1197}
        }
        httpretty.register_uri(httpretty.GET,
                               self.secure_url,
                               body=json.dumps(expected_response),
                               content_type='application/json')

        response = self.client.latest(symbols=symbols, secure=True)

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        symbols_str = ','.join(symbols)
        params = urlencode({'symbols': symbols_str})
        expected_path = '{url}?{params}'.format(url=self.path, params=params)
        self.assertEqual(request.path, expected_path)
        self.assertEqual(request.querystring, {'symbols': [symbols_str]})
        self.assertEqual(request.body, b'')

    @httpretty.activate
    def test_raises_exception_if_bad_request(self):
        httpretty.register_uri(httpretty.GET,
                               self.secure_url,
                               body="{'success': false}",
                               status=400,
                               content_type='text/json')

        with self.assertRaises(FixerioException)as ex:
            self.client.latest(secure=True)

        expected_message = (('400 Client Error: Bad Request for url: '
                             '{0}').format(self.secure_url))
        self.assertEqual(str(ex.exception), expected_message)

from __future__ import unicode_literals

import json
import unittest
from datetime import date

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import httpretty

from fixerio.client import Fixerio, FixerioException

BASE_URL = 'http://api.fixer.io'


class FixerioLatestTestCase(unittest.TestCase):
    def setUp(self):
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

        response = Fixerio.latest()

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.path, self.path)
        self.assertEqual(request.querystring, {})
        self.assertEqual(request.body, b'')

    @httpretty.activate
    def test_raises_exception_if_bad_request(self):
        httpretty.register_uri(httpretty.GET,
                               self.url,
                               body="{'success': false}",
                               status=400,
                               content_type='text/json')

        with self.assertRaises(FixerioException)as ex:
            Fixerio.latest()

        expected_message = (('400 Client Error: Bad Request for url: '
                             '{0}').format(self.url))
        self.assertEqual(str(ex.exception), expected_message)


class FixerioHistoricalRatesTestCase(unittest.TestCase):
    def setUp(self):
        self.date = date(2000, 1, 3)
        self.path = '/{0}'.format(self.date.isoformat())
        self.url = urljoin(BASE_URL, self.path)

    @httpretty.activate
    def test_returns_historical_rates_for_any_day_since_1999(self):
        expected_response = {
            'base': 'EUR',
            'date': '2000-01-03',
            'rates': {
                'AUD': 1.5346,
                'CAD': 1.4577,
                'CHF': 1.6043,
                'CYP': 0.5767,
                'CZK': 36.063,
                'DKK': 7.4404,
                'EEK': 15.6466,
                'GBP': 0.6246,
                'HKD': 7.8624,
                'HUF': 254.53,
                'ISK': 73.03,
                'JPY': 102.75,
                'KRW': 1140.02,
                'LTL': 4.0454,
                'LVL': 0.5916,
                'MTL': 0.4151,
                'NOK': 8.062,
                'NZD': 1.9331,
                'PLN': 4.1835,
                'ROL': 18273,
                'SEK': 8.552,
                'SGD': 1.6769,
                'SIT': 198.8925,
                'SKK': 42.317,
                'TRL': 546131,
                'USD': 1.009,
                'ZAR': 6.2013
            }
        }
        httpretty.register_uri(httpretty.GET,
                               self.url,
                               body=json.dumps(expected_response),
                               content_type='application/json')

        response = Fixerio.historical_rates(date=self.date.isoformat())

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.path, self.path)
        self.assertEqual(request.querystring, {})
        self.assertEqual(request.body, b'')

        response = Fixerio.historical_rates(date=self.date)

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.path, self.path)
        self.assertEqual(request.querystring, {})
        self.assertEqual(request.body, b'')

    @httpretty.activate
    def test_raises_exception_if_bad_request(self):
        httpretty.register_uri(httpretty.GET,
                               self.url,
                               body="{'success': false}",
                               status=400,
                               content_type='text/json')

        with self.assertRaises(FixerioException)as ex:
            Fixerio.historical_rates(date=self.date)

        expected_message = (('400 Client Error: Bad Request for url: '
                             '{0}').format(self.url))
        self.assertEqual(str(ex.exception), expected_message)

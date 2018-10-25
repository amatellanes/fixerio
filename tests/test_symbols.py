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


class FixerioGetSymbolsTestCase(unittest.TestCase):
    def setUp(self):
        self.access_key = 'test-access-key'
        self.path = 'symbols'
        query = urlencode({'access_key': self.access_key})
        self.url = BASE_URL + self.path + '?' + query

    @responses.activate
    def test_returns_symbols(self):
        expected_response = {
            "symbols": {
                "AED": "United Arab Emirates Dirham",
                "AFN": "Afghan Afghani",
                "ALL": "Albanian Lek",
                "AMD": "Armenian Dram"
            }
        }
        responses.add(responses.GET,
                      self.url,
                      body=json.dumps(expected_response),
                      content_type='application/json')

        client = Fixerio(self.access_key)
        response = client.symbols()

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
            client.symbols()

        expected_message = (('400 Client Error: Bad Request for url: '
                             '{0}').format(self.url))
        self.assertEqual(str(ex.exception), expected_message)

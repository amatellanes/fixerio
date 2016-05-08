from __future__ import unicode_literals

import json
import unittest

import httpretty

from fixerio.client import Fixerio, FixerioException


class FixerioLatestTestCase(unittest.TestCase):
    @httpretty.activate
    def test_returns_latest_rates(self):
        expected_response = {'base': 'EUR', 'date': '2016-04-29',
                             'rates': {'GBP': 0.78025}}
        httpretty.register_uri(httpretty.GET,
                               'http://api.fixer.io/latest',
                               body=json.dumps(expected_response),
                               content_type='application/json')

        response = Fixerio.latest()

        self.assertDictEqual(response, expected_response)
        request = httpretty.last_request()
        self.assertEqual(request.method, 'GET')
        self.assertEqual(request.querystring, {})
        self.assertEqual(request.body, b'')

    @httpretty.activate
    def test_raises_exception_if_bad_request(self):
        httpretty.register_uri(httpretty.GET,
                               'http://api.fixer.io/latest',
                               body='{"success": false}',
                               status=400,
                               content_type='text/json')

        with self.assertRaises(FixerioException)as ex:
            Fixerio.latest()

        expected_message = ('400 Client Error: Bad Request for url: '
                            'http://api.fixer.io/latest')
        self.assertEqual(str(ex.exception), expected_message)

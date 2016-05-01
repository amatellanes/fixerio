import json
import unittest

import httpretty
from sure import expect

from fixerio.client import Fixerio


class FixerioLatestTestCase(unittest.TestCase):
    @httpretty.activate
    def test_returns_latest_rates(self):
        expected_response = {"base": "EUR", "date": "2016-04-29", "rates": {"GBP": 0.78025}}
        httpretty.register_uri(httpretty.GET,
                               'http://api.fixer.io/latest',
                               body=json.dumps(expected_response),
                               content_type='application/json')

        response = Fixerio.latest()

        expect(response).to.equal(expected_response)

        expect(httpretty.last_request().method).to.equal('GET')
        expect(httpretty.last_request().querystring).being.equal({})
        expect(httpretty.last_request().body).being.equal(b'')

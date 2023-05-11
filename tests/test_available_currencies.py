import responses
import pytest
from pathlib import Path

from fixerio.client import Fixerio
from fixerio.exceptions import FixerioException

BASE_URL = 'https://api.apilayer.com/fixer/'
RESPONSES_DIR = Path(__file__).parent / 'responses'


class TestAvailableCurrencies:
    def setup_class(cls):
        cls.access_key = 'test-access-key'
        cls.url = BASE_URL + 'symbols'
        cls.response_file = \
            RESPONSES_DIR / "available_currencies_responses.yaml"

    @responses.activate
    def test_returns_available_currencies(self):
        responses._add_from_file(self.response_file)
        client = Fixerio(self.access_key)
        response = client.available_currencies()

        assert response['success'] is True
        assert response['symbols']['AED'] == 'United Arab Emirates Dirham'
        assert response['symbols']['CRC'] == 'Costa Rican Colón'

    @responses.activate
    def test_raises_exception_if_bad_request(self):
        responses.add(responses.GET,
                      self.url,
                      body="{'success': false}",
                      status=400,
                      content_type='application/json')

        with pytest.raises(FixerioException):
            client = Fixerio(self.access_key)
            client.available_currencies()

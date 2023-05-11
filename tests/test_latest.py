import responses
import pytest
from pathlib import Path

from fixerio.client import Fixerio
from fixerio.exceptions import FixerioException

BASE_URL = 'https://api.apilayer.com/fixer/'
RESPONSES_DIR = Path(__file__).parent / 'responses'


class TestLatest:
    def setup_class(cls):
        cls.access_key = 'test-access-key'
        cls.date = '2023-05-09'
        cls.url = BASE_URL + 'latest'
        cls.response_file = RESPONSES_DIR / "latest_responses.yaml"

    @responses.activate
    def test_returns_latest_rates(self):
        responses._add_from_file(file_path=self.response_file)
        client = Fixerio(self.access_key)
        response = client.latest()

        assert response['date'] == self.date
        assert response['base'] == 'EUR'
        rates = response['rates']
        assert rates['SEK'] == 11.172796
        assert rates['NOK'] == 11.557591
        assert rates['JPY'] == 148.40037

    @responses.activate
    def test_raises_exception_if_bad_request(self):
        responses.add(responses.GET,
                      self.url,
                      body="{'success': false}",
                      status=400,
                      content_type='application/json')

        with pytest.raises(FixerioException):
            client = Fixerio(self.access_key)
            client.latest()

    @responses.activate
    def test_returns_latest_rate_for_single_symbol_passed_as_string(self):
        symbol = 'USD'
        responses._add_from_file(file_path=self.response_file)
        client = Fixerio(self.access_key, symbols=symbol)
        response = client.latest()

        assert response['rates']['USD'] == 1.093434

    @responses.activate
    def test_returns_latest_rates_for_symbols_passed_in_constructor(self):
        symbols = ['USD', 'GBP']
        responses._add_from_file(file_path=self.response_file)

        client = Fixerio(self.access_key, symbols=symbols)
        response = client.latest()

        assert response['rates']['USD'] == 1.099239
        assert response['rates']['GBP'] == 0.871224

    @responses.activate
    def test_returns_latest_rates_for_symbols_passed_in_method(self):
        symbols = ['USD', 'GBP']
        responses._add_from_file(file_path=self.response_file)

        client = Fixerio(self.access_key)
        response = client.latest(symbols=symbols)

        assert response['rates']['USD'] == 1.099239
        assert response['rates']['GBP'] == 0.871224

    @responses.activate
    def test_returns_latest_rates_for_symbols_passed_in_method_if_both(self):
        symbols = ['USD', 'GBP']
        other_symbols = ['JPY', 'EUR']
        responses._add_from_file(file_path=self.response_file)

        client = Fixerio(self.access_key, symbols=other_symbols)
        response = client.latest(symbols=symbols)

        assert response['rates']['USD'] == 1.099239
        assert response['rates']['GBP'] == 0.871224
        assert response['rates'].get('JPY') is None

import datetime

from urllib.parse import urlencode

import requests

from .exceptions import FixerioException

from typing import Dict, Iterable, Optional, Union

BASE_URL = 'https://api.apilayer.com/fixer/'


class Fixerio(object):
    """ A client for Fixer API, available on API Layer. """

    def __init__(self,
                 access_key: str,
                 base: Optional[str] = None,
                 symbols: Union[None, str, Iterable[str]] = None):
        """
        :param access_key: your API Key.
        :param symbols: currency symbols to request specific exchange rates.
        """
        self._access_key = access_key
        self._base = base or 'EUR'
        self._symbols = symbols

    def _create_headers(self) -> Dict[str, str]:
        """ Creates a header with the API key required for accessing Fixer.io
        on API Layer.
        """
        headers = {
            "apikey": self._access_key
        }
        return headers

    def _create_payload(self, symbols: Union[None, str, Iterable[str]]) -> str:
        """ Creates a payload with no none values.

        :param symbols: currency symbols to request specific exchange rates.
        :return: a payload.
        """
        payload = {}
        if self._base is not None:
            payload['base'] = self._base
        if symbols is not None:
            if isinstance(symbols, str):
                payload['symbols'] = symbols
            else:
                payload['symbols'] = ','.join(symbols)

        payload_str = urlencode(payload, safe=',')
        return payload_str

    def available_currencies(self) -> dict:
        """ Get all currency symbols that can be used as base or target.

        :return: a dictinary where the member `symbols` contains a mapping
            from currency symbols to the full currency name.
        :raises FixerioException: if any error making a request.
        """
        try:
            url = BASE_URL + "symbols"
            response = requests.get(url, headers=self._create_headers())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

    def latest(self, symbols: Union[None, str, Iterable[str]] = None) -> dict:
        """ Get the latest foreign exchange reference rates.

        :param symbols: currency symbol(s) to request specific exchange rates.
        :return: the latest foreign exchange reference rates.
        :raises FixerioException: if any error making a request.
        """
        try:
            headers = self._create_headers()
            symbols = symbols or self._symbols
            payload = self._create_payload(symbols)

            url = BASE_URL + "latest"

            response = requests.get(url, headers=headers, params=payload)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

    def historical_rates(self,
                         date: Union[datetime.date, str],
                         symbols: Optional[Union[str, Iterable[str]]]
                         = None) -> dict:
        """
        Get rates for a historical date.

        :param date: the date to get rates for.
        :param symbols: currency symbol(s) to request specific exchange rates.
        :return: the historical rates for a specific date.
        :raises FixerioException: if any error making a request.
        """
        try:
            if isinstance(date, datetime.date):
                # Convert date to ISO 8601 format.
                date = date.isoformat()

            symbols = symbols or self._symbols
            headers = self._create_headers()
            payload = self._create_payload(symbols)

            url = BASE_URL + date

            response = requests.get(url, headers=headers, params=payload)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

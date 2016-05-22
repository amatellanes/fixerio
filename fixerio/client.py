from __future__ import unicode_literals

import datetime

try:
    from urllib.parse import urljoin
except ImportError:  # For Python 2
    from urlparse import urljoin

import requests

DEFAULT_BASE = 'EUR'

BASE_URL = 'http://api.fixer.io/'
SECURE_BASE_URL = 'https://api.fixer.io/'
LATEST_PATH = '/latest'


class FixerioException(BaseException):
    pass


class Fixerio(object):
    """ A client for Fixer.io. """

    def __init__(self, base=DEFAULT_BASE, symbols=None):
        """
        :param base: currency to quote rates.
        :type base: str or unicode
        :param symbols: currency symbols to request specific exchange rates.
        :type symbols: list or tuple
        """
        self.base = base if base != DEFAULT_BASE else None
        self.symbols = symbols

    @staticmethod
    def _create_payload(base, symbols):
        """ Creates a payload with no none values.

        :param base: currency to quote rates.
        :type base: str or unicode
        :param symbols: currency symbols to request specific exchange rates.
        :type symbols: list or tuple
        :return: a payload.
        :rtype: dict
        """
        payload = {}
        if base is not None:
            payload['base'] = base
        if symbols is not None:
            payload['symbols'] = ','.join(symbols)

        return payload

    def latest(self, base=None, symbols=None, secure=False):
        """ Get the latest foreign exchange reference rates.

        :param base: currency to quote rates.
        :type base: str or unicode
        :param symbols: currency symbols to request specific exchange rates.
        :type symbols: list or tuple
        :param secure: enable HTTPS endpoint.
        :type secure: bool
        :return: the latest foreign exchange reference rates.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        try:
            base = base or self.base
            symbols = symbols or self.symbols
            payload = Fixerio._create_payload(base, symbols)

            if secure:
                url = urljoin(SECURE_BASE_URL, LATEST_PATH)
            else:
                url = urljoin(BASE_URL, LATEST_PATH)
            response = requests.get(url, params=payload)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

    def historical_rates(self, date, base=None, symbols=None, secure=False):
        """
        Get historical rates for any day since `date`.

        :param date: a date
        :type date: date or str
        :param base: currency to quote rates.
        :type base: str or unicode
        :param symbols: currency symbols to request specific exchange rates.
        :type symbols: list or tuple
        :param secure: enable HTTPS endpoint.
        :type secure: bool
        :return: the historical rates for any day since `date`.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        try:
            if isinstance(date, datetime.date):
                # Convert date to ISO 8601 format.
                date = date.isoformat()

            base = base or self.base
            symbols = symbols or self.symbols
            payload = Fixerio._create_payload(base, symbols)

            if secure:
                url = urljoin(SECURE_BASE_URL, date)
            else:
                url = urljoin(BASE_URL, date)
            response = requests.get(url, params=payload)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

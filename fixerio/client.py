from __future__ import unicode_literals

import datetime

try:
    from urllib.parse import urljoin
    from urllib.parse import urlencode
except ImportError:  # For Python 2
    from urlparse import urljoin
    from urllib import urlencode

import requests

DEFAULT_BASE = 'EUR'

BASE_URL = 'http://api.fixer.io/'
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

    def latest(self, base=None, symbols=None):
        """ Get the latest foreign exchange reference rates.

        :param base: currency to quote rates.
        :type base: str or unicode
        :param symbols: currency symbols to request specific exchange rates.
        :type symbols: list or tuple
        :return: the latest foreign exchange reference rates.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        try:
            payload = {}
            base = base or self.base
            if base is not None:
                payload['base'] = base
            symbols = symbols or self.symbols
            if symbols is not None:
                payload['symbols'] = ','.join(symbols)

            url = urljoin(BASE_URL, LATEST_PATH)
            params = urlencode(payload)
            response = requests.get(url, params=params)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

    def historical_rates(self, date, base=None):
        """
        Get historical rates for any day since `date`.

        :param date: a date
        :type date: date or str
        :param base: currency to quote rates.
        :type base: str or unicode
        :return: the historical rates for any day since `date`.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        try:
            if isinstance(date, datetime.date):
                # Convert date to ISO 8601 format.
                date = date.isoformat()

            payload = {'base': base or self.base}

            url = urljoin(BASE_URL, date)
            response = requests.get(url, params=payload)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

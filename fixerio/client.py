from __future__ import unicode_literals

import datetime

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests

DEFAULT_BASE = 'EUR'

BASE_URL = 'http://api.fixer.io/'
LATEST_PATH = '/latest'


class FixerioException(BaseException):
    pass


class Fixerio(object):
    """ A client for Fixer.io. """

    def __init__(self, base=DEFAULT_BASE):
        self.base = base if base != DEFAULT_BASE else None

    def latest(self, base=None):
        """ Get the latest foreign exchange reference rates.

        :param base: currency to quote rates.
        :type base: str or unicode
        :return: the latest foreign exchange reference rates.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        try:
            base = base or self.base
            if base is not None:
                payload = {'base': base}
            else:
                payload = {}

            url = urljoin(BASE_URL, LATEST_PATH)
            response = requests.get(url, params=payload)

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

            base = base or self.base
            if base is not None:
                payload = {'base': base}
            else:
                payload = {}

            url = urljoin(BASE_URL, date)
            response = requests.get(url, params=payload)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

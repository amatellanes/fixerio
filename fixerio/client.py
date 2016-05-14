from __future__ import unicode_literals

import datetime

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests

BASE_URL = 'http://api.fixer.io/'
LATEST_PATH = '/latest'


class FixerioException(BaseException):
    pass


class Fixerio(object):
    """ A client for Fixer.io. """

    @staticmethod
    def latest():
        """ Get the latest foreign exchange reference rates.

        :return: the latest foreign exchange reference rates.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        try:
            url = urljoin(BASE_URL, LATEST_PATH)
            response = requests.get(url)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

    @staticmethod
    def historical_rates(date):
        """
        Get historical rates for any day since `date`.

        :param date: a date
        :type date: date or str
        :return: the historical rates for any day since `date`.
        :rtype: dict
        :raises FixerioException: if any error making a request.
        """
        try:
            if isinstance(date, datetime.date):
                # Convert date to ISO 8601 format.
                date = date.isoformat()

            url = urljoin(BASE_URL, date)
            response = requests.get(url)

            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as ex:
            raise FixerioException(str(ex))

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
        if isinstance(date, datetime.date):
            date = date.isoformat()
        url = urljoin(BASE_URL, date)
        response = requests.get(url)
        return response.json()

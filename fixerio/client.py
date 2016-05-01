try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests

BASE_URL = 'http://api.fixer.io/'
LATEST_PATH = '/latest'


class Fixerio(object):
    """ A client for Fixer.io. """

    @staticmethod
    def latest():
        """ Get the latest foreign exchange reference rates.

        :return: the latest foreign exchange reference rates
        :rtype: dict
        """
        response = requests.get(urljoin(BASE_URL, LATEST_PATH))

        return response.json()

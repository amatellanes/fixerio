A Python client for `Fixer API`_
================================

|Build Status| |Coverage Status| |Supports Wheel format|
|Latest PyPI version| |Documentation Status| |Requirements Status|

`Fixer API`_ (formerly known as Fixer.io) is a free JSON API for current and
historical foreign exchange rates published by the European Central Bank.

The rates are updated daily around 3 pm CET.

Installation
------------

Install ``fixerio`` with:

::

    pip install fixerio

Or with:

::

    easy_install fixerio

Or you can get the source from GitHub at
https://github.com/amatellanes/fixerio.


Usage
-----

Get the latest foreign exchange reference rates in JSON format.

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio(access_key='YOUR ACCESS KEY')
    >>> fxrio.latest()
    '''
     {'base': 'EUR',
     'date': '2016-05-27',
     'rates': {'AUD': 1.5483,
      'BGN': 1.9558,
      'BRL': 4.031,
      'CAD': 1.456,
      'CHF': 1.1068,
      'CNY': 7.3281,
      'CZK': 27.028,
      'DKK': 7.4367,
      'GBP': 0.76245,
      'HKD': 8.6735,
      'HRK': 7.4905,
      'HUF': 314.21,
      'IDR': 15157.25,
      'ILS': 4.2938,
      'INR': 74.867,
      'JPY': 122.46,
      'KRW': 1316.98,
      'MXN': 20.6611,
      'MYR': 4.5554,
      'NOK': 9.282,
      'NZD': 1.6586,
      'PHP': 52.096,
      'PLN': 4.3912,
      'RON': 4.5034,
      'RUB': 73.7516,
      'SEK': 9.2673,
      'SGD': 1.536,
      'THB': 39.851,
      'TRY': 3.2928,
      'USD': 1.1168,
      'ZAR': 17.4504}}
    '''

Get historical rates for any day since 1999.

.. code:: python

    >>> import datetime
    >>> from fixerio import Fixerio

    >>> today = datetime.date.today()
    >>> fxrio = Fixerio(access_key='YOUR ACCESS KEY')
    >>> fxrio.historical_rates(today)
    '''
    {'base': 'EUR',
     'date': '2016-05-27',
     'rates': {'AUD': 1.5483,
      'BGN': 1.9558,
      'BRL': 4.031,
      'CAD': 1.456,
      'CHF': 1.1068,
      'CNY': 7.3281,
      'CZK': 27.028,
      'DKK': 7.4367,
      'GBP': 0.76245,
      'HKD': 8.6735,
      'HRK': 7.4905,
      'HUF': 314.21,
      'IDR': 15157.25,
      'ILS': 4.2938,
      'INR': 74.867,
      'JPY': 122.46,
      'KRW': 1316.98,
      'MXN': 20.6611,
      'MYR': 4.5554,
      'NOK': 9.282,
      'NZD': 1.6586,
      'PHP': 52.096,
      'PLN': 4.3912,
      'RON': 4.5034,
      'RUB': 73.7516,
      'SEK': 9.2673,
      'SGD': 1.536,
      'THB': 39.851,
      'TRY': 3.2928,
      'USD': 1.1168,
      'ZAR': 17.4504}}
    '''

Request specific exchange rates by setting the ``symbols`` parameter.

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio(access_key='YOUR ACCESS KEY', symbols=['USD', 'GBP'])
    >>> fxrio.latest()
    '''
    {'base': 'EUR',
     'date': '2016-05-27',
     'rates': {'GBP': 0.76245, 'USD': 1.1168}}
    '''

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio(access_key='YOUR ACCESS KEY')
    >>> fxrio.latest(symbols=['USD', 'GBP'])
    '''
    {'base': 'EUR',
     'date': '2016-05-27',
     'rates': {'GBP': 0.76245, 'USD': 1.1168}}
    '''

All exceptions that ``fixerio`` explicitly raises are
``fixerio.exceptions.FixerioException``.

.. _Fixer API: https://apilayer.com/marketplace/fixer-api

.. |Build Status| image:: https://travis-ci.org/amatellanes/fixerio.svg?branch=master
    :target: https://travis-ci.org/amatellanes/fixerio
.. |Coverage Status| image:: https://coveralls.io/repos/github/amatellanes/fixerio/badge.svg?branch=feature%2Flatest-rates
    :target: https://coveralls.io/github/amatellanes/fixerio?branch=feature%2Flatest-rates
.. |Supports Wheel format| image:: https://img.shields.io/pypi/wheel/fixerio.svg
    :target: https://pypi.python.org/pypi/fixerio/
.. |Latest PyPI version| image:: https://img.shields.io/pypi/v/fixerio.svg
    :target: https://pypi.python.org/pypi/fixerio/
.. |Documentation Status| image:: https://readthedocs.org/projects/fixerio/badge/?version=latest
    :target: http://fixerio.readthedocs.io/en/latest/?badge=latest
.. |Requirements Status| image:: https://requires.io/github/amatellanes/fixerio/requirements.svg?branch=develop
    :target: https://requires.io/github/amatellanes/fixerio/requirements/?branch=develop

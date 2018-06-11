A Python client for `Fixer.io`_
===============================

|Build Status| |Coverage Status| |Supports Wheel format|
|Latest PyPI version| |Documentation Status| |Requirements Status|

`Fixer.io`_ is a free JSON API for current and historical foreign
exchange rates published by the European Central Bank.

The rates are updated daily around 3PM CET.

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
     {u'base': u'EUR',
     u'date': u'2016-05-27',
     u'rates': {u'AUD': 1.5483,
      u'BGN': 1.9558,
      u'BRL': 4.031,
      u'CAD': 1.456,
      u'CHF': 1.1068,
      u'CNY': 7.3281,
      u'CZK': 27.028,
      u'DKK': 7.4367,
      u'GBP': 0.76245,
      u'HKD': 8.6735,
      u'HRK': 7.4905,
      u'HUF': 314.21,
      u'IDR': 15157.25,
      u'ILS': 4.2938,
      u'INR': 74.867,
      u'JPY': 122.46,
      u'KRW': 1316.98,
      u'MXN': 20.6611,
      u'MYR': 4.5554,
      u'NOK': 9.282,
      u'NZD': 1.6586,
      u'PHP': 52.096,
      u'PLN': 4.3912,
      u'RON': 4.5034,
      u'RUB': 73.7516,
      u'SEK': 9.2673,
      u'SGD': 1.536,
      u'THB': 39.851,
      u'TRY': 3.2928,
      u'USD': 1.1168,
      u'ZAR': 17.4504}}
    '''

Get historical rates for any day since 1999.

.. code:: python

    >>> import datetime
    >>> from fixerio import Fixerio

    >>> today = datetime.date.today()
    >>> fxrio = Fixerio(access_key='YOUR ACCESS KEY')
    >>> fxrio.historical_rates(today)
    '''
    {u'base': u'EUR',
     u'date': u'2016-05-27',
     u'rates': {u'AUD': 1.5483,
      u'BGN': 1.9558,
      u'BRL': 4.031,
      u'CAD': 1.456,
      u'CHF': 1.1068,
      u'CNY': 7.3281,
      u'CZK': 27.028,
      u'DKK': 7.4367,
      u'GBP': 0.76245,
      u'HKD': 8.6735,
      u'HRK': 7.4905,
      u'HUF': 314.21,
      u'IDR': 15157.25,
      u'ILS': 4.2938,
      u'INR': 74.867,
      u'JPY': 122.46,
      u'KRW': 1316.98,
      u'MXN': 20.6611,
      u'MYR': 4.5554,
      u'NOK': 9.282,
      u'NZD': 1.6586,
      u'PHP': 52.096,
      u'PLN': 4.3912,
      u'RON': 4.5034,
      u'RUB': 73.7516,
      u'SEK': 9.2673,
      u'SGD': 1.536,
      u'THB': 39.851,
      u'TRY': 3.2928,
      u'USD': 1.1168,
      u'ZAR': 17.4504}}
    '''

Request specific exchange rates by setting the ``symbols`` parameter.

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio(access_key='YOUR ACCESS KEY', symbols=['USD', 'GBP'])
    >>> fxrio.latest()
    '''
    {u'base': u'EUR',
     u'date': u'2016-05-27',
     u'rates': {u'GBP': 0.76245, u'USD': 1.1168}}
    '''

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio(access_key='YOUR ACCESS KEY')
    >>> fxrio.latest(symbols=['USD', 'GBP'])
    '''
    {u'base': u'EUR',
     u'date': u'2016-05-27',
     u'rates': {u'GBP': 0.76245, u'USD': 1.1168}}
    '''

All exceptions that ``fixerio`` explicitly raises are
``fixerio.exceptions.FixerioException``.

.. _Fixer.io: http://fixer.io/

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

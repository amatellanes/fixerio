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

    >>> fxrio = Fixerio()
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
    >>> fxrio = Fixerio()
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

Rates are quoted against the Euro by default. Quote against a different
currency by setting the ``base`` parameter in your request.

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio(base='USD')
    >>> fxrio.latest()
    '''
    {u'base': u'USD',
     u'date': u'2016-05-27',
     u'rates': {u'AUD': 1.3864,
      u'BGN': 1.7513,
      u'BRL': 3.6094,
      u'CAD': 1.3037,
      u'CHF': 0.99105,
      u'CNY': 6.5617,
      u'CZK': 24.201,
      u'DKK': 6.6589,
      u'EUR': 0.89542,
      u'GBP': 0.68271,
      u'HKD': 7.7664,
      u'HRK': 6.7071,
      u'HUF': 281.35,
      u'IDR': 13572.0,
      u'ILS': 3.8447,
      u'INR': 67.037,
      u'JPY': 109.65,
      u'KRW': 1179.2,
      u'MXN': 18.5,
      u'MYR': 4.079,
      u'NOK': 8.3112,
      u'NZD': 1.4851,
      u'PHP': 46.648,
      u'PLN': 3.9319,
      u'RON': 4.0324,
      u'RUB': 66.038,
      u'SEK': 8.2981,
      u'SGD': 1.3754,
      u'THB': 35.683,
      u'TRY': 2.9484,
      u'ZAR': 15.625}}
    '''

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio()
    >>> fxrio.latest(base='USD')
    '''
    {u'base': u'USD',
     u'date': u'2016-05-27',
     u'rates': {u'AUD': 1.3864,
      u'BGN': 1.7513,
      u'BRL': 3.6094,
      u'CAD': 1.3037,
      u'CHF': 0.99105,
      u'CNY': 6.5617,
      u'CZK': 24.201,
      u'DKK': 6.6589,
      u'EUR': 0.89542,
      u'GBP': 0.68271,
      u'HKD': 7.7664,
      u'HRK': 6.7071,
      u'HUF': 281.35,
      u'IDR': 13572.0,
      u'ILS': 3.8447,
      u'INR': 67.037,
      u'JPY': 109.65,
      u'KRW': 1179.2,
      u'MXN': 18.5,
      u'MYR': 4.079,
      u'NOK': 8.3112,
      u'NZD': 1.4851,
      u'PHP': 46.648,
      u'PLN': 3.9319,
      u'RON': 4.0324,
      u'RUB': 66.038,
      u'SEK': 8.2981,
      u'SGD': 1.3754,
      u'THB': 35.683,
      u'TRY': 2.9484,
      u'ZAR': 15.625}}
    '''

Request specific exchange rates by setting the ``symbols`` parameter.

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio(symbols=['USD', 'GBP'])
    >>> fxrio.latest()
    '''
    {u'base': u'EUR',
     u'date': u'2016-05-27',
     u'rates': {u'GBP': 0.76245, u'USD': 1.1168}}
    '''

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio()
    >>> fxrio.latest(symbols=['USD', 'GBP'])
    '''
    {u'base': u'EUR',
     u'date': u'2016-05-27',
     u'rates': {u'GBP': 0.76245, u'USD': 1.1168}}
    '''

An HTTPS endpoint is available.

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio(secure=True)
    >>> fxrio.latest()
    '''
    {u'base': u'EUR',
     u'date': u'2016-05-27',
     u'rates': {u'AUD': 1.5483,
     ...
    '''

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio()
    >>> fxrio.latest(secure=True)
    '''
    {u'base': u'EUR',
     u'date': u'2016-05-27',
     u'rates': {u'AUD': 1.5483,
     ...
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

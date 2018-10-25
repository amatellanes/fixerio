A Python client for `Fixer.io`_
===============================

|Build Status| |Coverage Status| |Supports Wheel format|
|Latest PyPI version| |Documentation Status| |Requirements Status|

`Fixer.io`_ is a simple and lightweight JSON API for current and
historical foreign exchange (forex) rates.

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

Returns real-time exchange rate data for all available or a specific set of
currencies.

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio(access_key='YOUR ACCESS KEY')
    >>> fxrio.latest()
    '''
     {
        'success': True,
        'timestamp': 1540479545,
        'base': 'EUR',
        'date': '2018-10-25',
        'rates':
        {
            'AUD': 1.5483,
            'BGN': 1.9558,
            'BRL': 4.031,
            'CAD': 1.456,
            [...]
        }
    }
    '''

Returns historical exchange rate data for all available or a specific set of
currencies.

.. code:: python

    >>> import datetime
    >>> from fixerio import Fixerio

    >>> today = datetime.date.today()
    >>> fxrio = Fixerio(access_key='YOUR ACCESS KEY')
    >>> fxrio.historical_rates(today)
    '''
    {
        'success': True,
        'timestamp': 1540480626,
        'historical': True,
        'base': 'EUR',
        'date': '2018-10-25',
        'rates': {
            'AUD': 1.5483,
            'BGN': 1.9558,
            'BRL': 4.031,
            'CAD': 1.456,
            [...]
        }
    }
    '''

Returns all available currencies.

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio(access_key='YOUR ACCESS KEY')
    >>> fxrio.symbols()
    '''
    {
        'success': True,
        'symbols': {
            'AED': 'United Arab Emirates Dirham',
            'AFN': 'Afghan Afghani',
            'ALL': 'Albanian Lek',
            'AMD': 'Armenian Dram',
            [...]
        }
    }
    '''

Request specific exchange rates by setting the ``symbols`` parameter.

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio(access_key='YOUR ACCESS KEY', symbols=['USD', 'GBP'])
    >>> fxrio.latest()
    '''
    {
        'success': True,
        'timestamp': 1540479545,
        'base': 'EUR',
        'date': '2018-10-25',
        'rates': {
            'GBP': 0.76245,
            'USD': 1.1168
        }
    }
    '''

.. code:: python

    >>> from fixerio import Fixerio

    >>> fxrio = Fixerio(access_key='YOUR ACCESS KEY')
    >>> fxrio.latest(symbols=['USD', 'GBP'])
    '''
    {
        'success': True,
        'timestamp': 1540479545,
        'base': 'EUR',
        'date': '2018-10-25',
        'rates': {
            'GBP': 0.76245,
            'USD': 1.1168
        }
    }
    '''

All exceptions that ``fixerio`` explicitly raises are
``fixerio.exceptions.FixerioException``.

.. _Fixer.io: https://fixer.io/

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

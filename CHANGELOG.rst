.. :changelog:

Release History
---------------

1.1.0 (2023-??-??)
~~~~~~~~~~~~~~~~~~
- Update to the `new Fixer API endpoint on API Layer <https://api.apilayer.com/fixer/>`_.
- Re-add support for changing base currency. This option is once again supported by Free Plan.
- Always use TLS encrypted endpoint, since this is once again supported by Free Plan.
- Add new API function, available_currencies(), for listing supported currency symbols.
- Replace unit tests based on nosetest with unit tests based on pytest (nose is not supported
  by modern Python 3 versions).
- Remove support for Python 2.
- Add type hints for all methods.

1.0.0-alpha (2018-06-13)
~~~~~~~~~~~~~~~~~~~~~~~~
- Update to the `new Fixer endpoint <https://data.fixer.io/api/>`_.
- Add Fixer API Access Key support.
- Drop Changing base currency support. This option is not supported by Free Plan.
- Drop SSL Encryption support. This option is not supported by Free Plan.

0.1.1 (2016-06-16)
~~~~~~~~~~~~~~~~~~

- Initial version.

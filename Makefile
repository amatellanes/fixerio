SHELL := /bin/bash

help:
	@echo "Usage:"
	@echo " make test       to run test suite."
	@echo " make coverage   to run test suite with coverage."

test:
	nosetests

coverage:
	nosetests --with-coverage --cover-package=fixerio
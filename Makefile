SHELL := /bin/bash

help:
	@echo "Usage:"
	@echo " clean           remove all build, test, coverage and Python artifacts."
	@echo " clean-build     remove build artifacts."
	@echo " clean-pyc       remove Python file artifacts."
	@echo " clean-test      remove test and coverage artifacts."
	@echo " make coverage   run test suite with coverage."
	@echo " make lint       run code checker."
	@echo " make test       run test suite."

clean: clean-test clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .cache/
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

coverage:
	nosetests --config=.noserc

make lint:
	flake8
	prospector --messages-only

test:
	nosetests
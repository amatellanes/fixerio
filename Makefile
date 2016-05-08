SHELL := /bin/bash

help:
	@echo "Usage:"
	@echo " clean           remove all build, test, coverage and Python artifacts."
	@echo " clean-build     remove build artifacts."
	@echo " clean-pyc       remove Python file artifacts."
	@echo " clean-test      remove test and coverage artifacts."
	@echo " make test       run test suite."
	@echo " make coverage   run test suite with coverage."

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
	nosetests --with-coverage --cover-package=fixerio --cover-html --cover-html-dir=htmlcov

test:
	nosetests
SHELL := /bin/bash

.PHONY: help
help:
	@echo "Usage:"
	@echo " clean           remove all build, test, coverage and Python artifacts."
	@echo " clean-docs      remove docs artifacts."
	@echo " clean-build     remove build artifacts."
	@echo " clean-pyc       remove Python file artifacts."
	@echo " clean-test      remove test and coverage artifacts."
	@echo " make coverage   run test suite with coverage."
	@echo " make lint       run code checker."
	@echo " make test       run test suite."
	@echo " make build      build source distribution."
	@echo " make wheel      build universal wheel."
	@echo " make upload     upload distributions."
	@echo " make manifest   check MANIFEST.in."

.PHONY: clean
clean: clean-docs clean-test clean-build clean-pyc

.PHONY: clean-docs
clean-docs:
	rm -fr docs/_build

.PHONY: clean-build
clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: clean-test
clean-test:
	rm -fr .cache/
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

.PHONY: coverage
coverage:
	nosetests --config=.noserc

.PHONY: lint
make lint:
	flake8
	prospector --messages-only

.PHONY: test
test:
	nosetests

.PHONY: build
build:
	python setup.py sdist

.PHONY: wheel
wheel:
	python setup.py bdist_wheel

.PHONY: upload
upload:
	python setup.py sdist bdist_wheel upload

.PHONY: manifest
manifest:
	check-manifest
# vim: noai:ts=4:sw=4:noet
PYTHON_MODULES := reinforcement_learning
PYTHON_TESTS := tests
PYTHONPATH := .
PYTHON_VERSION := 3.6
VENV := .venv
VENV_ON := $(VENV)/bin/activate
VENV_OFF := deactivate
PYTEST := env PYTHONPATH=$(PYTHONPATH) PYTEST=1 $(VENV)/bin/py.test
PYLINT := env PYTHONPATH=$(PYTHONPATH) $(VENV)/bin/pylint --disable=I0011 --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}"
PEP8 := env PYTHONPATH=$(PYTHONPATH) $(VENV)/bin/pycodestyle --repeat --ignore=E202,E501,E402
PYTHON := env PYTHONPATH=$(PYTHONPATH) $(VENV)/bin/python
PIP := $(VENV)/bin/pip

DEFAULT_PYTHON := python$(PYTHON_VERSION)
PYTHON_PATH := $(shell which $(DEFAULT_PYTHON))

VIRTUALENV := /usr/local/bin/virtualenv

REQUIREMENTS := -r requirements.txt

default: test pylint-full

python_exists:
ifndef PYTHON_PATH
	$(error Could not find $(DEFAULT_PYTHON) in your search path PATH=$(PATH))
endif

venv: python_exists
	@test -d $(VENV) || $(VIRTUALENV) -p $(DEFAULT_PYTHON) -q $(VENV)
	@. $(VENV_ON)

requirements: python_exists
	@if [ -d wheelhouse ]; then \
		$(PIP) install -q --no-index --find-links=wheelhouse $(REQUIREMENTS); \
	else \
		$(PIP) install -q $(REQUIREMENTS); \
	fi

bootstrap: venv requirements

check-coding-style: bootstrap
	@$(PEP8) $(PYTHON_MODULES)
	@$(PYLINT) -E $(PYTHON_MODULES)

pylint-full: check-coding-style
	@$(PYLINT) $(PYTHON_MODULES)

test: check-coding-style
	@$(PYTEST) $(PYTHON_TESTS)

check: python_exists
	@$(PYTEST) $(PYTHON_MODULES)

clean:
	@rm -f MANIFEST
	@rm -rf build dist
	@find $(PYTHON_MODULES) -type d -name "__pycache__" -exec rm -rf {} \; > /dev/null 2>&1
	@find $(PYTHON_TESTS) -type d -name "__pycache__" -exec rm -rf {} \; > /dev/null 2>&1

.PHONY: python_exists default venv requirements bootstrap check-coding-style pylint-full test check clean


.PHONY: init requirements tests

VENV=./venv/bin
REQUIREMENTS=$(VENV)/pip install -r backend/requirements.txt

init:
	python3 -m venv venv
	$(VENV)/python -m pip install --upgrade pip setuptools
	$(REQUIREMENTS)

requirements:
	$(REQUIREMENTS)

tests:
	$(VENV)/flake8 backend/app.py
	$(VENV)/black backend/app.py
	$(VENV)/pytest backend/tests.py
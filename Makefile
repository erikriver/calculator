.PHONY: backend requirements test-backend frontend test-frontend clean run all

###### Backend stuff

VENV=./venv/bin
REQUIREMENTS=$(VENV)/pip install -r backend/requirements.txt

backend:
	python3 -m venv venv
	$(VENV)/python -m pip install --upgrade pip setuptools
	$(REQUIREMENTS)

requirements:
	$(REQUIREMENTS)

test-backend:
	$(VENV)/flake8 backend/app.py
	$(VENV)/black backend/app.py
	$(VENV)/pytest backend/tests.py

###### Frontend stuff

frontend:
	cd ./frontend/ && \
	yarn && \
	yarn build && \
	mv ./build ../backend/client

test-frontend:
	cd ./frontend/ && \
	yarn && \
	yarn test

run:
	. $(VENV)/activate && \
	cd ./backend/ && \
	gunicorn -b 0.0.0.0:5000 app:app

clean:
	rm -rf venv && \
	rm -fr backend/client

all: backend frontend run
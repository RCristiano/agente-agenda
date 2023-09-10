SHELL:=/usr/bin/env bash

.PHONY: help clean run install

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "run - run the application"
	@echo "venv - create a virtualenv"
	@echo "install - install the dependencies"
	@echo ".env - create .env file"

clean:
	@echo "Removing cache"
	@find ./ -name '__pycache__' | xargs rm -rf;

run: install
	python run.py

venv: .env
	python -m venv venv
	source venv/bin/activate

install: venv
	pip install -r requirements-dev.txt

.env:
	@echo "Creating .env file"
	@cp .env.example .env
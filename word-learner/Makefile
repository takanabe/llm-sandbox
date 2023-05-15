.PHONY: all
all: format lint

.PHONY: format
format:
	poetry run isort *.py models/*.py
	poetry run black *.py models/*.py

.PHONY: lint
lint:
    # use pflake8 instead of flake8 to use pyproject.toml for flake8
    # https://github.com/csachs/pyproject-flake8
	poetry run pflake8
	poetry run isort --check --diff *.py models/*.py
	poetry run black --check *.py models/*.py

.PHONY: server
server:
	poetry run uvicorn server:app --host 0.0.0.0 --port 8000

.PHONY: client
client:
	poetry run python client.py

.PHONY: all
all: format lint

.PHONY: format
format:
	poetry run isort *.py
	poetry run black *.py

.PHONY: lint
lint:
    # use pflake8 instead of flake8 to use pyproject.toml for flake8
    # https://github.com/csachs/pyproject-flake8
	poetry run pflake8
	poetry run isort --check --diff *.py
	poetry run black --check *.py

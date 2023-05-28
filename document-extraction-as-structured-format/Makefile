.PHONY: all
all: format lint

.PHONY: format
format:
	poetry run isort app.py
	poetry run black app.py

.PHONY: lint
lint:
    # use pflake8 instead of flake8 to use pyproject.toml for flake8
    # https://github.com/csachs/pyproject-flake8
	poetry run pflake8 app.py
	poetry run isort --check --diff app.py
	poetry run black --check app.py

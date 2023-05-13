# Word learner

## Setup

```sh
pyenv install
pip install poetry
```

## Usage

### Launch server

```sh
poetry run uvicorn server:app --host 0.0.0.0 --port 8000
```

### Launch client

```sh
poetry run python client.py
```

## Tools

### LLM

- [LangChain](https://python.langchain.com/en/latest/)

### Web application

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)

### Database

- [SQLite](https://sqlite.org/index.html)
# Word learner

## What's this?

This is a word learning application testing LLM + LangChain. This application uses text completions to generate the information of English words.
As for the LLM prompts, this application uses a zero-shot demonstration (or one-shot) for predictions.


```sh
$ make client
poetry run python client.py
Please choose an option:
1. Word registration
2. Word list
Enter your choice (1 or 2): 1
Enter the word to register: unsupervised
+--------------+----------------------------------------------------------+------------------------------------------------------------------+------------------------------------+-------------------------------------------------------------------+
| Word         | English meaning                                          | English example                                                  | Japanese meaning                   | Japanese example                                                  |
+--------------+----------------------------------------------------------+------------------------------------------------------------------+------------------------------------+-------------------------------------------------------------------+
| unsupervised | [Adjective]: Not subject to supervision or control; free | 1. The unsupervised children were running around the playground. | [形容詞]: 相関なしの、直管されない | 1. 相関なしの子供たちが遊び場を回っていました。                   |
|              | [Verb]: To not provide with supervision or guidance      | 2. The teacher unsupervised the students during the test.        | [動詞]: 直管することをしない       | 2. 卒業者たちに学生を直管しなくていた先生は、テスト中で直管した。 |
+--------------+----------------------------------------------------------+------------------------------------------------------------------+------------------------------------+-------------------------------------------------------------------+

$ make client
poetry run python client.py
Please choose an option:
1. Word registration
2. Word list
Enter your choice (1 or 2): 2
+-----+--------------+----------------------------------------------------------+------------------------------------------------------------------+------------------------------------+-------------------------------------------------------------------+
| No. | Word         | English meaning                                          | English example                                                  | Japanese meaning                   | Japanese example                                                  |
+-----+--------------+----------------------------------------------------------+------------------------------------------------------------------+------------------------------------+-------------------------------------------------------------------+
| 1   | unsupervised | [Adjective]: Not subject to supervision or control; free | 1. The unsupervised children were running around the playground. | [形容詞]: 相関なしの、直管されない | 1. 相関なしの子供たちが遊び場を回っていました。                   |
|     |              | [Verb]: To not provide with supervision or guidance      | 2. The teacher unsupervised the students during the test.        | [動詞]: 直管することをしない       | 2. 卒業者たちに学生を直管しなくていた先生は、テスト中で直管した。 |
+-----+--------------+----------------------------------------------------------+------------------------------------------------------------------+------------------------------------+-------------------------------------------------------------------+
```

NOTE: The Japanese examples are weird and maybe need to improve the prompts passed to LLM.

## Setup

```sh
pyenv install
pip install poetry
```

## Usage

### Launch server

```sh
make server
```

### Launch client

```sh
make client
```

## Tools

### LLM

- [LangChain](https://python.langchain.com/en/latest/)

### Web application

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)

### Database

- [SQLite](https://sqlite.org/index.html)


## Related article

- [[2005.14165] Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)

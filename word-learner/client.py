from typing import List

import requests
from pydantic import parse_obj_as

from models.word_information import DBWordInformation
from prettytable import PrettyTable


def word_registration():
    url = "http://127.0.0.1:8000/word"
    word = input("Enter the word to register: ")

    response = requests.post(url, data=word.encode('utf-8'))

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Request failed with status code {response.status_code}")


def word_quiz():
    url = "http://127.0.0.1:8000/words"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        words = parse_obj_as(List[DBWordInformation], data)

        table = PrettyTable()
        table.field_names = [
            "No.",
            "Word",
            "English meaning",
            "English example",
            "Japanese meaning",
            "Japanese example",
        ]

        table.align = 'l'

        for word in words:
            # remove empty string and unnecessary white spaces at the beginning of the meanings.
            en_mean_split = [s.strip() for s in word.english_meaning.split('|') if len(s) > 0]
            ja_mean_split = [s.strip() for s in word.japanese_meaning.split('|') if len(s) > 0]
            table.add_row([
                word.id,
                word.word,
                # word.ipa_pronunciation,
                # word.phonetic_spelling,
                '\n'.join(en_mean_split),
                f"1. {word.english_example}\n2. {word.english_example2}",
                '\n'.join(ja_mean_split),
                f"1. {word.japanese_example}\n2. {word.japanese_example2}",
            ])
        print(table)
    else:
       print(f"Request failed with status code {response.status_code}")


def main():
    print("Please choose an option:")
    print("1. Word registration")
    print("2. Word quiz")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        word_registration()
    elif choice == "2":
        word_quiz()
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == '__main__':
    main()

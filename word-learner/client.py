from typing import List

import requests
from pydantic import parse_obj_as

from models.word_information import DBWordInformation


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

        for word in words:
            print(f"ID: {word.id}")
            print(f"Word: {word.word}")
            print(f"English meaning: {word.english_meaning}")
            print(f"English example: {word.english_example}")
            print(f"Japanese meaning: {word.japanese_meaning}")
            print(f"Japanese example: {word.japanese_example}")
            print("")
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
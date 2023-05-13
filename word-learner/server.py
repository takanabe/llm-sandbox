import os
import openai

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

def get_word_meaning(api_key, word):
    openai.api_key = api_key
    chat_completion =  openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Your are a professional English teacher."},
            {"role": "user", "content": "Teach the meaning of the following english word: " + word},
        ],
    )
    ret = chat_completion.choices[0].message.content
    return ret

def get_word_information(api_key, word):

    prompt = f"Please provide the following information for the English word'{word}':\n\n" \
             f"1. English meaning\n" \
             f"2. English example\n" \
             f"3. Japanese meaning\n" \
             f"4. Japanese example\n\n" \
             f"Answer:\n" \
             f"1. {{English meaning}}\n" \
             f"2. {{English example}}\n" \
             f"3. {{Japanese meaning}}\n" \
             f"4. {{Japanese example}}"

    data = {
        "prompt": prompt,
        "max_tokens": 200,
        "n": 1,
        "stop": None,
        "temperature": 0.5,
    }

    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.5,
    )

    ret = completion.choices[0].text

    # if answer:
    #     word_info = parse_answer(answer)
    #     table = PrettyTable()
    #     table.field_names = ["ID", "Word", "English Meaning", "English Example", "Japanese Meaning", "Japanese Example"]
    #     table.add_row([1, word, word_info["1"], word_info["2"], word_info["3"], word_info["4"]])
    #     print(table)
    # else:
    #     print(f"Could not find the information for '{word}'")
    return ret

def parse_answer(answer):
    lines = answer.split("\n")
    parsed_info = {}
    for line in lines:
        key, value = line.split(".", 1)
        parsed_info[key.strip()] = value.strip()
    return parsed_info


@app.post("/", response_class=PlainTextResponse)
async def receive_message(request: Request):
    data = await request.body()
    message = data.decode('utf-8')
    return f"You sent: {message}"

@app.post("/word", response_class=PlainTextResponse)
async def receive_word(request: Request):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("API key not found in environment variables. Please set the 'OPENAI_API_KEY' variable.")
        exit(1)

    data = await request.body()
    word = data.decode('utf-8')

    # Switch API
    # meaning = get_word_meaning(api_key, word)
    meaning = get_word_information(api_key, word)

    if meaning:
        return f"The meaning of '{word}' is: {meaning}"
    else:
        return f"Could not find the meaning of '{word}'"

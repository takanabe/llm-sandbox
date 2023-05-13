import os

import openai
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator

app = FastAPI()

class WordInformation(BaseModel):
    word: str = Field(description="the word")
    english_meaning: str = Field(description="meaning of the word in English")
    english_example: str = Field(description="example of the word in English")
    japanese_meaning: str = Field(description="meaning of the word in Japanese")
    japanese_example: str = Field(description="example of the word in Japanese")

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

    # Set up a parser + inject instructions into the prompt template.
    # https://python.langchain.com/en/latest/modules/prompts/output_parsers/examples/pydantic.html#
    parser = PydanticOutputParser(pydantic_object=WordInformation)
    query = f"""
        Instruction: You are an professional English Teacher.\n\n
        Question: Tell me about '{word}'.\n\n
    """
    template = "{query}.\n{format_instructions}\n"

    prompt = PromptTemplate(
        template=template,
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    _input = prompt.format_prompt(query=query)

    model = OpenAI(
        model_name="text-davinci-003",
    )

    output = model(_input.to_string())
    return parser.parse(output)

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

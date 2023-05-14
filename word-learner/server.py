import os

import openai
from langchain.llms import OpenAI
from langchain import PromptTemplate

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

from langchain.output_parsers import PydanticOutputParser
from typing import List

from langchain.memory import ConversationBufferMemory



from sqlmodel import Field, Session, SQLModel, create_engine, select

from models.word_information import WordInformation, DBWordInformation

app = FastAPI()
memory = ConversationBufferMemory()

abs_path = os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f"sqlite://{abs_path}/database.db")
SQLModel.metadata.create_all(engine)




def get_word_meaning(api_key, word):
    openai.api_key = api_key
    chat_completion = openai.ChatCompletion.create(
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
        Instruction: You are an professional English teacher.\n\n
        Question: Tell me about '{word}'.\n\n
    """
    template = "{query}.\n{format_instructions}\n"

    prompt = PromptTemplate(
        template=template,
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    model = OpenAI(
        max_tokens = 1000,
        model_name="text-davinci-003",
    )
    _input = prompt.format_prompt(query=query)
    output = model(_input.to_string())

    ret: WordInformation = parser.parse(output)

    wordInfo: DBWordInformation = DBWordInformation(
        word=ret.word,
        # ipa_pronunciation=ret.ipa_pronunciation,
        # phonetic_spelling=ret.phonetic_spelling,
        english_meaning=ret.english_meaning,
        english_example=ret.english_example,
        english_example2=ret.english_example2,
        japanese_meaning=ret.japanese_meaning,
        japanese_example=ret.japanese_example,
        japanese_example2=ret.japanese_example2,
    )

    with Session(engine) as session:
        session.add(wordInfo)
        session.commit()

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

@app.get("/words", response_model=List[DBWordInformation])
async def list_words() -> List[DBWordInformation]:
    with Session(engine) as session:
        query = select(DBWordInformation)
        ret: List[DBWordInformation] = session.exec(query).all()
        return ret


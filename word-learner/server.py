import os
from typing import List

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.output_parsers import PydanticOutputParser
from sqlmodel import Session, SQLModel, create_engine, select

from models.word_information import WordInformation

# LangChain uses OPENAI_API_KEY
# https://python.langchain.com/en/latest/ecosystem/openai.html#installation-and-setup
if not os.environ.get("OPENAI_API_KEY"):
    print("API key not found in environment variables. Please set the 'OPENAI_API_KEY' variable.")
    exit(1)

# Setup API server
app = FastAPI()

# Setup DB
abs_path = os.path.dirname(os.path.abspath(__file__))
# An absolute path, which is denoted by starting with a slash, means you need four slashes:
# https://docs.sqlalchemy.org/en/13/dialects/sqlite.html#connect-strings
engine = create_engine(f"sqlite:///{abs_path}/database.sqlite")
SQLModel.metadata.create_all(engine)


def get_word_information(word):
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
        max_tokens=1000,
        model_name="text-davinci-003",
    )

    _input = prompt.format_prompt(query=query)
    output = model(_input.to_string())

    word_info: WordInformation = parser.parse(output)
    # remove ID assigned by LangChain and OutputParser
    # to rely on the ID autoincrement of DB.
    word_info.id = None

    with Session(engine, expire_on_commit=False) as session:
        session.add(word_info)
        session.commit()

    return word_info


@app.post("/", response_class=PlainTextResponse)
async def receive_message(request: Request):
    data = await request.body()
    message = data.decode("utf-8")
    return f"You sent: {message}"


@app.post("/word", response_model=WordInformation)
async def receive_word(request: Request):
    data = await request.body()
    word = data.decode("utf-8")

    ret: WordInformation = get_word_information(word)

    if ret:
        return ret
    else:
        return f"Could not find the meaning of '{word}'"


@app.get("/words", response_model=List[WordInformation])
async def list_words() -> List[WordInformation]:
    with Session(engine) as session:
        query = select(WordInformation)
        ret: List[WordInformation] = session.exec(query).all()
        return ret

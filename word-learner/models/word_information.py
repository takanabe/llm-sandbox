from pydantic import BaseModel
from sqlmodel import Field, SQLModel

class WordInformation(BaseModel):
    word: str = Field(description="the word")
    english_meaning: str = Field(description="meaning of the word in English")
    english_example: str = Field(description="example of the word in English")
    japanese_meaning: str = Field(description="meaning of the word in Japanese")
    japanese_example: str = Field(description="example of the word in Japanese")


class DBWordInformation(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    word: str
    english_meaning: str
    english_example: str
    japanese_meaning: str
    japanese_example: str


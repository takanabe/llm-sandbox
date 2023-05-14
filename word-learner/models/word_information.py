from pydantic import BaseModel
from sqlmodel import Field, SQLModel

class WordInformation(BaseModel):
    word: str = Field(description="the word in small letters")
    # NOTE: the answer for pronunciation is not always correct and need to find a way to get the correct pronunciation.
    # ipa_pronunciation: str = Field(description="American International Phonetic Alphabet (IPA) of the word")
    #
    # https://ell.stackexchange.com/questions/266826/why-does-google-show-the-pronunciation-of-teacher-as-%CB%88t%C4%93ch%C9%99r-not-%CB%88ti-t%CA%83%C9%9C%CB%90
    # https://en.wikipedia.org/wiki/Pronunciation_respelling_for_English
    # https://en.wikipedia.org/wiki/Google_Dictionary
    # phonetic_spelling: str = Field(description="American non-phonemic pronunciation respelling of the word what Google provides in small letters")
    english_meaning: str = Field(description="Meaning of the word in English. List as many word classes as possible. Add the prefix [<word_class>]: and add '|' at the end of each word class if there are following word classes. For example, '[Noun]: A person or thing that provides assistance|[Adjective]: Serving to aid or support; supplementary'")
    english_example: str = Field(description="Example of the word in English. The situation is that software engineers are learning English")
    english_example2: str = Field(description="Example of the word in English 2. The situation is that software engineers are learning English")
    japanese_meaning: str = Field(description="Meaning of the word in Japanese. List as many word classes as possible. Add the prefix [<word_class>]: and add '|' at the end of each word class if there are following word classes. For example, '[名詞]: 援助者, 手助けとなる人または物|[形容詞]: 補助の,補助的な'")
    japanese_example: str = Field(description="Japanese translation of the English example")
    japanese_example2: str = Field(description="Japanese translation of the English example 2")


class DBWordInformation(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    word: str
    # ipa_pronunciation: str
    # phonetic_spelling: str
    english_meaning: str
    english_example: str
    english_example2: str
    japanese_meaning: str
    japanese_example: str
    japanese_example2: str


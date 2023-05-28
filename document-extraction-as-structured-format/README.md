# Document extraction as structured format

A LLM application to extract information given structured format. This application uses the following LLM concepts:

- Text embedding with vector DB
- Retrieve answers from documents by using the vector DB
- Extraction as structure format with an output parser

## Concept

See https://docs.langchain.com/docs/use-cases/extraction

>Most APIs and databases still deal with structured information. Therefore, in order to better work with those, it can be useful to extract structured information from text. Examples of this include:
>
>- Extracting a structured row to insert into a database from a sentence
>- Extracting multiple rows to insert into a database from a long document
>- Extracting the correct API parameters from a user query
>
>This work is extremely related to [output parsing](https://python.langchain.com/en/latest/modules/prompts/output_parsers.html). Output parsers are responsible for instructing the LLM to respond in a specific format. In this case, the output parsers specify the format of the data you would like to extract from the document. Then, in addition to the output format instructions, the prompt should also contain the data you would like to extract information from.
>
>While normal output parsers are good enough for basic structuring of response data, when doing extraction you often want to extract more complicated or nested structures. For a deep dive on extraction, we recommend checking out kor, a library that uses the existing LangChain chain and OutputParser abstractions but deep dives on allowing extraction of more complicated schemas.

## Setting note

```
pyenv local 3.11.3
poetry init
poetry config virtualenvs.in-project true --local
```


## Result

<details>
<summary>$ poetry run python app.py</summary>

```
token: 37450


> Entering new StuffDocumentsChain chain...


> Entering new LLMChain chain...
Prompt after formatting:
Use the following pieces of context to answer the question at the end. If you don't know the answer,
    just say that you don't know, don't try to make up an answer.

    Context:
    ---------
    Coca-Cola
Coca-Cola has retained many of its
historical design features in modern
glass bottles.
Type Cola
Manufacturer The Coca-
Cola
Company
Country of origin United States
Region of origin Atlanta,
Georgia, U.S.
Introduced May 8, 1886
Color Caramel E-
150d
Variants Diet CokeCoca-Cola
Coca-Cola, or Coke, is a carbona ted soft drink manufactured by
the Coca-Cola Company. In 2013, Coke produc ts were sold in
over 200 countries worldwide, with consumers drinking more than
1.8 billion company beverage servings each day.[1] Coca-Cola
ranked No. 87 in the 2018 Fortune 500 list of the largest United
States corporations by total revenue.[2] Based on Interbrand's "best
global brand" study of 2020, Coca-Cola was the world's sixth
most valuable brand.[3]
Originally marketed as a temperance drink and intended as a patent
medicine, it was invented in the late 19th century by John Stith
Pemberton in Atlanta, Georgia. In 1888, Pemberton sold Coca-
Cola's ownership rights to Asa Griggs Candler, a businessman,
whose marketing tactics led Coca-Cola to its dominance of the
global soft-drink market throughout  the 20th and 21st century.[4]
The drink's name refers to two of its original ingredients: coca
leaves and kola nuts (a source of caffeine).[5] The current formula
of Coca-Cola remains a closely guarded trade secret; however, a
variety of reported recipes and experimental recreations have been
published. The secrecy around the formula has been used by
Coca-Cola in its marketing as only a handful of anonym ous
employees know  the formula.[6] The drink has inspired imitators
and created a whole classification of  soft drink: colas.
The Coca-Cola Company produc es concentrate, which is then sold
to licensed Coca-Cola bottlers throughout  the world. The bottlers,
who hold exclusive territory contracts with the company, produc e
the finished produc t in cans and bottles from the concentrate, in
combination with filtered water and sweeteners. A typical 12-US-
fluid-ounc e (350 ml) can contains 38 grams (1.3 oz) of sugar
(usually in the form of high-fructose corn syrup in North America).
The bottlers then sell, distribute, and merchandise Coca-Cola to
retail stores, restaurants, and vending machines througho ut the
world. The Coca-Cola Company also sells concentrate for soda
fountains of major restaurants and foodservice distributors.
The Coca-Cola Company has on occasion introduc ed other cola
drinks under the Coke name. The most common of these is Diet
Coke, along with others including Caffeine-Free Coca-Cola, Diet
Coke Caffeine-Free, Coca-Cola Zero Sugar, Coca-Cola Cherry,

A Coca-Cola bottle designed by
Jean Paul Gaultier and inspired
by American singer Madonna[117]In 2009, in Italy, Coca-Cola Light had a Tribute to Fashion to
celebrate 100 years of the recognizable contour bottle. Well know n
Italian designers Alberta Ferretti, Blumarine, Etro, Fendi, Marni,
Missoni, Moschino, and Versace each designed limited edition
bottles.[118]
In 2019, Coca-Cola shared the first beverage bottle made with ocean
plastic.[119]
Pepsi, the flagship produc t of PepsiCo, the Coca-Cola Company's main rival in the soft drink industry, is
usually second to Coke in sales, and outsells Coca-Cola in some markets. RC Cola, now owned by the Dr
Pepper Snapple Group, the third-largest soft drink m anufacturer, is also widely available.[120]
Around the world, many local brands compete with Coke. In South and Central America Kola Real, also
know n as Big Cola, is a growing competitor to Coca-Cola.[121] On the French island of Corsica, Corsica
Cola, made by brewers of the local Pietra beer, is a growing competitor to Coca-Cola. In the French region
of Brittany, Breizh Cola is available. In Peru, Inca Kola outsells Coca-Cola, which led the Coca-Cola
Company to purchase the brand in 1999. In Sweden, Julmust outsells Coca-Cola during the Christmas
season.[122] In Scotland, the locally produc ed Irn-Bru was more popul ar than Coca-Cola until 2005, when
Coca-Cola and Diet Coke began to outpace its sales.[123] In the former East Germany, Vita Cola, invented
during communist rule, is gaining popul arity.
In India, Coca-Cola ranked third behind the leader, Pepsi, and local drink Thums Up. The Coca-Cola
Company purchased Thums Up in 1993.[124] As of 2004 , Coca-Cola held a 60.9%  market-share in
India.[125] Tropicola, a domestic drink, is served in Cuba instead of Coca-Cola, due to a United States
embargo. French brand Mecca-Cola[126] and British brand Qibla Cola[127] are competitors to Coca-Cola in
the Middle East.
In Turkey, Cola Turka, in Iran and the Middle East, Zamzam and Parsi Cola, in some parts of China, Future
Cola, in the Czech Republic and Slovakia, Kofola, in Slovenia, Cockta, and the inexpensive Mercator
Cola, sold only in the country's biggest supermarket chain, Mercator, are some of the brand's competitors.
Classiko Cola, made by Tiko Group, the largest manufacturing company in Madagascar, is a competitor to
Coca-Cola in many regions.[128]
In 2021, Coca-Cola petitioned to cancel registrations for the marks Thums Up and Limca issued to
Meenaxi Enterprise, Inc. based on misrepresentation of source. The Trademark Trial and Appeal Board
concluded that "Meenaxi engaged in blatant misuse in a manner calculated to trade on the goodw ill andCompetitors

Hays, Constance L. The Real Thing: Truth and Power at the Coca-Cola Company. New
York: Random House, 2004.
Kahn, Ely J., Jr. The Big Drink: The Story of Coca-Cola. New York: Random House, 1960.
Louis, Jill Chen and Harvey Z. Yazijian. The Cola Wars. New York: Everest House
Publishers, 1980.
Oliver, Thomas. The Real Coke, The Real Story. New York: Random House, 1986.
Pendergrast, Mark. For God, Country, and Coca-Cola: The Unauthorized History of the Great
American Soft Drink And the Company That Makes It. New York: Basic Books, 2000.
Isdell, Neville. Inside Coca-Cola: A CEO's Life Story of Building the World's Most Popular
Brand. With the assistance of David Beasley. New York: St. Martin's Press, 2011.
Official website (https://www.coca-cola.com/)
Kinescope of a live 1954 TV commercial for Coca-Cola (Internet Archive) (https://archive.org/
details/Coke_Commercial)
Coca-Cola Advertising History (http://jipemania.com/coke) (in Portuguese)
The Contour Bottle (http://www.contourbottle.com/)
Coca-Cola: Refreshing Memories (https://web.archive.org/web/20110529094049/http://www.
life.com/gallery/60951/coca-cola-refreshing-memories#index/0) – slideshow by Life
China Advisory: Avoiding the Wax Tadpole – Effective Chinese Language Trademark
Strategy (https://web.archive.org/web/20091222190342/http://www.troutmansanders.com/11
-19-2008/) – Chinese language trademark for Coca-Cola
Retrieved from "https://en.wikipedia.org/w/index.php?title=Coca-Cola&oldid=1154277444"Primary sources
External links

An 1890s advertisement
showing model Hilda Clark
in formal 19th century attire.
The ad is titled Drink Coca-
Cola 5¢. (US).
Coca-Cola ghost sign in Fort Dodge,
Iowa. Older Coca-Cola ghosts behind
Borax and telephone ads. April 2008.
Coca-Cola delivery truck of
Argentina, with the slogan "Drink
Coca-Cola – delicious, refreshing"reputation of Coca-Cola in an attempt to confuse consumers in the United States that its Thums Up and
Limca marks were licensed or produc ed by the source of the same types of cola and lemon-lime soda sold
unde r these marks for decades in India."[129]
Coca-Cola's advertising has significantly affected American culture, and it
is frequently credited with inventing the modern image of Santa Claus as an
old man in a red-and-white suit. Although the company did start using the
red-and-white Santa image in the 1930s, with its winter advertising
campaigns illustrated by Haddon Sundbl om, the motif was already
common.[130][131] Coca-Cola was not even the first soft drink company to
use the modern image of Santa Claus in its advertising: White Rock
Beverages used Santa in advertisements for its ginger ale in 1923, after first
using him to sell mineral water in 1915.[132][133] Before Santa Claus,
Coca-Cola relied on images of smartly dressed young women to sell its
beverages. Coca-Cola's first such advertisement appeared in 1895,
featuring the young B ostonian actress Hilda Clark as its spoke swoman.
1941 saw the first use of the nickname "Coke" as an official trademark for
the product, with a series of advertisements informing consumers that
"Coke means Coca-Cola".[134] In 1971, a song from a Coca-Cola
commercial called "I'd Like to Teach the World to Sing", produc ed by Billy
Davis, became a hit single. During the 1950s  the term cola wars emerged,
describing the on-going battle between Coca-Cola and Pepsi for
supremacy in the soft drink industry. Coca-Cola and Pepsi were
competing with new produc ts, global expansion, US marketing
initiatives and sport spons orships.[135]
Coke's advertising is pervasive, as one of Woodruff's stated goals
was to ensure that everyone  on Earth drank Coca-Cola as their
preferred beverage. This is especially true in southern areas of the
United States, such as Atlanta, where Coke was born.
Some Coca-Cola television commercials between 1960 through
1986 were written and produc ed by former Atlanta radio veteran
Don Naylor (WGST 1936–1950, WAGA 1951–1959)  during his
career as a produc er for the McCann Erickson advertising agency.
Many of these early television commercials for Coca-Cola featured
movie stars, sports heroes, and popul ar singers.
During the 1980s , Pepsi ran a series of television advertisements
showing people participating in taste tests demonstrating that,
according to the commercials, "fifty percent of the participants who
said they preferred Coke actually chose the Pepsi." Coca-Cola ran
ads to combat Pepsi's ads in an incident sometimes referred to as
the cola wars; one of Coke's ads compared the so-called Pepsi
challenge to two chimpanzees deciding which tennis ball was
furrier. Thereafter, Coca-Cola regained its leadership in the market.Advertising
    ---------

    The output should be formatted as a JSON instance that conforms to the JSON schema below.

As an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}}
the object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.

Here is the output schema:

{"properties": {"name": {"title": "Name", "description": "name of Coca Cola", "type": "string"}, "kind": {"title": "Kind", "description": "kind of Coca Cola", "type": "string"}, "inventor": {"title": "Inventor", "description": "inventor of Coca Cola", "type": "string"}, "born_date": {"title": "Born Date", "description": "born date of Coca Cola", "type": "string"}}, "required": ["name", "kind", "inventor", "born_date"]}

    Question: What is Coca Cola?


> Finished chain.

> Finished chain.
# Question: What is Coca Cola?
app.py:94 <module>
    p: Product(
        name='Coca-Cola',
        kind='carbonated soft drink',
        inventor='John Stith Pemberton',
        born_date='May 8, 1886',
    ) (Product)

```
</details>
# Document summarizer

A LLM integrated application to summarize documents using OpenAI API and LangChain.

This application follows [Summarization — 🦜🔗 LangChain 0.0.181](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html).

# Load PDF using Document Loader

See [PDF — 🦜🔗 LangChain 0.0.181](https://python.langchain.com/en/latest/modules/indexes/document_loaders/examples/pdf.html)

```shell
poetry add pypdf
```

# Technique to overcome long documents with limited tokens

See [Index-related chains | 🦜️🔗 LangChain](https://docs.langchain.com/docs/components/chains/index_related_chains)

There are several chains to summarize indexes 

- Stuffing
- MapReduce
- Refine
- Map-Rerank

# Consideration

Stuffing cannot handle huge text data due to the LLM's token limitation. However, we sometimes don't need full texts to summarize documents. 
For example, we can reduce the sizes of stacktraces, and test failure logs by extracting only the last part of them.  In that case, Stuffing is the best option.


# Note

```shell
$ pyenv which python

/Users/takayuki-watanabe/.pyenv/versions/3.11.3/bin/python

# poetry virtual env for this project
$ poetry env info --path
/Users/takayuki-watanabe/Library/Caches/pypoetry/virtualenvs/document-summarizer-9OAneZ6r-py3.11

$ poetry env info

Virtualenv
Python:         3.11.3
Implementation: CPython
Path:           /Users/takayuki-watanabe/Library/Caches/pypoetry/virtualenvs/document-summarizer-9OAneZ6r-py3.11
Executable:     /Users/takayuki-watanabe/Library/Caches/pypoetry/virtualenvs/document-summarizer-9OAneZ6r-py3.11/bin/python
Valid:          True

System
Platform:   darwin
OS:         posix
Python:     3.11.3
Path:       /Users/takayuki-watanabe/.pyenv/versions/3.11.3
Executable: /Users/takayuki-watanabe/.pyenv/versions/3.11.3/bin/python3.11

```

# Result

As an example documents, this application summarizes [Coca-Cola - Wikipedia](https://en.wikipedia.org/wiki/Coca-Cola).

<details>
<summary>poetry run python app.py</summary>

```
$ poetry run python app.py

token: 37450


> Entering new RefineDocumentsChain chain...


> Entering new LLMChain chain...
Prompt after formatting:
Write a concise summary of the following:


"Coca-Cola
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
Coke Caffeine-Free, Coca-Cola Zero Sugar, Coca-Cola Cherry,"


CONCISE SUMMARY:

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:  Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke and Coca-Cola Zero Sugar.
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
Diet Coke
Caffeine-Free
Caffeine-Free
Coca-Cola
Coca-Cola
Zero Sugar
Coca-Cola
Cherry
Coca-Cola
Vanilla
Coca-Cola
Citra
Coca-Cola
Lime
Coca-Cola
Mango
Related productsPepsi
RC Cola
Afri-Cola
Postobón
Inca Kola
Kola Real
Cavan Cola
Website coca-cola.com
(https://www.c
oca-cola.co
m/)
John Pemberton, the original
creator of Coca-Cola
Believed to be the first coupon ever,
this ticket for a free glass of Coca-
Cola was first distributed in 1888 to
help promote the drink. By 1913, the
company had redeemed 8.5 million
tickets.[7]Coca-Cola Vanilla, and special versions with lemon, lime, and
coffee. Coca-Cola was called Coca-Cola Classic from July 1985
to 2009, t o distinguish it from "New Coke".
Confederate Colonel John
Pemberton, wounde d in the
American Civil War and addicted
to morphine, also had a medical
degree and began a quest to find a
substitute for the problematic
drug.[8] In 1885 at Pemberton's
Eagle Drug and Chemical House,
his drugstore in Columbus,
Georgia, he registered Pemberton's
French Wine Coca nerve
tonic.[9][10][11][12] Pemberton's
tonic may have been inspired by
the formidable success of Vin
Mariani, a French-Corsican coca
wine,[13] but his recipe additionally included the African kola nut,
the beverage's source of caffeine.[14] A Spanish drink called "Kola
Coca" was presented at a contest in Philadelphia in 1885, a year
before the official birth of Coca-Cola. The rights for this Spanish
drink w ere bought  by C oca-Cola in 1953.[15]
In 1886, when Atlanta and Fulton County passed prohibition
legislation, Pemberton responde d by developing Coca-Cola, a
nona lcoholic version of Pemberton's French Wine Coca.[16] It was
marketed as "Coca-Cola: The temperance drink", which appealed
to many people as the temperance movement enjoyed wide suppo rt
during this time.[4] The first sales were at Jacob's Pharmacy in
Atlanta, Georgia, on May 8, 1886,[17] where it initially sold for five
cents a glass.[18] Drugstore soda fountains were popul ar in the
United States at the time due to the belief that carbona ted water was
good for the health,[19] and Pemberton's new drink was marketed
and sold as a patent medicine, Pemberton claiming it a cure for
many diseases, including morphine addiction, indigestion, nerve
disorders, headaches, and impotence. Pemberton ran the first
advertisement for the beverage on May 29 of the same year in the
Atlanta Journal.[20]
By 1888, three versions of Coca-Cola – sold by three separate businesses – were on the market. A co-
partnership had been formed on January 14, 1888, between Pemberton and four Atlanta businessmen: J.C.
Mayfield, A.O. Murphey, C.O. Mullahy, and E.H. Bloodw orth. Not codified by any signed document, aHistory
19th century historical origins
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, and Coca-Cola Mango. The original creator of Coca-Cola, John Pemberton, was a Confederate Colonel wounded in the American Civil War and addicted to morphine. He developed Coca-Cola as a non-alcoholic version of his French Wine Coca, which he marketed as a patent medicine with claims that it could cure many diseases. The first sales of Coca-Cola were at Jacob's Pharmacy in Atlanta, Georgia, on May 8, 1886.
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
This refurbished Coca-Cola
advertisement from 1943 is still
displayed in Minden, Louisiana.
Early Coca-Cola vending machine at
Biedenharn Museum and Gardens in
Monroe, Louisianaverbal statement given by Asa Candler years later asserted unde r
testimony that he had acquired a stake in Pemberton's company as
early as 1887.[21] John Pemberton declared that the name "Coca-
Cola" belonge d to his son, Charley, but the other two
manufacturers could continue to use the formula.[22]
Charley Pemberton's record of control over the "Coca-Cola" name
was the unde rlying factor that allowed for him to participate as a
major shareholder in the March 1888 Coca-Cola Company
incorporation filing made in his father's place.[23] Charley's
exclusive control over the "Coca-Cola" name became a continual
thorn in Asa Candler's side. Candler's oldest son, Charles Howard
Candler, authored a book in 1950 published by Emory University.
In this definitive biography about his father, Candler specifically
states: "on April 14, 1888, the young druggist Asa Griggs Candler
purchased a one-third interest in the formula of an almost
completely unknow n proprietary elixir known as Coca-Cola."[24]
The deal was actually between John Pemberton's son Charley and
Walker, Candler & Co. – with John Pemberton acting as cosigner
for his son. For $50 down and $500 in 30 days, Walker, Candler &
Co. obtained all of the one-third interest in the Coca-Cola
Company that Charley held, all while Charley still held on to the
name. After the April 14 deal, on April 17, 1888, one-half of the
Walker/Dozier interest shares were acquired by Candler for an
additional $750.[25]
In 1892, Candler set out to incorporate a second company, the
Coca-Cola Company (the current corporation). When Candler had
the earliest records of the "Coca-Cola Company" destroyed in
1910, the action was claimed to have been made during a move to
new corporation of fices around t his time.[26]
After Candler had gained a better foothold on Coca-Cola in April 1888, he nevertheless was forced to sell
the beverage he produc ed with the recipe he had unde r the names "Yum Yum" and "Koke". This was while
Charley Pemberton was selling the elixir, although a cruder mixture, unde r the name "Coca-Cola", all with
his father's blessing. After both names failed to catch on for Candler, by the middle of 1888, the Atlanta
pharmacist was quite anxious to establish a firmer legal claim to Coca-Cola, and hope d he could force his
two competitors, Walker and D ozier, completely out  of the business, as well.[25]
John Pemberton died sudde nly on August 16, 1888. Asa Candler then decided to move swiftly forward to
attain full control of the entire Coca-Cola operation.
Charley Pemberton, an alcoholic and opium addict, unne rved Asa Candler more than anyone  else. Candler
is said to have quickly maneuvered to purchase the exclusive rights to the name "Coca-Cola" from
Pemberton's son Charley immediately after he learned of Dr. Pemberton's death. One of several stories
states that Candler approached Charley's mother at John Pemberton's funeral and offered her $300 in cash
for the title to the name. Charley Pemberton was found on June 23, 1894, unconscious, with a stick of
opium by hi s side. Ten days later, Charley died at Atlanta's Grady H ospital at the age of 40.[27]Company
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, and Coca-Cola Mango. The original creator of Coca-Cola, John Pemberton, was a Confederate Colonel wounded in the American Civil War and addicted to morphine. He developed Coca-Cola as a non-alcoholic version of his French Wine Coca, which he marketed as a patent medicine with claims that it could cure many diseases. The first sales of Coca-Cola were at Jacob's Pharmacy in Atlanta, Georgia, on May 8, 1886. After John Pemberton's death in 1888, Asa
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
Bottling plant of Coca-Cola Canada
Ltd. January 8, 1941. Montreal,
Canada.In Charles Howard Candler's 1950 book about his father, he stated: "On August 30 [1888] , he [Asa
Candler] became the sole proprietor of Coca-Cola, a fact which was stated on letterheads, invoice blanks
and advertising copy."[24]
With this action on August 30, 1888, Candler's sole control became technically all true. Candler had
negotiated with Margaret Dozier and her brother Woolfolk Walker a full payment amounting to $1,000,
which all agreed Candler could pay off with a series of notes over a specified time span. By May 1, 1889,
Candler was now claiming full ownership of the Coca-Cola beverage, with a total investment outlay by
Candler for the drink enterprise over the years amounting to $2,300.[28]
In 1914, Margaret Dozier, as co-owner of the original Coca-Cola Company in 1888, came forward to claim
that her signature on the 1888 Coca-Cola Company bill of sale had been forged. Subsequent analysis of
other similar transfer documents had also indicated John Pemberton's signature had most likely been forged
as well, which some accounts claim was precipitated by hi s son C harley.[22]
On September 12, 1919, Coca-Cola Co. was purchased by a group of investors led by Ernest Woodruff's
Trust Company for $25 million and reincorporated unde r Delaware General Corporation Law. The
company publicly offered 500,000 shares of the company for $40 a share.[29][30] In 1923, his son Robert
W. Woodruff was elected President of the company. Woodruff expanded the company and brought  Coca-
Cola to the rest of the world. Coca-Cola began distributing bottles as “Six-packs”, encouraging customers
to pur chase the beverage for their hom e.[31]
During its first several decades, Coca-Cola officially wanted to be know n by its full-name despite being
commonly know n as "Coke". This was due to company fears that the term "coke" would eventually
become a generic trademark, which to an extent became true in the Southern United States where "coke" is
used even for non Coca-Cola produc ts. The company also didn't want to confuse its drink with the
similarly-named coal byproduc t that clearly wasn't safe to consume. Eventually, out for fears that another
company may claim the trademark for "Coke", Coca-Cola finally embraced it and officially endorsed the
name "Coke" in 1941. "Coke" eventually became a registered trademark of the Coca-Cola Company in
1945.[32]
In 1986, the Coca-Cola Company merged with two of their bottling operators (owned by JTL Corporation
and B CI Holding C orporation) to form Coca-Cola Enterprises Inc. (CCE).[33]
In December 1991, C oca-Cola Enterprises merged with the Johnston C oca-Cola Bottling G roup, I nc.[33]
The first bottling of Coca-Cola occurred in Vicksburg, Mississippi,
at the Biedenharn Candy Company on March 12, 1894.[34] The
proprietor of the bottling works was Joseph A. Biedenharn.[35] The
original bottles were Hutchinson bottles, very different from the
much later hobbl e-skirt design of  1915 now  so familiar.
A few years later two entrepreneurs from Chattanooga , Tennessee,
namely Benjamin F. Thomas and Joseph B. Whitehead, proposed
the idea of bottling and were so persuasive that Candler signed a
contract giving them control of the procedure for only one dollar.
Candler later realized that he had made a grave mistake.[36]
Candler never collected his dollar, but in 1899, Chattanooga
became the site of the first Coca-Cola bottling company. Candler remained very content just selling hisOrigins of bottling
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, and Coca-Cola Mango. The original creator of Coca-Cola, John Pemberton, was a Confederate Colonel wounded in the American Civil War and addicted to morphine. He developed Coca-Cola as a non-alcoholic version of his French Wine Coca, which he marketed as a patent medicine with claims that it could cure many diseases. The first sales of Coca-Cola were at Jacob's Pharmacy in Atlanta, Georgia, on May 8, 1886. After John Pemberton's death in 1888, Asa
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
Original framed Coca-Cola artist's
drawn graphic presented by the
Coca-Cola Company on July 12,
1944, to Charles Howard Candler on
the occasion of Coca-Cola's "1
Billionth Gallon of Coca-Cola Syrup"company's syrup.[37] The loosely termed contract proved to be problematic for the Coca-Cola Company for
decades to come. Legal matters were not helped by the decision of the bottlers to subcontract to other
companies, effectively becoming parent bottlers.[38] This contract specified that bottles would be sold at 5¢
each and ha d no f ixed dur ation, leading to the fixed price of Coca-Cola from 1886 t o 1959 .
The first outdoor wall advertisement that promoted the Coca-Cola drink was painted in 1894 in
Cartersville, Georgia.[39] Cola syrup was sold as an over-the-counter dietary supplement for upset
stomach.[40][41] By the time of its 50th anniversary, the soft drink had reached the status of a national icon
in the US. In 1935, it was certified kosher by Atlanta rabbi Tobias Geffen. With the help of Harold Hirsch,
Geffen was the first person outside the company to see the top-secret ingredients list after Coke faced
scrutiny from the American Jewish popul ation regarding the drink's kosher status.[42] Consequently, the
company made minor changes in the sourcing of some ingredients so it could continue to be consumed by
America's Jewish popul ation, including dur ing Passover.[43]
The longest running commercial Coca-Cola soda fountain
anywhere was Atlanta's Fleeman's Pharmacy, which first opened its
doors in 1914.[44] Jack Fleeman took over the pharmacy from his
father and ran it until 1995;  closing it after 81 years.[45] On July 12,
1944, the one-billionth gallon of Coca-Cola syrup was
manufactured by the Coca-Cola Company. Cans of Coke first
appeared in 1955.[46]
Sugar prices spiked in the 1970s  because of Soviet
demand/hoarding and possible futures contracts market
manipulation. The Soviet Union was the largest produc er of sugar
at the time. In 1974 Coca-Cola switched over to high-fructose corn
syrup because of the elevated prices.[47][48]
Sugar prices 1962-2022
On April 23, 1985, Coca-Cola, amid much publicity, attempted to change the formula of the drink with
"New Coke". Follow-up taste tests revealed most consumers preferred the taste of New Coke to both Coke
and Pepsi[49] but Coca-Cola management was unprepared for the public's nostalgia for the old drink,20th century
Sugar replaced with high-fructose corn syrup
New Coke
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.
k
> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, and Coca-Cola Mango. The original creator of Coca-Cola, John Pemberton, was a Confederate Colonel wounded in the American Civil War and addicted to morphine. He developed Coca-Cola as a non-alcoholic version of his French Wine Coca, which he marketed as a patent medicine with claims that it could cure many diseases. The first sales of Coca-Cola were at Jacob's Pharmacy in Atlanta, Georgia, on May 8, 1886. After John Pemberton's death in 1888, Asa
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
Claimed to be the first installation
anywhere of the 1948 model "Boat
Motor" styled Coca-Cola soda
dispenser, Fleeman's Pharmacy,
Atlanta, Georgia. The "Boat Motor"
soda dispenser was introduced in the
late 1930s and manufactured until
the late 1950s. Photograph c. 1948.
The Las Vegas Strip World of Coca-
Cola museum in 2003leading to a backlash. The company gave in to protests and
returned to the old formula unde r the name Coca-Cola Classic, on
July 10, 1985. "New Coke" remained available and was renamed
Coke II in 1992;  it was discontinued in 2002.
On July 5, 2005, it was revealed that Coca-Cola would resume
operations in Iraq for the first time since the Arab League boyc otted
the company in 1968.[50]
In April 2007, in Canada, the name "Coca-Cola Classic" was
changed back to "Coca-Cola". The word "Classic" was removed
because "New Coke" was no longe r in produc tion, eliminating the
need to differentiate between the two. The formula remained
unchanged. In January 2009, Coca-Cola stoppe d printing the word
"Classic" on the labels of 16-US-fluid-ounce (470 ml) bottles sold
in parts of the southeastern United States.[51] The change was part
of a larger strategy to rejuvenate the product's image.[51] The word
"Classic" was removed from all Coca-Cola produc ts by 201 1.
In November 2009, due to a dispute over wholesale prices of Coca-
Cola produc ts, Costco stoppe d restocking its shelves with Coke
and Diet Coke for two months; a separate pouring rights deal in
2013 saw Coke products removed from Costco food courts in favor
of Pepsi.[52] Some Costco locations (such as the ones in Tucson,
Arizona) additionally sell imported Coca-Cola from Mexico with
cane sugar instead of corn syrup from separate distributors.[53]
Coca-Cola introduc ed the 7.5-ounc e mini-can in 2009, and on
September 22, 2011, the company announc ed price reductions,
asking retailers to sell eight-packs for $2.99. That same day, Coca-
Cola announc ed the 12.5- ounc e bottle, to sell for 89 cents. A 16-
ounc e bottle has sold well at 99 cents since being re-introduc ed, but
the price was going up t o $1.19.[54]
In 2012, Coca-Cola resumed business in Myanmar after 60 years of
absence due to US-imposed investment sanctions against the
country.[55][56] Coca-Cola's bottling plant is located in Yangon  and is part of the company's five-year plan
and $200 million investment in Myanmar.[57] Coca-Cola with its partners is to invest US$5 billion in its
operations in India by 2020.[58]21st century
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, and Coca-Cola Mango. The original creator of Coca-Cola, John Pemberton, was a Confederate Colonel wounded in the American Civil War and addicted to morphine. He developed Coca-Cola as a non-alcoholic version of his French Wine Coca, which he marketed as a patent medicine with claims that it could cure many diseases. The first sales of Coca-Cola were at Jacob's Pharmacy in Atlanta, Georgia, on May 8, 1886. After John Pemberton's death in 1888, Asa
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
World of Coca-Cola museum in
Atlanta, GeorgiaIn February 2021, as a plan to combat plastic waste, Coca-Cola said that it would start selling its sodas in
bottles made from 100% recycled plastic material in the United States, and by 2030 planned to recycle one
bottle or can for each one it sold.[59] Coca-Cola started by selling 2000 paper bottles to see if they held up
due to the risk of safety and of  changing the taste of the drink.[60]
Carbonated water
Sugar (sucrose or high-fructose corn syrup (HFCS) depending on country of origin)
Caffeine
Phosphoric acid
Caramel color (E150d)
Natural flavorings[61]
A typical can of Coca-Cola (12 fl ounc es/355 ml) contains 39 grams of sugar,[62] 50 mg of sodium,
0 grams fat, 0 grams potassium, and 140 calories.[63] On May 5, 2014, Coca-Cola said it was working to
remove a controversial ingredient, brominated vegetable oil, from its drinks.[64]
A UK 330 m l can contains 35 gr ammes of sugar and 139 c alories.
The exact formula of Coca-Cola's natural flavorings (but not its other ingredients, which are listed on the
side of the bottle or can) is a trade secret. The original copy of the formula was held in Truist Financial's
main vault in Atlanta for 86 years. Its predecessor, the Trust Company, was the unde rwriter for the Coca-
Cola Company's initial public offering in 1919. On December 8, 2011, the original secret formula was
moved from the vault at SunTrust Banks to a new vault containing the formula which will be on display for
visitors to its World of Coca-Cola museum in dow ntown Atlanta.[65]
According to Snope s, a popul ar myth states that only two
executives have access to the formula, with each executive having
only half the formula.[66] However, several sources state that while
Coca-Cola does have a rule restricting access to only two
executives, each know s the entire formula and others, in addition to
the prescribed duo, ha ve know n the formulation pr ocess.[67]
On February 11, 2011, Ira Glass said on his PRI radio show, This
American Life, that TAL staffers had found a recipe in "Everett
Beal's Recipe Book" , reproduc ed in the February 28, 1979, issue
of The Atlanta Journal-Constitution, that they believed was either
Pemberton's original formula for Coca-Cola, or a version that he
made either before or after the produc t hit the market in 1886. TheProduction
Listed ingredients
Formula of natural flavorings
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, and Coca-Cola Mango. The original creator of Coca-Cola, John Pemberton, was a Confederate Colonel wounded in the American Civil War and addicted to morphine. He developed Coca-Cola as a non-alcoholic version of his French Wine Coca, which he marketed as a patent medicine with claims that it could cure many diseases. The first sales of Coca-Cola were at Jacob's Pharmacy in Atlanta, Georgia, on May 8, 1886. After John Pemberton's death in 1888, Asa
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
An early Coca-Cola advertisementformula basically matched the one found  in Pemberton's diary.[68][69][70] Coca-Cola archivist Phil Moone y
acknow ledged that the recipe "could be a precursor" to the formula used in the original 1886 produc t, but
emphasized that Pemberton's original formula is not the same as the one used in the current produc t.[71]
When launched, Coca-Cola's two key ingredients were cocaine and
caffeine. The cocaine was derived from the coca leaf and the
caffeine from kola nut (also spelled "cola nut" at the time), leading
to the name Coca-Cola.[72][73]
Pemberton called for five ounc es of coca leaf per gallon of syrup
(approximately 37 g/L), a significant dose; in 1891, Candler
claimed his formula (altered extensively from Pemberton's original)
contained only a tenth of this amount. Coca-Cola once contained
an estimated nine milligrams of cocaine per glass. (For comparison,
a typical dose or "line" of cocaine is 50–75 mg.[74]) In 1903, it was
removed.[75]
After 1904, instead of using fresh leaves, Coca-Cola started using
"spent" leaves – the leftovers of the cocaine-extraction process with
trace levels of cocaine.[76] Since then (by 1929[77]), Coca-Cola has
used a cocaine-free coca leaf extract. Today, that extract is prepared at a Stepan Company plant in
Maywood, New Jersey, the only manufacturing plant authorized by the federal gove rnment to import and
process coca leaves, which it obtains from Peru and Bolivia.[78] Stepan Company extracts cocaine from the
coca leaves, which it then sells to Mallinckrodt, the only company in the United States licensed to purify
cocaine for medicinal use.[79]
Long after the syrup had ceased to contain any significant amount of cocaine, in North Carolina "dope "
remained a common colloquialism for Coca-Cola, and "dope -wagons" were trucks that transported it.[80]
The kola nut acts as a flavoring and the original source of caffeine in Coca-Cola. It contains about 2.0 to
3.5%  caffeine, and ha s a bitter flavor.
In 1911, the US government sued in United States v. Forty Barrels and Twenty Kegs of Coca-Cola, hoping
to force the Coca-Cola Company to remove caffeine from its formula. The court found t hat the syrup, w hen
diluted as directed, would result in a beverage containing 1.21 grains (or 78.4 mg) of caffeine per 8 US
fluid ounc es (240 ml) serving.[81] The case was decided in favor of the Coca-Cola Company at the district
court, but subsequently in 1912, the US Pure Food and Drug Act was amended, adding caffeine to the list
of "habit-forming" and "deleterious" substances which must be listed on a produc t's label. In 1913 the case
was appealed to the Sixth Circuit in Cincinnati, where the ruling was affirmed, but then appealed again in
1916 to the Supreme Court, where the gove rnment effectively won as a new trial was ordered. The
company then voluntarily reduced the amount of caffeine in its produc t, and offered to pay the
gove rnment's legal costs to settle and avoid further litigation.Use of stimulants in formula
Coca leaf
Kola nuts for caffeine
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, and Coca-Cola Mango. The original creator of Coca-Cola, John Pemberton, was a Confederate Colonel wounded in the American Civil War and addicted to morphine. He developed Coca-Cola as a non-alcoholic version of his French Wine Coca, which he marketed as a patent medicine with claims that it could cure many diseases. The first sales of Coca-Cola were at Jacob's Pharmacy in Atlanta, Georgia, on May 8, 1886. After John Pemberton's death in 1888, Asa
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
Coca-Cola contains 34 m g of caffeine per 12 fluid ounc es (9.8 m g per 100 m l).[82]
The actual produc tion and distribution of Coca-Cola follows a franchising model. The Coca-Cola
Company only produc es a syrup concentrate, which it sells to bottlers through out the world, who hold
Coca-Cola franchises for one or more geographical areas. The bottlers produc e the final drink by mixing
the syrup with filtered water and sweeteners, putting the mixture into cans and bottles, and carbona ting it,
which the bottlers then sell and distribute to retail stores, vending machines, restaurants, and foodservice
distributors.[83]
The Coca-Cola Company owns minority shares in some of its largest franchises, such as Coca-Cola
Enterprises, Coca-Cola Amatil, Coca-Cola Hellenic Bottling Company, and Coca-Cola FEMSA, as well as
some smaller ones, such as Coca-Cola Bottlers Uzbekistan, but fully independent bottlers produc e almost
half of the volume sold in the world. Independent bottlers are allowed to sweeten the drink according to
local tastes.[84]
The bottling pl ant in Skopje, Macedonia, received the 2009 a ward for "Best Bottling C ompany".[85]
Since it announc ed its intention to begin distribution in Myanmar in June 2012, Coca-Cola has been
officially available in every country in the world except Cuba and North Korea.[86] However, it is reported
to be available in bot h countries as a grey import.[87][88]
Coca-Cola has been a point of legal discussion in the Middle East. In the early 20th century, a fatwa was
created in Egypt to discuss the question of "whether Muslims were permitted to drink Coca-Cola and Pepsi
cola."[89] The fatwa states: "According to the Muslim Hanefite, Shafi'ite, etc., the rule in Islamic law of
forbidding or allowing foods  and beverages is based on the presumption that such things are permitted
unless it can be shown that they are forbidden on the basis of the Qur'an."[89] The Muslim jurists stated
that, unless the Qur'an specifically prohibits the consumption of a particular produc t, it is permissible to
consume. Another clause was discussed, whereby the same rules apply if a person is unaware of the
condition or  ingredients of the item in que stion.
Coca-Cola first entered the Chinese market in the 1920s  and opted for a localized name "蝌蝌啃蜡" (Ke-
Ke Ken-La), but the name sounde d like chewing wax blocks, resulting in poor produc t sales. In the 1930s ,
the new localized name "可⼝可（可⼝可乐）" (Ke-kou ke-le), which means "Tasty and Fun", was
replaced, taking into account the effects of syllable translation and meaning translation, so that the sales of
the produc t increased and became a good translation case.[90][91] The story introduc tion from Coca-Cola
mentions that Chiang Yee provided the new localized name,[92] but there are also sources that the localized
name appeared before 1935,[93] or that it was given by someone named Jerome T. Lieu who studied at
Columbia University in New York.[94]
This is a list of variants of Coca-Cola introduc ed around the world. In addition to the caffeine-free version
of the original, additional fruit flavors have been included over the years. Not included here are versions of
Diet Coke and Coca-Cola Zero Sugar; variant versions of those no-calorie colas can be found at their
respective articles.Franchised production model
Geographic spread
Brand portfolio
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, and Coca-Cola Mango. The original creator of Coca-Cola, John Pemberton, was a Confederate Colonel wounded in the American Civil War and addicted to morphine. He developed Coca-Cola as a non-alcoholic version of his French Wine Coca, which he marketed as a patent medicine with claims that it could cure many diseases. The first sales of Coca-Cola were at Jacob's Pharmacy in Atlanta, Georgia, on May 8, 1886. After John Pemberton's death in 1888, Asa
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
Shortened "Coke" logo used on the
back of cans and included in the
logos of some flavor variationsCaffeine-Free Coca-Cola (1983–present) – Coca-Cola
without the caffeine.
Coca-Cola Cherry (1985–present) – Coca-Cola with a
cherry flavor. Was available in Canada starting in 1996.
Originally marketed as Cherry Coke (Cherry Coca-
Cola) in North America until 2006.
New Coke / Coca-Cola II (1985–2002) – An unpopular
formula change, remained after the original formula
quickly returned and was later rebranded as Coca-Cola
II until its full discontinuation in 2002. In 2019, New Coke
was re-introduced to the market to promote the third season of the Netflix original series,
Stranger Things.[95]
Golden Coca-Cola (2001) was a limited edition produced by Beijing Coca-Cola company to
celebrate Beijing's successful bid to host the Olympics.
Coca-Cola with Lemon (2001–2005) – Coca-Cola with a lemon flavor. Available in:
Australia, American Samoa, Austria, Belgium, Brazil, China, Denmark, Federation of Bosnia
and Herzegovina, Finland, France, Germany, Hong Kong, Iceland, Korea, Luxembourg,
Macau, Malaysia, Mongolia, Netherlands, New Caledonia, New Zealand, Réunion,
Singapore, Spain, Switzerland, Taiwan, Tunisia, the United Kingdom, the United States, and
West Bank-Gaza
Coca-Cola Vanilla (2002–2005; 2007–present) – Coca-Cola with a vanilla flavor. Available
in: Austria, Australia, China, Czech Republic, Canada, Finland, France, Germany, Hong
Kong, New Zealand, Malaysia, Slovakia, South-Africa, Sweden, Switzerland, the United
Kingdom, and the United States. It was reintroduced in June 2007 by popular demand.
Coca-Cola with Lime (2005–present) – Coca-Cola with a lime flavor. Available in Belgium,
Lithuania, Netherlands, Singapore, Canada, the United Kingdom, and the United States.
Coca-Cola Raspberry (2005; 2009–present) – Coca-Cola with a raspberry flavor. Originally
only available in New Zealand. Available in Australia, the United States, and the United
Kingdom in Coca-Cola Freestyle fountain since 2009.
Coca-Cola Citra (2005–present) – Coca-Cola with a citrus flavor. Only available in New
Zealand, and Japan.
Coca-Cola Black Cherry Vanilla (2006–2007) – Coca-Cola with a combination of black
cherry and vanilla flavor. It replaced and was replaced by Vanilla Coke in June 2007.
Coca-Cola Blāk (2006–2008) – Coca-Cola with a rich coffee flavor, formula depends on the
country. Only available in the United States, France, Canada, Czech Republic, Bosnia and
Herzegovina, Bulgaria, and Lithuania
Coca-Cola Orange (2007) – Coca-Cola with an orange flavor. Was available in the United
Kingdom and Gibraltar for a limited time. In Germany, Austria, and Switzerland it is sold
under the label Mezzo Mix. Currently available in Coca-Cola Freestyle fountain outlets in the
United States since 2009, and in the United Kingdom since 2014.
Coca-Cola Life (2013–2020) – A version of Coca-Cola with stevia and sugar as sweeteners
rather than simply sugar.
Coca-Cola Ginger (2016–present) – A version that mixes in the taste of ginger beer.
Available in Australia, New Zealand, and as a limited edition in Vietnam.
Coca-Cola Fiber+ (2017–present) – Diet variant of Coca-Cola with added dietary fiber in
the form of dextrin developed by Coca-Cola Asia Pacific. Available in Japan, Taiwan,
Mainland China, Hong Kong, Vietnam, and Mongolia
Coca-Cola Orange Vanilla (2019–2021) – Coca-Cola with an orange vanilla flavor
(intended to imitate the flavor of an orange Creamsicle). Made available nationwide in the
United States on February 25, 2019.[96]
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, and Coca-Cola Orange Vanilla. The original creator of Coca-Cola, John Pemberton, was a Confederate Colonel wounded in the American Civil War and addicted to morphine. He developed Coca-Cola as a non-alcoholic version of
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
Coca-Cola Energy (2019–present) – An energy drink with a flavor similar to standard Coca-
Cola, with guarana, vitamin B3 (niacinamide), vitamin B6 (pyridoxine hydrochloride), and
extra caffeine. Introduced in 2019 in the United Kingdom,[97] and released in the United
States and Canada in January 2020.[98] Also available in zero-sugar, cherry, and zero-sugar
+ cherry variants. In May 2021, the company announced they would discontinue the product
in North America but it will remain available in other places and it will focus on its traditional
beverages.[99]
Coca-Cola Cinnamon (2019–2020) – Coca-Cola with cinnamon flavor. Released in
October 2019 in the United States as a limited release for the 2019 holiday season.[100]
Made available again in 2020 for the holiday season.
Coca-Cola with Coffee (2019–present) – Coca-Cola, with coffee. Introduced in 2019 in
various European markets, and released in the United States and Canada in January 2021.
Available in dark blend, vanilla and caramel versions, and also in zero-sugar dark blend and
vanilla variants.
Coca-Cola Cherry Vanilla (2020–present) – Coca-Cola with cherry vanilla flavor. Released
in the United States on February 10, 2020.
Coca-Cola Starlight (2022) – Coca-Cola with a space-inspired flavor. Released in North
America on February 21, 2022, as a limited edition.
Coca-Cola Marshmello (2022–present) – Coca-Cola with strawberry and watermelon
flavor, made in collaboration with Marshmello. Released in 2022 as a limited edition.
Coca-Cola Dreamworld (2022–present) – Coca-Cola with a dream-inspired flavour.
Released in 2022 as a limited edition.
Coca-Cola Move / Movement (2023–present) – Coca-Cola with a transformation-inspired
flavour, made in collaboration with Rosalía. Released in early 2023 as a limited edition.
The Coca-Cola logo was created by John Pemberton's bookke eper, Frank Mason Robinson, in 1885.[101]
Robinson came up with the name and chose the logo's distinctive cursive script. The writing style used,
know n as Spencerian script, was developed in the mid-19th century and was the dominant form of formal
handwriting in the United States during that period.[102]
Robinson also played a significant role in early Coca-Cola advertising. His promotional sugge stions to
Pemberton included giving away thousands of free drink coupons  and plastering the city of Atlanta with
publicity banners and streetcar signs.[103]
Coca-Cola came unde r scrutiny in Egypt in 1951  because of a conspiracy theory that the Coca-Cola logo,
when reflected in a mirror, spells out "No Mohammed no Mecca" in Arabic.[104]
The Coca-Cola bottle, called the "contour bottle" within the company, was created by bottle designer Earl
R. Dean and Coca-Cola's general couns el, Harold Hirsch. In 1915, the Coca-Cola Company was
represented by their general counsel to launch a competition among its bottle suppliers as well as any
competition entrants to create a new bottle for their beverage that would distinguish it from other beverage
bottles, "a bottle which a person could recognize even if they felt it in the dark, and so shaped that, even if
broken, a person could tell at a glance what it was."[105][106][107][108]Logo design
Contour bottle design
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca-Cola Move/Move
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
Earl R. Dean standing next to the
Johnny Bull Machine, the mold
machine used to produce the early
Coca-Cola contour bottles
Illustration of a gourd-shaped cocoa
pod in the Encyclopædia BritannicaChapman J. Root, president of The Root Glass Company of Terre
Haute, Indiana, turned the project over to members of his
supervisory staff, including company auditor T. Clyde Edwards,
plant superintendent Alexander Samuelsson, and Earl R. Dean,
bottle designer and supervisor of the bottle molding room. Root and
his subordinates decided to base the bottle's design on one of the
soda's two ingredients, the coca leaf or the kola nut, but were
unaware of what either ingredient looke d like. Dean and Edwards
went to the Emeline Fairbanks Memorial Library and were unable
to find any information about coca or kola. Instead, Dean was
inspired by a picture of the gourd-shaped cocoa pod in the
Encyclopædia Britannica. Dean made a rough sketch of the pod
and returned to the plant to show Root. He explained to Root how
he could transform the shape of the pod into a bottle. Root gave
Dean his approval.[105]
Faced with the upcoming scheduled maintenance of the mold-
making machinery, over the next 24 hours Dean sketched out a
concept drawing which was approved by Root the next morning.
Chapman Root approved the prototype bottle and a design patent
was issued on the bottle in November 1915. The prototype never
made it to produc tion since its middle diameter was larger than its
base, making it unstable on conve yor belts. Dean resolved this
issue by decreasing the bottle's middle diameter. During the 1916
bottler's conve ntion, Dean's contour bottle was chosen over other
entries and was on the market the same year. By 1920, the contour
bottle became the standard for the Coca-Cola Company. A revised
version was also patented in 1923. Because the Patent Office
releases the Patent Gazette on Tuesday, the bottle was patented on
December 25, 1923, and was nicknamed the "Christmas bottle."
Today, the contour Coca-Cola bottle is one of the most recognized
packages on the planet.[38]
As a reward for his efforts, Dean was offered a choice between a
$500 bonus  or a lifetime job at The Root Glass Company. He
chose the lifetime job and kept it until the Owens-Illinois Glass
Company boug ht out The Root Glass Company in the mid-1930s .
Dean went on to work in other Midwestern glass factories.[109]
Raymond Loewy upda ted the design in 1955 to accommodate
larger formats.[110]
Others have attributed inspiration for the design not to the cocoa
pod, but  to a Victorian hoope d dress.[111]
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca-Cola Move/Move
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
In 1944, Associate Justice Roger J. Traynor of the Supreme Court of California took advantage of a case
involving a waitress injured by an exploding Coca-Cola bottle to articulate the doctrine of strict liability for
defective produc ts. Traynor's concurring opinion in Escola v. Coca-Cola Bottling Co. is widely recognized
as a landmark case in US law today.[112][113][114][115][116]
Earl R. Dean's original
1915 concept drawing of
the contour Coca-Cola
bottle
The prototype never
made it to production
since its middle diameter
was larger than its base,
making it unstable on
conveyor belts.
Final production version
with slimmer middle
section
Numerous historical
Coke bottles
Karl Lagerfeld is the latest designer to have created a collection of aluminum bottles for Coca-Cola.
Lagerfeld is not the first fashion designer to create a special version of the famous Coca-Cola Contour
bottle. A number of other limited edition bottles by fashion designers for Coca-Cola Light soda have been
created in the last few years, including Jean Paul Gaultier.[117]Examples
Designer bottles
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca-Cola Move/Move
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
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
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca-Cola Move/Move
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
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
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca-Cola Move/Move
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
Coca-Cola sales booth on the Cape
Verde island of Fogo in 2004
Coke advertisement in
Budapest, 2013Selena was a spokesperson for Coca-Cola from 1989 until the time
of her death. She filmed three commercials for the company.
During 1994, to commemorate her five years with the company,
Coca-Cola issued special Selena coke bottles.[136]
The Coca-Cola Company purchased Columbia Pictures in 1982,
and began inserting Coke-produc t images into many of its films.
After a few early successes during Coca-Cola's ownership,
Columbia began to underperform, and the studio was sold to Sony
in 1989.
Coca-Cola has gone  through a number of different advertising
slogans in its long history, including "The pause that refreshes",
"I'd like to buy t he world a Coke", and "Coke is it".
In 1999, the Coca-Cola Company introduc ed the Coke Card, a loyalty
program that offered deals on items like clothes, entertainment and food
when the cardholder purchased a Coca-Cola Classic. The scheme was
cancelled after three years, with a Coca-Cola spoke sperson declining to
state why.[137]
The company then introduc ed another loyalty campaign in 2006, My Coke
Rewards. This allows consumers to earn points by entering codes from
specially marked packages of Coca-Cola produc ts into a website. These
points can be redeemed for various prizes or sweepstakes entries.[138]
In Australia in 2011, Coca-Cola began the "share a Coke" campaign,
where the Coca-Cola logo was replaced on the bottles and replaced with
first names. Coca-Cola used the 150 most popul ar names in Australia to
print on the bottles.[139][140][141] The campaign was paired with a website
page, Facebook page, and an online "share a virtual Coke". The same campaign was introduc ed to Coca-
Cola, Diet Coke and C oke Zero bot tles and cans in the UK in 2013.[142][143]
Coca-Cola has also advertised its produc t to be consumed as a breakfast beverage, instead of coffee or tea
for the morning caffeine.[144][145]
From 1886 t o 1959, t he price of Coca-Cola was fixed at five cents, in part due to an advertising campaign.
Throughout  the years, Coca-Cola has released limited-time collector bottles for Christmas.
The "Holidays are coming!" advertisement features a train of red delivery trucks, emblazoned with the
Coca-Cola name and decorated with Christmas lights, driving through a snowy landscape and causing
everything that they pass to light up a nd pe ople to watch as they pass through.[146]
The advertisement fell into disuse in 2001, as the Coca-Cola Company restructured its advertising
campaigns so that advertising around the world was produc ed locally in each country, rather than centrally
in the company's headqua rters in Atlanta, Georgia.[147] In 2007, the company brought  back the campaign5 cents
Holiday campaigns
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca-Cola Move/Move
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
A Freightliner Coca-Cola
Christmas truck in Dresden,
Germany, 2004after, according to the company, many consumers telephone d its
information center saying that they considered it to mark the beginning of
Christmas.[146] The advertisement was created by US advertising agency
Doner, and has been part of the company's global advertising campaign for
many ye ars.[148]
Keith Law, a produc er and writer of commercials for Belfast CityBeat, was
not convinced by Coca-Cola's reintroduc tion of the advertisement in 2007,
saying that "I do not think there's anything Christmassy about HGVs and
the commercial is too ge neric."[149]
In 2001, singer Melanie Thornton recorded the campaign's advertising
jingle as a single, "Wonde rful Dream (Holidays Are Coming)", which
entered the pop-music charts in Germany at no. 9.[150][151] In 2005, Coca-
Cola expanded the advertising campaign to radio, employing several
variations of the jingle.[152]
In 2011, Coca-Cola launched a campaign for the Indian holiday Diwali.
The campaign included commercials, a song, and an integration with Shah Rukh Khan's film
Ra.One.[153][154][155]
Coca-Cola was the first commercial sponsor of the Olympic Games, at the 1928 games in Amsterdam, and
has been an Olympics sponsor ever since.[156] This corporate sponsorship included the 1996 Summer
Olympics hosted in Atlanta, which allowed Coca-Cola to spotlight its hometown. Most recently, Coca-Cola
has released localized commercials for the 2010 Winter Olympics in Vancouver; one Canadian commercial
referred to Canada's hockey heritage and was modified after Canada won the gold medal game on
February 28, 2010, by changing the ending line of the commercial to say "Now they know  whose game
they're playing".[157]
Since 1978 , Coca-Cola has sponsored the FIFA World Cup, and other competitions organized by
FIFA.[158] One FIFA tournament trophy , the FIFA World Youth Championship from Tunisia in 1977  to
Malaysia in 1997 , was called "FIFA – Coca-Cola Cup". In addition, Coca-Cola sponsors NASCAR's
annua l Coca-Cola 600 and Coke Zero Sugar 400 at Charlotte Motor Speedway in Concord, North
Carolina and Daytona International Speedway in Daytona, Florida; since 2020, Coca-Cola has served as a
premier partner of the NASCAR Cup Series, which includes holding the naming rights to the series' regular
season championship trophy .[159] Coca-Cola is also the spons or of the iRacing Pro Series.
Coca-Cola has a long history of sports marketing relationships, which over the years have included Major
League Baseball, the National Football League, the National Basketball Association, and the National
Hockey League, as well as with many teams within those leagues. Coca-Cola has had a longtime
relationship with the NFL's Pittsburgh Steelers, due in part to the now-famous 1979 television commercial
featuring "Mean Joe" Greene, leading to the two opening the Coca-Cola Great Hall at Heinz Field in 2001
and a more recent Coca-Cola Zero commercial featuring Troy Polamalu.
Coca-Cola is the official soft drink of many collegiate football teams throughout  the nation, partly due to
Coca-Cola providing those schools with upgraded athletic facilities in exchange for Coca-Cola's
sponsorship. This is especially prevalent at the high school level, which is more dependent on such
contracts due to tighter budge ts.Sports sponsorship
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca-Cola Move/Move
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
Coca-Cola advertised on a
Volkswagen T2 in Maringá, Paraná,
Brazil, 2012Coca-Cola was one of the official sponsors of the 1996 C ricket World Cup held on t he Indian subcontinent.
Coca-Cola is also one  of the associate sponsors of Delhi Capitals in the Indian Premier League.
In England, Coca-Cola was the main sponsor of The Football League between 2004 and 2010, a name
given to the three professional divisions below the Premier League in soccer (football). In 2005, Coca-Cola
launched a competition for the 72 clubs of The Football League – it was called "Win a Player". This
allowed fans to place one vote per day for their favorite club, with one entry being chosen at random
earning £250,000 for the club; this was repeated in 2006. The "Win A Player" competition was very
controversial, as at the end of the 2 competitions, Leeds United A.F.C. had the most votes by more than
doubl e, yet they did not win any money to spend on a new player for the club. In 2007, the competition
changed to "Buy a Player". This competition allowed fans to buy a bottle of Coca-Cola or Coca-Cola Zero
and submit the code on the wrapper on the Coca-Cola website. This code could then earn anything from
50p to £100,000 for a club of their choice. This competition was favored over the old "Win a Player"
competition, as it allowed all clubs to win some money. Between 1992 and 1998 , Coca-Cola was the title
sponsor of the Football League Cup (Coca-Cola Cup), the seconda ry cup tournament of England. Starting
in 2019–20 season, Coca-Cola has agreed its biggest UK sponsorship deal by becoming Premier League
football's seventh and final commercial partner[160] for the UK and Ireland, China, Malaysia, Indone sia,
Singapore, Egyptian and the West African markets.
Between 1994 and 1997, Coca-Cola was also the title sponsor of the Scottish League Cup, renaming it to
the Coca-Cola Cup like its English counterpart. From 1998 to 2001, the company was the title sponsor of
the Irish League Cup in Northern Ireland, where it was named the Coca-Cola League Cup.
Coca-Cola is the presenting sponsor of the Tour Championship, the final event of the PGA Tour held each
year at East Lake Golf Club in Atlanta, Georgia.[161]
Introduc ed March 1, 2010, in Canada, to celebrate the 2010 Winter Olympics, Coca-Cola sold gold colored
cans in packs of 12 355 m L (12 imp fl oz; 12 U S fl oz) each, in select stores.[162]
Coca-Cola which has been a partner with UEFA since 1988.[163]
Coca-Cola has been prominently featured in many films and
television programs. It was a major plot element in films such as
One, Two, Three, The Coca-Cola Kid, and The Gods Must Be
Crazy, among many others. In music, such as in the Beatles' song,
"Come Together", the lyrics say, "He shoot Coca-Cola". The
Beach Boys also referenced Coca-Cola in their 1964 song "All
Summer Long", singing "Member when you spilled Coke all over
your blouse?"[164]
The best selling solo artist of all time[165] Elvis Presley, promoted
Coca-Cola during his last tour of 1977 .[166] The Coca-Cola
Company used Presley's image to promote the produc t.[167] For
example, the company used a song performed by Presley, "A Little Less Conve rsation", in a Japanese
Coca-Cola commercial.[168]
Other artists that promoted Coca-Cola include David Bowie,[169] George Michael,[170] Elton John,[171]
and Whitney Houston,[172] who appeared in the Diet Coke commercial, among m any ot hers.In mass media
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca-Cola Move/Move
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
As sold in China
Astronauts served Coca-
Cola from this device on the
Space Shuttle in 1995.Not all musical references to Coca-Cola went well. A line in "Lola" by the Kinks was originally recorded
as "You drink champagne and it tastes just like Coca-Cola." When the British Broadcasting Corporation
refused to play the song because of the commercial reference, lead singer Ray Davies re-recorded the lyric
as "it tastes just like cherry cola" to get airplay for the song.[173][174]
Political cartoonist Michel Kichka satirized a famous Coca-Cola billboard in his 1982 poster "And I Love
New York." On the billboard, the Coca-Cola wave is accompanied by the words "Enjoy Coke." In
Kichka's poster, the lettering and script above  the Coca-Cola wave instead read "Enjoy C ocaine."[175]
Coca-Cola has a high degree of identification with
the United States, being considered by some an
"American Brand" or as an item representing
America, criticized as Cocacolonization. After
World War II, this gave rise to the brief produc tion
of White Coke by the request of and for Soviet
Marshal Georgy Zhukov , who did not want to be
seen drinking a symbol of American imperialism.
The bottles were given by the President
Eisenhow er during a conference, and Marshal
Zhukov enjoyed the drink. The bottles were
disguised as vodka  bottles, with the cap having a
red star design, to avoid suspicion of Soviet
officials.[176] The drink is also often a metonym  for
the Coca-Cola Company.
Coca-Cola was introduc ed to China in 1927, and
was very popul ar until 1949. After the Chinese
Civil War ended in 1949, the beverage was no longe r imported into China, as it
was perceived to be a symbol of decadent Western culture and capitalist lifestyle.
Importation and sales of the beverage resumed in 1979, after diplomatic relations
between the United States and C hina were restored.[177]
There are some consumer boyc otts of Coca-Cola in Arab countries due to Coke's early investment in Israel
during the Arab League boyc ott of Israel (its competitor Pepsi stayed out of Israel).[178] Mecca-Cola and
Pepsi are popul ar alternatives in the Middle East.[179]
A Coca-Cola fountain dispenser (officially a Fluids Generic Bioprocessing Apparatus or FGBA) was
developed for use on the Space Shuttle as a test bed to determine if carbona ted beverages can be produc ed
from separately stored carbon dioxide, water, and flavored syrups and determine if the resulting fluids can
be made available for consumption without bubbl e nucleation and resulting foam formation. FGBA-1 flew
on STS-63 in 1995 and dispensed pre-mixed beverages, followed by FGBA-2 on STS-77 the next year.
The latter mixed CO ₂ , water, and syrup to make beverages. It supplied 1.65 liters each of Coca-Cola and
Diet Coke.[180][181]
Coca-Cola is sometimes used for the treatment of gastric phytobezoars. In about 50% of cases studied,
Coca-Cola alone was found to be effective in gastric phytobezoar dissolution. This treatment can however
result in the potential of developing small bowel obstruction in a minority of cases, necessitating surgicalUse as political and corporate symbol
Medicinal application
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca-Cola Move/Move
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
intervention.[182][183]
Criticism of Coca-Cola has arisen from various groups around the world, concerning a variety of issues,
including health effects, environmental issues, and business practices. The drink's coca flavoring, and the
nickname "Coke", remain a common theme of criticism due to the relationship with the illegal drug
cocaine. In 1911, the US gove rnment seized 40 barrels and 20 kegs of Coca-Cola syrup in Chattanooga ,
Tennessee, alleging the caffeine in its drink was "injurious to health", leading to amended food safety
legislation.[184]
Beginning in the 1940s , PepsiCo started marketing their drinks to African Americans, a niche market that
was largely ignored by white-owned manufacturers in the US, and was able to use its anti-racism stance as
a selling point, attacking Coke's reluctance to hire blacks and suppor t by the chairman of the Coca-Cola
Company for segregationist Governor of Georgia Herman Talmadge.[185] As a result of this campaign,
PepsiCo's market share as compared to Coca-Cola's shot up dramatically in the 1950s  with African
American soft-drink consumers three times more likely to pur chase Pepsi over Coke.[186]
The Coca-Cola Company, its subsidiaries and produc ts have been subject to sustained criticism by
consumer groups , environmentalists, and watchdogs , particularly since the early 2000s .[187] In 2019,
BreakFreeFromPlastic named Coca-Cola the single biggest plastic polluter in the world. After 72,541
volunteers collected 476,423 pieces of plastic waste from around where they lived, a total of 11,732 pieces
were found to be labeled with a Coca-Cola brand (including the Dasani, Sprite, and Fanta brands) in 37
countries across four continents.[188] At the 2020 World Econom ic Forum in Davos, Coca-Cola's Head of
Sustainability, Bea Perez, said customers like them because they reseal and are lightweight, and "business
won't be in business if we don't accommodate consumers."[189] In February 2022, Coca-Cola announc ed
that it will aim to make 25 pe rcent of its packaging reusable by 2030.[190]
Coca-Cola Classic is rich in sugars, especially sucrose, which causes dental caries when consumed
regularly. Besides this, the high caloric value of the sugars themselves can contribute to obesity. Both are
major health issues in the developed world.[191]
In February 2021, Coca-Cola received criticism after a video of a training session, which told employees to
"try to be less white", was leaked by an employee. The session also said in order to be "less white"
employees had to be less "arrogant" and "defensive".[192][193]
In July 2001, the Coca-Cola Company was sued over its alleged use of far-right death squads (the United
Self-Defense Forces of Colombia) to kidnap, torture, and kill Colombian bottler workers that were linked
with trade union activity. Coca-Cola was sued in a US federal court in Miami by the Colombian food and
drink union Sinaltrainal. The suit alleged that Coca-Cola was indirectly responsible for having "contracted
with or otherwise directed paramilitary security forces that utilized extreme violence and murdered,
tortured, unlawfully detained or otherwise silenced trade union leaders". This sparked campaigns to boyc ott
Coca-Cola in the UK, US, Germany, Italy, and Australia.[194][195] Javier Correa, the president of
Sinaltrainal, said the campaign aimed to put pressure on Coca-Cola "to mitigate the pain and suffering" that
union m embers had suffered.[195]Criticism
Colombian death-squad allegations
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca-Cola Move/Move
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
Speaking from the Coca-Cola Company's headqua rters in Atlanta, company spoke sperson Rafael
Fernandez Quiros said "Coca-Cola denies any conne ction to any human-rights violation of this type" and
added "We do not  own or operate the plants".[196]
Food portal
Drink portal
United States
portal
Georgia (U.S.
state) portal
Coca-Cola HBC AG
Coca-Cola treatment of phytobezoars
Colalife
Fanta
List of Coca-Cola brandsList of soft drink flavors
Mexican Coke
Neiman Marcus
OpenCola (drink)
Premix and postmix
1. Elmore, 2013, p. 717
2. "Fortune 500 Companies 2018: Who Made the List" (http://fortune.com/fortune500/list/).
Fortune. Archived (https://web.archive.org/web/20181110190356/http://fortune.com/fortune5
00/list/) from the original on November 10, 2018. Retrieved November 10, 2018.
3. "2020 Best Global Brands - Interbrand" (https://www.interbrand.com/best-global-brands/).
Interbrand. Archived (https://web.archive.org/web/20220521191641/https://interbrand.com/b
est-global-brands/) from the original on May 21, 2022. Retrieved July 7, 2021.
4. Eschner, Kat (March 29, 2017). "Coca-Cola's Creator Said the Drink Would Make You
Smarter" (https://www.smithsonianmag.com/smart-news/coca-colas-creator-said-drink-would
-make-you-smarter-180962665/). Smithsonian Magazine. Smithsonian. Archived (https://we
b.archive.org/web/20190814233739/https://www.smithsonianmag.com/smart-news/coca-col
as-creator-said-drink-would-make-you-smarter-180962665/) from the original on August 14,
2019. Retrieved October 7, 2019. "So Pemberton concocted a recipe using coca leaves,
kola nuts and sugar syrup. "His new product debuted in 1886: 'Coca-Cola: The temperance
drink,'" writes Hamblin."
5. Greenwood, Veronique (September 23, 2016). "The little-known nut that gave Coca-Cola its
name" (https://www.bbc.com/future/article/20160922-the-nut-that-helped-to-build-a-global-e
mpire). www.bbc.com. Archived (https://web.archive.org/web/20200808215627/https://www.
bbc.com/future/article/20160922-the-nut-that-helped-to-build-a-global-empire) from the
original on August 8, 2020. Retrieved January 21, 2023.
6. Ivana Kottasova (February 18, 2014). "Does formula mystery help keep Coke afloat?" (http://
edition.cnn.com/2014/02/18/business/coca-cola-secret-formula/index.html). CNN. Archived
(https://web.archive.org/web/20220321170452/http://edition.cnn.com/2014/02/18/business/c
oca-cola-secret-formula/index.html) from the original on March 21, 2022. Retrieved
March 21, 2022.
7. Geuss, Megan (October 2010). "First Coupon Ever". Wired. Vol. 18, no. 11. p. 104.
8. Richard Gardiner, "The Civil War Origin of Coca-Cola in Columbus, Georgia," Muscogiana:
Journal of the Muscogee Genealogical Society (Spring 2012), Vol. 23: 21–24.See also
References
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca-Cola Move/Move
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
9. "Coca-Cola Inventor was Local Pharmacist" (http://files.usgwarchives.net/ga/muscogee/phot
os/pemberto13411gph.txt). Columbus Ledger. Archived (https://web.archive.org/web/201105
11115720/http://files.usgwarchives.net/ga/muscogee/photos/pemberto13411gph.txt) from
the original on May 11, 2011. Retrieved March 13, 2011.
10. "Columbus helped make Coke's success" (https://web.archive.org/web/20121110115355/htt
p://www.ledger-enquirer.com/2011/03/27/1514591/columbus-helped-make-cokes-success.ht
ml). Columbus Ledger-Enquirer. March 27, 2011. Archived from the original (http://www.ledg
er-enquirer.com/2011/03/27/1514591/columbus-helped-make-cokes-success.html) on
November 10, 2012. Retrieved August 12, 2012.
11. Patent Office, United States (1886). Annual Report of the Patent Office, 1885 (https://books.g
oogle.com/books?id=W4JGAQAAIAAJ&q=%22pemberton%2C+john+s.+atlanta%22+nerve
&pg=PA423). Archived (https://web.archive.org/web/20230423112322/https://books.google.c
om/books?id=W4JGAQAAIAAJ&q=%22pemberton%2C+john+s.+atlanta%22+nerve&pg=P
A423) from the original on April 23, 2023. Retrieved April 26, 2014.
12. "pemberton_1.jpg" (https://archive.today/20130908005438/http://facstaff.columbusstate.edu/
gardiner_Richard/columbus/John_Pemberton_files/pemberton_1.jpg). Archived from the
original (http://facstaff.columbusstate.edu/gardiner_Richard/columbus/John_Pemberton_file
s/pemberton_1.jpg) on September 8, 2013. Retrieved April 26, 2014 – via
columbusstate.edu.
13. Pendergrast, Mark (2000). For God, Country and Coca-Cola (https://archive.org/details/forgo
dcountrycoc00pend_0). Basic Books. p. 25 (https://archive.org/details/forgodcountrycoc00pe
nd_0/page/25). ISBN 978-0-465-05468-8.
14. Blanding, Michael (2010). The Coke machine : the dirty truth behind the world's favorite soft
drink (https://archive.org/details/cokemachinedirty00blan). New York: Avery. pp. 14 (https://ar
chive.org/details/cokemachinedirty00blan/page/n23). ISBN 9781583334065.
OCLC 535490831 (https://www.worldcat.org/oclc/535490831).
15. "Spanish town claims origins of Coca-Cola" (https://www.usatoday.com/story/news/world/20
13/08/10/newser-spanish-town-coca-cola/2638515/). USA Today. Archived (https://web.archi
ve.org/web/20200302212931/https://www.usatoday.com/story/news/world/2013/08/10/news
er-spanish-town-coca-cola/2638515/) from the original on March 2, 2020. Retrieved June 8,
2020.
16. Hayes, Jack. "Coca-Cola Television Advertisements: Dr. John S. Pemberton" (https://web.ar
chive.org/web/20070106000832/http://memory.loc.gov/ammem/ccmphtml/colainvnt.html).
Nation's Restaurant News. Archived from the original (http://memory.loc.gov/ammem/ccmpht
ml/colainvnt.html) on January 6, 2007. Retrieved January 21, 2007.
17. The Coca-Cola Company. "The Chronicle Of Coca-Cola" (https://web.archive.org/web/2013
0917012648/http://cocacolaweb.online.fr/chronicle/01.php). Archived from the original (http://
cocacolaweb.online.fr/chronicle/01.php) on September 17, 2013. Retrieved January 7, 2013.
18. Harford, Tim (May 11, 2007). "The Mystery of the 5-Cent Coca-Cola: Why it's so hard for
companies to raise prices" (https://web.archive.org/web/20070514033738/http://www.slate.c
om/id/2165787/). Slate. Archived from the original (http://www.slate.com/id/2165787/) on May
14, 2007. Retrieved May 12, 2007.
19. "Themes for Coca-Cola Advertising (1886–1999)" (https://web.archive.org/web/2007030307
0717/http://memory.loc.gov/ammem/ccmphtml/colatime1.html). Archived from the original (htt
p://memory.loc.gov/ammem/ccmphtml/colatime1.html) on March 3, 2007. Retrieved
February 11, 2007.
20. Pendergrast, Mark (2000). For God, Country and Coca-Cola (https://archive.org/details/forgo
dcountrycoc00pend_0). Basic Books. p. 32 (https://archive.org/details/forgodcountrycoc00pe
nd_0/page/32). ISBN 978-0-465-05468-8.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
21. Pendergrast, Mark (2000). For God, Country and Coca-Cola (https://archive.org/details/forgo
dcountrycoc00pend_0). Basic Books. p. 42 (https://archive.org/details/forgodcountrycoc00pe
nd_0/page/42). ISBN 978-0-465-05468-8.
22. Pendergrast, Mark (2000). For God, Country and Coca-Cola (https://archive.org/details/forgo
dcountrycoc00pend_0). Basic Books. pp. 45 (https://archive.org/details/forgodcountrycoc00p
end_0/page/45)–47. ISBN 978-0-465-05468-8.
23. Pendergrast, Mark (2000). For God, Country and Coca-Cola (https://archive.org/details/forgo
dcountrycoc00pend_0). Basic Books. p. 45 (https://archive.org/details/forgodcountrycoc00pe
nd_0/page/45). ISBN 978-0-465-05468-8.
24. Candler, Charles Howard (1950). Asa Griggs Candler. Georgia: Emory University. p. 81.
25. Pendergrast, Mark (2000). For God, Country and Coca-Cola (https://archive.org/details/forgo
dcountrycoc00pend_0). Basic Books. pp. 44 (https://archive.org/details/forgodcountrycoc00p
end_0/page/44)–45. ISBN 978-0-465-05468-8.
26. Pendergrast, Mark (2000). For God, Country and Coca-Cola (https://archive.org/details/forgo
dcountrycoc00pend_0). Basic Books. p. 49 (https://archive.org/details/forgodcountrycoc00pe
nd_0/page/49). ISBN 978-0-465-05468-8.
27. Pendergrast, Mark (2000). For God, Country and Coca-Cola (https://archive.org/details/forgo
dcountrycoc00pend_0). Basic Books. pp. 48 (https://archive.org/details/forgodcountrycoc00p
end_0/page/48)–49. ISBN 978-0-465-05468-8.
28. Pendergrast, Mark (2000). For God, Country and Coca-Cola (https://archive.org/details/forgo
dcountrycoc00pend_0). Basic Books. p. 46 (https://archive.org/details/forgodcountrycoc00pe
nd_0/page/46). ISBN 978-0-465-05468-8.
29. "This Day in Georgia History – Coca-Cola Sale Completed – GeorgiaInfo" (http://georgiainf
o.galileo.usg.edu/thisday/gahistory/09/12/coca-cola-sale-completed). usg.edu. Archived (htt
ps://web.archive.org/web/20161115081202/http://georgiainfo.galileo.usg.edu/thisday/gahist
ory/09/12/coca-cola-sale-completed) from the original on November 15, 2016. Retrieved
June 8, 2020.
30. "Robert W. Woodruff (1889–1985)" (http://www.georgiaencyclopedia.org/articles/business-e
conomy/robert-w-woodruff-1889-1985). New Georgia Encyclopedia. Archived (https://web.ar
chive.org/web/20190330195106/https://www.georgiaencyclopedia.org/articles/business-eco
nomy/robert-w-woodruff-1889-1985) from the original on March 30, 2019. Retrieved June 8,
2020.
31. Wood, Benjamin; Ruskin, Gary; Sacks, Gary (January 2020). "How Coca-Cola Shaped the
International Congress on Physical Activity and Public Health: An Analysis of Email
Exchanges between 2012 and 2014" (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC77303
22). International Journal of Environmental Research and Public Health. 17 (23): 8996.
doi:10.3390/ijerph17238996 (https://doi.org/10.3390%2Fijerph17238996). ISSN 1660-4601
(https://www.worldcat.org/issn/1660-4601). PMC 7730322 (https://www.ncbi.nlm.nih.gov/pm
c/articles/PMC7730322). PMID 33287097 (https://pubmed.ncbi.nlm.nih.gov/33287097).
32. "World of Coke exhibit shares story of forgotten 'Sprite Boy'" (https://www.ajc.com/blog/talk-t
own/world-coke-exhibit-shares-story-forgotten-sprite-boy/soMnt1rHQd9j5JxpyZeuML/).
Archived (https://web.archive.org/web/20230402005821/https://www.ajc.com/blog/talk-town/
world-coke-exhibit-shares-story-forgotten-sprite-boy/soMnt1rHQd9j5JxpyZeuML/) from the
original on April 2, 2023. Retrieved April 2, 2023.
33. "Coca-Cola Enterprises : Our Story" (https://archive.today/20150417095329/http://www.coke
cce.com/about-cce/our-story). Coca-Cola Enterprises. Archived from the original (http://www.
cokecce.com/about-cce/our-story) on April 17, 2015.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
34. The Coca-Cola Company. "History of Bottling" (http://www.coca-colacompany.com/our-comp
any/history-of-bottling). Archived (https://web.archive.org/web/20130116234350/http://www.c
oca-colacompany.com/our-company/history-of-bottling) from the original on January 16,
2013. Retrieved March 12, 2018.
35. "Mar 12, 1894 CE: First Bottles of Coca-Cola" (https://www.nationalgeographic.org/thisday/
mar12/first-bottles-coca-cola/). National Geographic Society. December 17, 2013. Archived
(https://web.archive.org/web/20160604175453/https://www.nationalgeographic.org/thisday/
mar12/first-bottles-coca-cola/) from the original on June 4, 2016. Retrieved March 12, 2019.
36. "Coca-Cola History" (https://www.worldofcoca-cola.com/about-us/coca-cola-history).
worldofcoca-cola.com. Archived (https://web.archive.org/web/20160407225546/http://www.w
orldofcoca-cola.com/about-us/coca-cola-history/) from the original on April 7, 2016.
Retrieved June 8, 2020.
37. "Chattanooga Coca-Cola History" (http://cocacolaunited.com/wp-content/uploads/2012/03/H
ISTORY-OF-CHATTANOOGA-COCA-COLA-WORLDS-FIRST-BOTTLING-COMPANY.pdf)
(PDF). Archived (https://web.archive.org/web/20140201213538/http://cocacolaunited.com/w
p-content/uploads/2012/03/HISTORY-OF-CHATTANOOGA-COCA-COLA-WORLDS-FIRST
-BOTTLING-COMPANY.pdf) (PDF) from the original on February 1, 2014. Retrieved
August 24, 2008.
38. "History Of Bottling" (https://web.archive.org/web/20130116234350/http://www.coca-colaco
mpany.com/our-company/history-of-bottling). Archived from the original (http://www.coca-col
acompany.com/our-company/history-of-bottling) on January 16, 2013. Retrieved January 7,
2013.
39. First painted wall sign to advertise Coca-Cola : Cartersville, GA (http://www.waymarking.co
m/waymarks/WM2DK6) Archived (https://web.archive.org/web/20100324232658/http://www.
waymarking.com/waymarks/WM2DK6) March 24, 2010, at the Wayback Machine –
Waymarking
40. Staff, The Doctors Book of Home Remedies. Nausea: 10 Stomach-Soothing Solutions (htt
p://www.guidetohealth.com/library/the-doctors-book-of-home-remedies/nausea/) Archived (ht
tps://web.archive.org/web/20130524174753/http://www.guidetohealth.com/library/the-doctor
s-book-of-home-remedies/nausea/) May 24, 2013, at the Wayback Machine
41. Example: Flent's Cola Syrup (https://web.archive.org/web/20110224015437/http://www.drug
store.com/flents-cola-syrup/qxp80274) Label says "For Simple Nausea associated with an
upset stomach.* *These statements have not been evaluated by the Food and Drug
Administration. This product is not intended to diagnose, treat, cure, or prevent any disease."
42. "Atlanta Jews and Coca-Cola" (https://www.bh.org.il/atlanta-jews-and-coca-cola/). Archived
(https://web.archive.org/web/20180821062611/https://www.bh.org.il/atlanta-jews-and-coca-c
ola/) from the original on August 21, 2018. Retrieved June 8, 2020.
43. "Beyond Seltzer Water: The Kashering of Coca-Cola" (http://www.ajhs.org/scholarship/chapt
ers/chapter.cfm?documentID=270). American Jewish Historical Society. Archived (https://we
b.archive.org/web/20100917045652/http://www.ajhs.org/scholarship/chapters/chapter.cfm?d
ocumentID=270) from the original on September 17, 2010. Retrieved February 26, 2007.
44. "Fleeman's Pharmacy (now the Belly General Store)" (http://www.bellystore.com/BELLYSTO
RE/history.htm). Archived (https://web.archive.org/web/20031217184412/http://www.bellystor
e.com/BELLYSTORE/history.htm) from the original on December 17, 2003.
45. "Jack Fleeman – 86 – Owner" (https://www.ajc.com/news/local/jack-fleeman-owner-landmar
k-drugstore/BXly9zmIFesfhJRMYnt0qM/). Atlanta Journal-Constitution. Georgia. August 17,
2009. Archived (https://web.archive.org/web/20121110115403/http://www.ajc.com/news/jack
-fleeman-86-owner-117848.html) from the original on November 10, 2012.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
46. "Coke Can History" (https://archive.today/20120530045557/http://home.comcast.net/~collect
iblesodacans/Cokepg1.htm). Archived from the original (http://home.comcast.net/~collectible
sodacans/Cokepg1.htm) on May 30, 2012.
47. "A History of Sugar Prices" (https://www.winton.com/longer-view/the-sweet-and-sour-history-
of-sugar-prices). Archived (https://web.archive.org/web/20220901083635/https://www.winto
n.com/longer-view/the-sweet-and-sour-history-of-sugar-prices) from the original on
September 1, 2022. Retrieved September 2, 2022.
48. Ennis, Thomas W. (January 5, 1972). "Sugar Futures up on Soviet Buying" (https://www.nyti
mes.com/1972/01/05/archives/sugar-futures-up-on-soviet-buying-purchases-on-world-marke
t-said-to.html). The New York Times. Archived (https://web.archive.org/web/2022090108363
8/https://www.nytimes.com/1972/01/05/archives/sugar-futures-up-on-soviet-buying-purchase
s-on-world-market-said-to.html) from the original on September 1, 2022. Retrieved
September 2, 2022.
49. "New Coke – Top 10 Bad Beverage Ideas" (http://content.time.com/time/specials/packages/a
rticle/0,28804,1913612_1913610_1913608,00.html). Time.com. April 23, 2010. Archived (htt
ps://web.archive.org/web/20191121111728/http://content.time.com/time/specials/packages/a
rticle/0,28804,1913612_1913610_1913608,00.html) from the original on November 21,
2019. Retrieved June 8, 2020.
50. Rory Carroll in Baghdad (July 5, 2005). "Cola wars as Coke moves on Baghdad" (https://ww
w.theguardian.com/world/2005/jul/05/iraq.rorycarroll). The Guardian. London. Archived (http
s://web.archive.org/web/20180621193954/https://www.theguardian.com/world/2005/jul/05/ir
aq.rorycarroll) from the original on June 21, 2018. Retrieved March 13, 2011.
51. McKay, Betsy (January 30, 2009). "Coke to Omit 'Classic'" (https://www.wsj.com/articles/SB
123332768434033495). The Wall Street Journal. Archived (https://web.archive.org/web/202
00521052905/https://www.wsj.com/articles/SB123332768434033495) from the original on
May 21, 2020. Retrieved June 8, 2020.
52. Klinemann, Jeffrey (January 31, 2013). "PepsiCo's in the Club... Store, that is, Capturing
Costco Food Service Account" (http://www.bevnet.com/news/2013/pepsicos-in-the-club-stor
e-that-is-capturing-costco-food-service-account). BevNET. Archived (https://web.archive.org/
web/20150320120650/http://www.bevnet.com/news/2013/pepsicos-in-the-club-store-that-is-
capturing-costco-food-service-account) from the original on March 20, 2015. Retrieved
April 25, 2015.
53. Fredrix, Emily and Sarah Skidmore (November 17, 2009). "Costco nixes Coke products over
pricing dispute" (https://archive.today/20091120184311/http://www.google.com/hostednews/
ap/article/ALeqM5hC_n50ZLyl8FLDBIkGfCn7-110BwD9C1F1C80). Associated Press.
Archived from the original (https://www.google.com/hostednews/ap/article/ALeqM5hC_n50Z
Lyl8FLDBIkGfCn7-110BwD9C1F1C80) on November 20, 2009.
54. Esterl, Mike (September 19, 2011). "Coke Tailors Its Soda Sizes" (https://www.wsj.com/articl
es/SB10001424053111903374004576578980270401662). The Wall Street Journal.
ISSN 0099-9660 (https://www.worldcat.org/issn/0099-9660). Archived (https://web.archive.or
g/web/20191219171247/https://www.wsj.com/articles/SB100014240531119033740045765
78980270401662) from the original on December 19, 2019. Retrieved December 19, 2019.
55. "Coca-Cola returns to Burma after a 60-year absence" (https://www.bbc.co.uk/news/busines
s-18453401). BBC News. June 14, 2012. Archived (https://web.archive.org/web/201810222
33834/https://www.bbc.co.uk/news/business-18453401) from the original on October 22,
2018. Retrieved June 8, 2020.
56. Jordan, Tony (June 14, 2012). "Coca-Cola Announces Will Return to Myanmar After 60
Years" (https://www.bloomberg.com/news/2012-06-15/coca-cola-announces-will-return-to-m
yanmar-after-60-years.html). Bloomberg. Archived (https://web.archive.org/web/2014121101
4652/http://www.bloomberg.com/news/2012-06-15/coca-cola-announces-will-return-to-myan
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
yanmar-after-60-years.html). Bloomberg. Archived (https://web.archive.org/web/2014121101
4652/http://www.bloomberg.com/news/2012-06-15/coca-cola-announces-will-return-to-myan
mar-after-60-years.html) from the original on December 11, 2014. Retrieved June 8, 2020.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
57. Calderon, Justin (June 4, 2013). "Coca-Cola starts bottling in Myanmar" (http://investvine.co
m/coca-cola-starts-bottling-in-myanmar/). Inside Investor. Archived (https://web.archive.org/w
eb/20130918184353/http://investvine.com/coca-cola-starts-bottling-in-myanmar/) from the
original on September 18, 2013. Retrieved June 5, 2013.
58. "Coca-Cola to invest Rs 28,000 cr in India" (http://www.indianexpress.com/news/coca-cola-t
o-invest-rs-28-000-cr-in-india/966950/). June 26, 2012. Archived (https://web.archive.org/we
b/20130917151332/http://www.indianexpress.com/news/coca-cola-to-invest-rs-28-000-cr-in-
india/966950/) from the original on September 17, 2013. Retrieved June 8, 2020.
59. Reuters Staff (February 9, 2021). "Coca-Cola turns to 100% recycled plastic bottles in U.S."
(https://www.reuters.com/article/us-environment-plastic-coca-cola-idUSKBN2A921L)
Reuters. Archived (https://web.archive.org/web/20220207101346/https://www.reuters.com/ar
ticle/us-environment-plastic-coca-cola-idUSKBN2A921L) from the original on February 7,
2022. Retrieved February 9, 2021. {{cite news}}: |author= has generic name (help)
60. "Coca-Cola company trials first paper bottle" (https://www.bbc.com/news/technology-560237
23). BBC News. February 12, 2021. Archived (https://web.archive.org/web/2022071010114
5/https://www.bbc.com/news/technology-56023723) from the original on July 10, 2022.
Retrieved February 12, 2021.
61. "Home of Coca-Cola UK : Diet Coke : Coke Zero – Coca-Cola GB" (https://web.archive.org/
web/20100515103118/http://www.letsgettogether.co.uk/DetailQuestionAnswer/QuestionID%
3D2-color%3Ddf0f0b). Letsgettogether.co.uk. April 13, 2010. Archived from the original (htt
p://www.letsgettogether.co.uk/DetailQuestionAnswer/QuestionID=2-color=df0f0b) on May
15, 2010. Retrieved March 13, 2011.
62. "Foods List" (https://web.archive.org/web/20181119223520/https://ndb.nal.usda.gov/ndb/sea
rch/list?qlookup=14400). usda.gov. Archived from the original (https://ndb.nal.usda.gov/ndb/
search/list?qlookup=14400) on November 19, 2018. Retrieved June 8, 2020.
63. "The Daily Plate" (http://www.thedailyplate.com/nutrition-calories/food/coca-cola/coca-cola-c
lassic-12 oz-can). The Daily Plate. Retrieved March 13, 2011.
64. "Coke, Pepsi to Drop Controversial Chemical from All Drinks" (https://www.nbcnews.com/bu
siness/consumer/coke-pepsi-drop-controversial-chemical-all-drinks-n97016). NBC News.
Archived (https://web.archive.org/web/20200515003548/https://www.nbcnews.com/busines
s/consumer/coke-pepsi-drop-controversial-chemical-all-drinks-n97016) from the original on
May 15, 2020. Retrieved June 8, 2020.
65. "Coca-Cola formula, after 86 years in vault, gets new home" (http://www.csmonitor.com/Busi
ness/Latest-News-Wires/2011/1208/Coca-Cola-formula-after-86-years-in-vault-gets-new-ho
me). The Christian Science Monitor. December 8, 2011. Archived (https://web.archive.org/w
eb/20200124075036/https://www.csmonitor.com/Business/Latest-News-Wires/2011/1208/C
oca-Cola-formula-after-86-years-in-vault-gets-new-home) from the original on January 24,
2020. Retrieved June 8, 2020.
66. "Urban Legends Reference Pages: Cokelore" (https://wayback.archive-it.org/all/200812180
31122/http://www.snopes.com/cokelore/). Archived from the original (http://www.snopes.com/
cokelore/) on December 18, 2008. Retrieved February 10, 2007.
67. "Urban Legends Reference Pages: Cokelore (Have a Cloak and a Smile)" (http://www.snop
es.com/cokelore/formula.asp). November 18, 1999. Archived (https://wayback.archive-it.org/
all/20051201022606/http://www.snopes.com/cokelore/formula.asp) from the original on
December 1, 2005. Retrieved February 22, 2007.
68. Katie Rogers, "'This American Life' bursts Coca-Cola's bubble: What's in that original recipe,
anyway?," (http://voices.washingtonpost.com/blog-post/2011/02/this_american_life_bursts_
coca.html) Archived (https://web.archive.org/web/20120609050804/http://voices.washington
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
anyway?," (http://voices.washingtonpost.com/blog-post/2011/02/this_american_life_bursts_
coca.html) Archived (https://web.archive.org/web/20120609050804/http://voices.washington
post.com/blog-post/2011/02/this_american_life_bursts_coca.html) June 9, 2012, at the
Wayback Machine The Washington Post BlogPost, February 15, 2011. Retrieved February
16, 2011.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
69. Brett Michael Dykes, "Did NPR's 'This American Life' discover Coke's secret formula?," (http
s://news.yahoo.com/s/yblog_thelookout/20110215/ts_yblog_thelookout/did-nprs-this-americ
an-life-discover-cokes-secret-formula) Archived (https://web.archive.org/web/201102172321
18/http://news.yahoo.com/s/yblog_thelookout/20110215/ts_yblog_thelookout/did-nprs-this-a
merican-life-discover-cokes-secret-formula) February 17, 2011, at the Wayback Machine
The Lookout, Yahoo! News, February 15, 2011.
70. David W. Freeman, "'This American Life' Reveals Coca-Cola's Secret Recipe (Full
Ingredient List)," (http://www.cbsnews.com/8301-504763_162-20031984-10391704.html)
Archived (https://web.archive.org/web/20110218030813/http://www.cbsnews.com/8301-504
763_162-20031984-10391704.html) February 18, 2011, at the Wayback Machine CBS
News Healthwatch blogs, February 15, 2011.
71. The Recipe (http://www.thisamericanlife.org/radio-archives/episode/427/original-recipe/recip
e) Archived (https://web.archive.org/web/20110217180930/http://www.thisamericanlife.org/ra
dio-archives/episode/427/original-recipe/recipe) February 17, 2011, at the Wayback
Machine, This American Life.
72. "Coca-cola" (https://web.archive.org/web/20091115102804/http://www.pponline.co.uk/ency
c/0204.htm). Pponline.co.uk. Archived from the original (http://www.pponline.co.uk/encyc/02
04.htm) on November 15, 2009. Retrieved March 13, 2011.
73. "The History of Coca-Cola" (http://inventors.about.com/od/cstartinventions/a/coca_cola.htm).
Archived (https://wayback.archive-it.org/all/20090315195846/http://inventors.about.com/od/c
startinventions/a/coca_cola.htm) from the original on March 15, 2009. Retrieved January 23,
2007.
74. "Cocaine Facts - How to Tell Use of Cocaine - Questions, Myths, Truth" (http://www.thegood
drugsguide.com/cocaine/faq.htm). thegooddrugsguide.com. Archived (https://web.archive.or
g/web/20081006104725/http://www.thegooddrugsguide.com/cocaine/faq.htm) from the
original on October 6, 2008. Retrieved June 8, 2020.
75. Liebowitz, Michael, R. (1983). The Chemistry of Love. Boston: Little, Brown, & Co.
76. "Is it true Coca-Cola once contained cocaine?" (https://web.archive.org/web/200702211149
07/http://www.straightdope.com/classics/a2_033.html). June 14, 1985. Archived from the
original (http://www.straightdope.com/classics/a2_033.html) on February 21, 2007.
Retrieved February 27, 2007.
77. "Coca-Cola's Scandalous Past" (https://archives.drugabuse.gov/blog/post/coca-colas-scand
alous-past). March 2012. Archived (https://web.archive.org/web/20220524130758/http://archi
ves.drugabuse.gov/) from the original on May 24, 2022. Retrieved March 29, 2022.
78. May, Clifford D. (July 1, 1988). "How Coca-Cola Obtains Its Coca" (https://www.nytimes.com/
1988/07/01/business/how-coca-cola-obtains-its-coca.html). The New York Times. Archived
(https://web.archive.org/web/20190420232528/https://www.nytimes.com/1988/07/01/busines
s/how-coca-cola-obtains-its-coca.html) from the original on April 20, 2019. Retrieved
April 11, 2008. "A Stepan laboratory in Maywood, N.J., is the nation's only legal commercial
importer of coca leaves, which it obtains mainly from Peru and, to a lesser extent, Bolivia.
Besides producing the coca flavoring agent sold to The Coca-Cola Company, Stepan
extracts cocaine from the coca leaves, which it sells to Mallinckrodt Inc., a St. Louis
pharmaceutical manufacturer that is the only company in the United States licensed to purify
the product for medicinal use"
79. Benson, Drew. "Coca kick in drinks spurs export fears" (https://archive.today/201205300456
00/http://www.mindfully.org/Food/2004/Kdrink-Coca-Drink19apr04.htm). Archived from the
original (http://www.mindfully.org/Food/2004/Kdrink-Coca-Drink19apr04.htm) on May 30,
2012.
80. "Dope Wagons" (http://ncpedia.org/dope-wagons). ncpedia.org. Archived (https://web.archiv
e.org/web/20200202113220/https://ncpedia.org/dope-wagons) from the original on February
2, 2020. Retrieved June 8, 2020.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
81. Text of United States v. Forty Barrels & Twenty Kegs of Coca-Cola, 241 U.S. 265 (1916) is
available from: CourtListener (https://www.courtlistener.com/opinion/98742/united-states-v-c
oca-cola-co-of-atlanta/)  Findlaw (https://caselaw.findlaw.com/us-supreme-court/241/265.htm
l)  Justia (https://supreme.justia.com/cases/federal/us/241/265/)  Library of Congress (http://c
dn.loc.gov/service/ll/usrep/usrep241/usrep241265/usrep241265.pdf)
82. Gene A. Spiller (1998). Caffeine Content of Some Cola Beverages (https://books.google.co
m/books?id=WxmBmvhsoZ8C&q=caffeine+coca+cola&pg=PA363). CRC. ISBN 978-0-
8493-2647-9. Archived (https://web.archive.org/web/20230423112347/https://books.google.c
om/books?id=WxmBmvhsoZ8C&q=caffeine+coca+cola&pg=PA363) from the original on
April 23, 2023. Retrieved October 17, 2020.
83. "Offices & Bottling Plants" (https://web.archive.org/web/20070216144908/http://www.thecoc
a-colacompany.com/ourcompany/aboutbottling.html). Archived from the original (http://www.t
hecoca-colacompany.com/ourcompany/aboutbottling.html) on February 16, 2007. Retrieved
January 7, 2013.
84. "What Is the Difference Between Coca-Cola Enterprises and the Coca-Cola Company" (http
s://web.archive.org/web/20121021100615/http://cokecce.com/pages/allContent.asp?page_i
d=84). Archived from the original (http://www.cokecce.com/pages/allContent.asp?page_id=8
4#q1) on October 21, 2012. Retrieved December 9, 2014.
85. "Coca-Cola: Macedonia makes the best Coke" (https://web.archive.org/web/201105111121
11/http://macedoniaonline.eu/content/view/7151/1/). Macedoniaonline.eu. June 16, 2009.
Archived from the original (http://macedoniaonline.eu/content/view/7151/1/) on May 11,
2011. Retrieved March 13, 2011.
86. Stafford, Leon (September 9, 2012). "Coca-Cola to spend $30 billion to grow globally" (http
s://www.ajc.com/business/coca-cola-spend-billion-grow-globally/w9gISxxV0dkJOQAZrnUO
dM/). The Atlanta Journal-Constitution. Archived (https://web.archive.org/web/202203211810
35/https://www.ajc.com/business/coca-cola-spend-billion-grow-globally/w9gISxxV0dkJOQA
ZrnUOdM/) from the original on March 21, 2022. Retrieved June 8, 2021.
87. Weissert, Will (May 15, 2007). "Cuba stocks US brands despite embargo" (http://usatoday3
0.usatoday.com/money/economy/2007-05-14-1080210184_x.htm). USA Today. Associated
Press. Archived (https://web.archive.org/web/20160313015718/http://usatoday30.usatoday.c
om/money/economy/2007-05-14-1080210184_x.htm) from the original on March 13, 2016.
Retrieved August 11, 2013.
88. Ryall, Julian (August 31, 2012). "Coca-Cola denies 'cracking' North Korea" (https://www.tele
graph.co.uk/news/worldnews/asia/northkorea/9511235/Coca-Cola-denies-cracking-North-K
orea.html). The Telegraph. London. Archived (https://web.archive.org/web/20130906214111/
http://www.telegraph.co.uk/news/worldnews/asia/northkorea/9511235/Coca-Cola-denies-cra
cking-North-Korea.html) from the original on September 6, 2013. Retrieved August 11, 2013.
89. Liebesny, Herbert J. (1975). The law of the Near and Middle East readings, cases, and
materials (https://archive.org/details/lawofnearmiddlee0000lieb). Albany: State University of
New York Press. pp. 42 (https://archive.org/details/lawofnearmiddlee0000lieb/page/42)–43.
ISBN 9780585090207.
90. "Transliteration of 'Coca-Cola' Trademark to Chinese Characters" (http://atisaustralia.weebly.
com/1/post/2015/08/transliteration-of-coca-cola-trademark-to-chinese-characters.html). ATIS
- Australian Translating and Interpreting Service. Archived (https://web.archive.org/web/2022
0522081707/https://atisaustralia.weebly.com/atis-blog/transliteration-of-coca-cola-trademark
-to-chinese-characters) from the original on May 22, 2022. Retrieved June 30, 2022.
91. "Coca-Cola in Chinese is Ke-kou-ke-la" (https://economictimes.indiatimes.com/business-jok
es/coca-cola-in-chinese-is-ke-kou-ke-la/articleshow/623585.cms). The Economic Times.
Archived (https://web.archive.org/web/20220630095421/https://economictimes.indiatimes.co
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
es/coca-cola-in-chinese-is-ke-kou-ke-la/articleshow/623585.cms). The Economic Times.
Archived (https://web.archive.org/web/20220630095421/https://economictimes.indiatimes.co
m/business-jokes/coca-cola-in-chinese-is-ke-kou-ke-la/articleshow/623585.cms) from the
original on June 30, 2022. Retrieved June 30, 2022.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
92. "可⼝可乐 "—— 中翻译的经典作  (https://web.archive.org/web/20180918160536/https://w
ww.coca-cola.com.cn/stories/kkklzwfydjdzz). Archived from the original (https://www.coca-co
la.com.cn/stories/kkklzwfydjdzz) on September 18, 2018. Retrieved September 18, 2018.
93. 明仁「可⼝可」中翻  (https://www.thinkhk.com/article/2021-01/11/4628
0.html). www.thinkhk.com. Archived (https://web.archive.org/web/20210115205723/https://w
ww.thinkhk.com/article/2021-01/11/46280.html) from the original on January 15, 2021.
Retrieved June 30, 2022.
94. ""Placing the history of advertising": A spatial history of advertising in modern Shanghai
(1905-1949)" (https://purl.stanford.edu/vr090fm8620). purl.stanford.edu. Archived (https://we
b.archive.org/web/20220714012804/https://purl.stanford.edu/vr090fm8620) from the original
on July 14, 2022. Retrieved June 30, 2022.
95. Huddleston, Tom Jr. (July 5, 2019). "Netflix's 'Stranger Things' revives New Coke. Here's
how the failed soda cost Coca-Cola millions in 1985" (https://www.cnbc.com/2019/07/05/netf
lix-stranger-things-revives-new-coke-heres-how-the-failed-soda-cost-coca-cola-millions.htm
l). CNBC. Archived (https://web.archive.org/web/20190708061804/https://www.cnbc.com/20
19/07/05/netflix-stranger-things-revives-new-coke-heres-how-the-failed-soda-cost-coca-cola
-millions.html) from the original on July 8, 2019. Retrieved July 8, 2019.
96. Meyer, Zlati (February 8, 2019). "Coca-Cola debuts Orange Vanilla, its first new flavor in
more than a decade" (https://www.usatoday.com/story/money/2019/02/08/coca-cola-orange-
vanilla-soda-giants-first-new-flavor-decade/2813256002/). USA Today. Archived (https://we
b.archive.org/web/20200226011250/https://www.usatoday.com/story/money/2019/02/08/coc
a-cola-orange-vanilla-soda-giants-first-new-flavor-decade/2813256002/) from the original on
February 26, 2020. Retrieved June 8, 2020.
97. "Coca-Cola Great Britain announces the launch of Coca-Cola Energy" (https://www.coca-col
a.co.uk/newsroom/press-releases/Coca-Cola-energy-launch). Archived (https://web.archive.
org/web/20190526165146/https://www.coca-cola.co.uk/newsroom/press-releases/Coca-Col
a-energy-launch) from the original on May 26, 2019.
98. Wienner-Bronner, Danielle (October 1, 2019). "Coca-Cola Energy is coming to the United
States" (https://www.cnn.com/2019/10/01/business/coke-energy-us-launch/index.html).
CNN.com. Archived (https://web.archive.org/web/20191224201839/https://www.cnn.com/20
19/10/01/business/coke-energy-us-launch/index.html) from the original on December 24,
2019. Retrieved June 8, 2020.
99. "Coca-Cola discontinues energy drink in N.America" (https://www.reuters.com/business/retai
l-consumer/coca-cola-discontinues-energy-drink-namerica-2021-05-14/). Reuters. May 14,
2021. Archived (https://web.archive.org/web/20220321181035/https://www.reuters.com/busi
ness/retail-consumer/coca-cola-discontinues-energy-drink-namerica-2021-05-14/) from the
original on March 21, 2022. Retrieved May 15, 2021.
100. Moye, Jay (September 30, 2019). "Priming the Innovation Pump: Coca-Cola Debuts Diverse
Lineup of New Drinks at NACS" (https://www.coca-colacompany.com/stories/priming-the-inn
ovation-pump-coca-cola-debuts-diverse-lineup). The Coca-Cola Company. Archived (https://
web.archive.org/web/20191003061646/https://www.coca-colacompany.com/stories/priming-t
he-innovation-pump-coca-cola-debuts-diverse-lineup) from the original on October 3, 2019.
Retrieved June 8, 2020.
101. "Coca-Cola Company – Red Spencerian Script" (http://inventors.about.com/od/advertisingm
edia/ss/Coca_Cola_Comp_2.htm). Archived (https://wayback.archive-it.org/all/20090315204
551/http://inventors.about.com/od/advertisingmedia/ss/Coca_Cola_Comp_2.htm) from the
original on March 15, 2009. Retrieved January 11, 2007.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
102. "The 130-year Evolution of the Coca-Cola logo" (https://www.coca-colajourney.com.au/storie
s/trace-the-130-year-evolution-of-the-coca-cola-logo). The Coca-Cola Company. Archived (h
ttps://web.archive.org/web/20180723182155/https://www.coca-colajourney.com.au/stories/tr
ace-the-130-year-evolution-of-the-coca-cola-logo) from the original on July 23, 2018.
Retrieved July 23, 2018.
103. "Frank Robinson, creator of the Coca-Cola logo" (http://coca-cola-art.com/2008/06/05/frank-r
obinson/). June 5, 2008. Archived (https://web.archive.org/web/20090127042828/http://coca-
cola-art.com/2008/06/05/frank-robinson/) from the original on January 27, 2009. Retrieved
December 15, 2008.
104. Kamdar, Ismail (March 23, 2011). "Of Wa-Hubbies and Conspiracies" (http://muslimmatters.o
rg/2011/03/23/of-wa-hubbies-and-conspiracies/). Muslim Matters. Archived (https://web.archi
ve.org/web/20200121031852/https://muslimmatters.org/2011/03/23/of-wa-hubbies-and-cons
piracies/) from the original on January 21, 2020. Retrieved June 8, 2020.
105. "Inventory: Earl R. Dean Collection" (http://www.vigo.lib.in.us/archives/inventories/business/
dean.php). Vigo County Public Library. Archived (https://web.archive.org/web/20110608214
022/http://www.vigo.lib.in.us/archives/inventories/business/dean.php) from the original on
June 8, 2011. Retrieved December 14, 2008.
106. "The Story of the Coca-Cola Bottle" (http://www.coca-colacompany.com/stories/the-story-of-t
he-coca-cola-bottle). Coca-Cola. February 26, 2015. Archived (https://web.archive.org/web/2
0171119092136/http://www.coca-colacompany.com/stories/the-story-of-the-coca-cola-bottle)
from the original on November 19, 2017. Retrieved November 20, 2017.
107. "The Contour Bottle Celebrates Its 100th Birthday!" (https://ccbanet.com/wp-content/uploads/
2015/04/TBL_Spring-Summer_324.pdf) (PDF). Coca-Cola Bottlers Association. 2015.
Archived (https://web.archive.org/web/20190412085853/https://ccbanet.com/wp-content/upl
oads/2015/04/TBL_Spring-Summer_324.pdf) (PDF) from the original on April 12, 2019.
Retrieved November 20, 2017.
108. Pendergrast, Mark (2004). For God, Country, and Coca-Cola (https://books.google.com/book
s?id=bSAChoqpnHUC&q=harold+hirsch). Basic Books. p. 104. ISBN 9780684826790.
Archived (https://web.archive.org/web/20191227142753/https://books.google.com/books?id
=bSAChoqpnHUC&q=harold+hirsch#v=snippet&q=harold%20hirsch) from the original on
December 27, 2019. Retrieved June 8, 2020.
109. Donna Gisolo Christenberry (2011). Terre Haute: Farrington's Grove (https://books.google.co
m/books?id=PN2HOJFxWRsC&pg=PA65). Arcadia Publishing. p. 65. ISBN 978-0-7385-
8319-8. Archived (https://web.archive.org/web/20191223061941/https://books.google.com/b
ooks?id=PN2HOJFxWRsC&pg=PA65) from the original on December 23, 2019. Retrieved
June 8, 2020.
110. "The History Behind the Coca-Cola Bottle" (https://www.coca-colacompany.com/stories/the-
story-of-the-coca-cola-bottle). The Coca-Cola Company. Archived (https://web.archive.org/w
eb/20190819164556/https://www.coca-colacompany.com/stories/the-story-of-the-coca-cola-
bottle) from the original on August 19, 2019. Retrieved October 20, 2019. "When King and
Family sized packaging were introduced in 1955, Raymond Loewy was part of the team that
worked to recast the bottle but still keep the proper proportions."
111. "Snopes urban legend of the Coca-Cola bottle shape" (http://www.snopes.com/cokelore/bottl
e.asp). Snopes.com. May 2, 1999. Archived (https://web.archive.org/web/20220118171338/h
ttps://www.snopes.com/fact-check/coke-bottle-design-accident/) from the original on January
18, 2022. Retrieved March 13, 2011.
112. Friedman, Lawrence M. (2004). American Law in the 20th Century (https://books.google.co
m/books?id=0kZNwJZxRr0C&pg=PA356). New Haven: Yale University Press. pp. 356–357.
ISBN 9780300102994. Archived (https://web.archive.org/web/20230423112323/https://book
s.google.com/books?id=0kZNwJZxRr0C&pg=PA356) from the original on April 23, 2023.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
ISBN 9780300102994. Archived (https://web.archive.org/web/20230423112323/https://book
s.google.com/books?id=0kZNwJZxRr0C&pg=PA356) from the original on April 23, 2023.
Retrieved December 11, 2021.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
113. O'Connell, Jeffrey; Linehan, John (2006). Carrington, Paul D.; Jones, Trina (eds.). "The Rise
and Fall (and Rise Again?) of Accident Law: A Continuing Saga" (https://books.google.com/b
ooks?id=dMMqAmkAyyYC&pg=PA353). Law and Class in America: Trends Since the Cold
War. New York: New York University Press: 349–363. ISBN 9780814716540. Retrieved
February 12, 2017.
114. Feinman, Jay M. (2014). Law 101 (https://books.google.com/books?id=7WfrAwAAQBAJ&pg
=PA166) (4th ed.). Oxford: Oxford University Press. p. 166. ISBN 9780199341696.
115. Vandall, Frank J. (2011). A History of Civil Litigation: Political and Economic Perspectives (h
ttps://books.google.com/books?id=vw9pAgAAQBAJ&pg=PA27). Oxford: Oxford University
Press. p. 27. ISBN 9780199781096.
116. Goldberg, John C.P.; Sebok, Anthony J.; Zipursky, Benjamin C.; Kendrick, Leslie C. (2021).
Tort Law: Responsibilities and Redress (https://books.google.com/books?id=U9UeEAAAQB
AJ&pg=PA981) (5th ed.). New York: Wolters Kluwer. p. 981. ISBN 9781543821086.
Archived (https://web.archive.org/web/20230423112924/https://books.google.com/books?id
=U9UeEAAAQBAJ&pg=PA981) from the original on April 23, 2023. Retrieved December 11,
2021.
117. Torrisi, Lauren (April 13, 2013). "Couture Coke Bottles Inspired by Madonna" (https://abcnew
s.go.com/blogs/lifestyle/2012/04/couture-coke-bottles-inspired-by-madonna). ABC News.
Archived (https://web.archive.org/web/20200323022520/https://abcnews.go.com/blogs/lifest
yle/2012/04/couture-coke-bottles-inspired-by-madonna) from the original on March 23, 2020.
Retrieved March 22, 2020.
118. "Coca-Cola Light Gets Dressed By Another Designer, Karl Lagerfeld" (http://ifitshipitshere.bl
ogspot.com/2010/04/coca-cola-light-get-dressed-by-another.html). Archived (https://web.arch
ive.org/web/20110721082512/http://ifitshipitshere.blogspot.com/2010/04/coca-cola-light-get-
dressed-by-another.html) from the original on July 21, 2011. Retrieved May 14, 2011.
119. Heyden, Dylan (October 9, 2019). "Coca-Cola Unveils First Bottles Made With Recycled
Ocean Plastic" (https://www.theinertia.com/environment/coca-cola-beverage-ocean-plastic-p
ollution/). The Inertia. Archived (https://web.archive.org/web/20191010021828/https://www.th
einertia.com/environment/coca-cola-beverage-ocean-plastic-pollution/) from the original on
October 10, 2019. Retrieved October 10, 2019.
120. "Islamic cola launched in the UK" (http://news.bbc.co.uk/2/hi/business/2720803.stm).
February 4, 2003. Archived (https://web.archive.org/web/20220321181035/http://news.bbc.c
o.uk/2/hi/business/2720803.stm) from the original on March 21, 2022. Retrieved July 23,
2020.
121. Mireles, Ricardo. "In Mexico, Big Cola is the real thing" (https://web.archive.org/web/200411
09222153/http://www.logisticstoday.com/sNO/6366/iID/20876/LT/displayStory.asp). Logistics
Today. Archived from the original (http://www.logisticstoday.com/sNO/6366/iID/20876/LT/disp
layStory.asp) on November 9, 2004.
122. "About Kristall Beverage" (https://web.archive.org/web/20031219013722/http://kristallbevera
ge.com/KBJulmust.html). Archived from the original (http://kristallbeverage.com/KBJulmust.h
tml) on December 19, 2003. Retrieved January 31, 2006.
123. Murden, Terry (January 30, 2005). Coke adds life to health drinks sector (https://web.archive.
org/web/20050304094426/http://scotlandonsunday.scotsman.com/business.cfm?id=112872
005). Scotland on Sunday. Retrieved February 14, 2006.
124. Kripalani, Manjeet and Mark L. Clifford (February 10, 2003) "Finally, Coke Gets It Right in
India" (http://www.businessweek.com/magazine/content/03_06/b3819080.htm) Archived (htt
ps://web.archive.org/web/20070207052221/http://www.businessweek.com/magazine/conten
t/03_06/b3819080.htm) February 7, 2007, at the Wayback Machine. BusinessWeek.
Retrieved August 9, 2006.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
125. "Fizzical Facts: Coke claims 60% mkt share in India" (http://economictimes.indiatimes.com/a
rticleshow/1191706.cms), Times News Network, August 5, 2005 Archived (https://web.archiv
e.org/web/20060630034238/http://economictimes.indiatimes.com/articleshow/1191706.cms)
June 30, 2006, at the Wayback Machine
126. "Mecca-Cola plans new factories for Middle East" (https://www.arabianbusiness.com/industri
es/retail/mecca-cola-plans-new-factories-for-middle-east-148332).
www.arabianbusiness.com. March 1, 2007. Archived (https://web.archive.org/web/20220321
181035/https://www.arabianbusiness.com/industries/retail/mecca-cola-plans-new-factories-f
or-middle-east-148332) from the original on March 21, 2022. Retrieved April 7, 2022.
127. "'Protest' drinks range targets Muslims" (https://www.theguardian.com/media/2003/apr/23/m
arketingandpr.iraq). The Guardian. April 23, 2003. Archived (https://web.archive.org/web/202
20321181035/https://www.theguardian.com/media/2003/apr/23/marketingandpr.iraq) from
the original on March 21, 2022. Retrieved March 2, 2022.
128. "Mentoring at Coca-Cola Foods" (https://www.coursehero.com/file/p1hh0sb/Around-the-worl
d-many-local-brands-compete-with-Coke-In-South-and-Central/). www.coursehero.com.
Archived (https://web.archive.org/web/20220111091705/https://www.coursehero.com/file/p1
hh0sb/Around-the-world-many-local-brands-compete-with-Coke-In-South-and-Central/) from
the original on January 11, 2022. Retrieved January 8, 2022.
129. "The Coca-Cola Companyv. Meenaxi Enterprise, Inc" (http://business.cch.com/ipld/CocaCol
aMeenaxieTTAB20210628.pdf) (PDF). UNITED STATES PATENT AND TRADEMARK
OFFICE. June 28, 2021. Archived (https://web.archive.org/web/20210723234428/http://busin
ess.cch.com/ipld/CocaColaMeenaxieTTAB20210628.pdf) (PDF) from the original on July
23, 2021.
130. Barbara Mikkelson and David P. Mikkelson, "The Claus That Refreshes (http://www.snopes.
com/cokelore/santa.asp)," snopes.com, February 27, 2001. Retrieved June 10, 2005.
Archived (https://wayback.archive-it.org/all/20051201022555/http://www.snopes.com/cokelor
e/santa.asp) December 1, 2005, at Archive-It
131. See George McKay 'Consumption, Coca-colonisation, cultural resistance – and Santa
Claus' (http://usir.salford.ac.uk/2227/) Archived (https://web.archive.org/web/2015041005161
2/http://usir.salford.ac.uk/2227/) April 10, 2015, at the Wayback Machine, in Sheila Whiteley,
ed. (2008) Christmas, Ideology and Popular Culture. Edinburgh University Press, pp. 50–70.
132. The White Rock Collectors Association, "Did White Rock or The Coca-Cola Company
create the modern Santa Claus Advertisement? (http://www.whiterocking.org/santa.html#arti
cle) Archived (https://web.archive.org/web/20211213214926/http://www.snopes.com/holiday
s/christmas/santa/cocacola.asp#article) December 13, 2021, at the Wayback Machine,"
whiterocking.org, 2001 . Retrieved January 19, 2007.
133. White Rock Beverages, "Coca-Cola's Santa Claus: Not The Real Thing! (http://www.bevnet.
com/news/2006/12-18-2006-white_rock_coke_santa_claus.asp)," BevNET.com, December
18, 2006 . Retrieved January 19, 2007. Archived (https://web.archive.org/web/20070117233
916/http://www.bevnet.com/news/2006/12-18-2006-white_rock_coke_santa_claus.asp)
January 17, 2007, at the Wayback Machine
134. "Coke means Coca-Cola" (https://web.archive.org/web/20110226184252/http://www.coca-c
olaconversations.com/my_weblog/2008/06/coke-means-coca.html). Coca-Cola
Conversations. June 16, 2008. Archived from the original (http://www.coca-colaconversation
s.com/my_weblog/2008/06/coke-means-coca.html) on February 26, 2011. Retrieved
March 13, 2011.
135. McKelvey, Steve M. (2006). "Coca-Cola vs. PepsiCo — A 'Super' Battleground for the Cola
Wars?". Sport MarHeting Quarterly. 15: 114–123. CiteSeerX 10.1.1.392.5206 (https://citesee
rx.ist.psu.edu/viewdoc/summary?doi=10.1.1.392.5206).
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
136. Orozco, Cynthia E. Quintanilla Perez, Selena. (http://www.tshaonline.org/handbook/online/ar
ticles/fquxg) Archived (https://web.archive.org/web/20200407230025/https://tshaonline.org/h
andbook/online/articles/fquxg) April 7, 2020, at the Wayback Machine The Handbook of
Texas online. Retrieved on June 5, 2006
137. "Coke Card loses its fizz" (https://strategyonline.ca/2002/03/25/coke-20020325/). Strategy.
Brunico Communications Ltd. March 25, 2002. Archived (https://web.archive.org/web/20220
319072309/https://strategyonline.ca/2002/03/25/coke-20020325/) from the original on March
19, 2022. Retrieved January 9, 2021.
138. My Coke Rewards (http://www.mycokerewards.com/) Archived (https://web.archive.org/web/
20091104025504/http://www.mycokerewards.com/) November 4, 2009, at the Wayback
Machine (Official Site)
139. Burke, Jessica (September 26, 2011). "Sharing your Coke: marketing genius or just entirely
weird?" (http://www.foodmag.com.au/news/sharing-your-coke--marketing-genius-or-just-entir
e). Foodmag.com.au. Archived (https://web.archive.org/web/20120130180750/http://www.foo
dmag.com.au/news/sharing-your-coke--marketing-genius-or-just-entire) from the original on
January 30, 2012. Retrieved February 23, 2013.
140. "What's in a Name?" (http://www.voxy.co.nz/lifestyle/whats-name/240/105315). Voxy.co.nz.
October 25, 2011. Archived (https://web.archive.org/web/20120305223011/http://www.voxy.c
o.nz/lifestyle/whats-name/240/105315) from the original on March 5, 2012. Retrieved
April 23, 2012.
141. "For Summer Campaign, Coke Prints 150 Popular First Names on Bottles" (http://www.desig
ntaxi.com/news/350737/For-Summer-Campaign-Coke-Prints-150-Popular-First-Names-on-
Bottles/?page=1). DesignTAXI.com. October 6, 2011. Archived (https://web.archive.org/web/
20120427073824/http://designtaxi.com/news/350737/For-Summer-Campaign-Coke-Prints-1
50-Popular-First-Names-on-Bottles/?page=1) from the original on April 27, 2012. Retrieved
April 23, 2012.
142. "Coca‑Cola Bottles History" (http://www.coca-cola.co.uk/125/coca-cola-bottles-history.html).
London, UK: Coca-Cola GB. 2013. Archived (https://web.archive.org/web/20110916070046/
http://www.coca-cola.co.uk/125/coca-cola-bottles-history.html) from the original on
September 16, 2011. Retrieved May 28, 2013.
143. "Share a Coke: Is your name on the list?" (http://www.belfasttelegraph.co.uk/lifestyle/share-a
-coke-is-your-name-on-the-list-29298254.html). The Belfast Telegraph. Belfast, UK:
Independent News & Media. May 27, 2013. Archived (https://web.archive.org/web/20130527
061305/http://www.belfasttelegraph.co.uk/lifestyle/share-a-coke-is-your-name-on-the-list-292
98254.html) from the original on May 27, 2013. Retrieved May 28, 2013.
144. "A Morning Cola Instead of Coffee?" (https://www.nytimes.com/1988/01/20/business/a-morni
ng-cola-instead-of-coffee.html). The New York Times. January 20, 1988. Archived (https://we
b.archive.org/web/20130424150535/http://www.nytimes.com/1988/01/20/business/a-mornin
g-cola-instead-of-coffee.html) from the original on April 24, 2013. Retrieved April 9, 2013.
145. McGrath, Karen (November 30, 1987). "Soft drink for breakfast could be your cup of tea" (http
s://news.google.com/newspapers?id=665JAAAAIBAJ&pg=4053,80769&dq=coca-cola+brea
kfast). Bangor Daily News. Archived (https://web.archive.org/web/20220719234648/https://n
ews.google.com/newspapers?id=665JAAAAIBAJ&pg=4053,80769&dq=coca-cola+breakfas
t) from the original on July 19, 2022. Retrieved April 9, 2013.
146. Sandison, Nikki (November 16, 2007). "Coca-Cola revives popular 'holidays are coming' ad"
(http://brandrepublic.com/News/767575/Coca-Cola-revives-popular-holidays-coming-ad/).
Brand Republic. Archived (https://web.archive.org/web/20110514201736/http://www.brandre
public.com/News/767575/Coca-Cola-revives-popular-holidays-coming-ad/) from the original
on May 14, 2011. Retrieved January 22, 2011.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
147. Armstrong, Stephen (May 14, 2001). "Coke goes for broke" (http://guardian.co.uk./media/200
1/may/14/mondaymediasection6). The Guardian. Guardian News and Media Limited.
Archived (https://web.archive.org/web/20091123155634/http://www.guardian.co.uk/media/20
01/may/14/mondaymediasection6) from the original on November 23, 2009. Retrieved
November 15, 2008.
148. "The Coca-Cola Challenge" (http://www.accessmylibrary.com/coms2/summary_0286-71403
27_ITM). Campaign. October 22, 2004. Archived (https://web.archive.org/web/20081206010
554/http://www.accessmylibrary.com/coms2/summary_0286-7140327_ITM) from the original
on December 6, 2008.
149. Hardy, Jane (December 27, 2007). "Do TV campaigns ad up?" (https://archive.today/201205
30045617/http://www.belfasttelegraph.co.uk/lifestyle/do-tv-campaigns-ad-up-13505247.htm
l). The Belfast Telegraph. Archived from the original (http://www.belfasttelegraph.co.uk./lifest
yle/do-tv-campaigns-ad-up-13505247.html) on May 30, 2012.
150. "Melanie Thornton: "Ich wollte immer Musik"" (http://spiegel.de./panorama/0,1518,169615,0
0.html). Der Spiegel (in German). SPIEGELnet GmbH. November 25, 2001. Archived (https://
web.archive.org/web/20081211064152/http://www.spiegel.de/panorama/0,1518,169615,00.
html) from the original on December 11, 2008. Retrieved November 15, 2008.
151. Prentiss Findlay (December 7, 2001). "Charleston native Thornton to be buried on Saturday"
(http://www.accessmylibrary.com/coms2/summary_0286-2079594_ITM). The Post and
Courier. Charleston, SC. Archived (https://web.archive.org/web/20081206010548/http://ww
w.accessmylibrary.com/coms2/summary_0286-2079594_ITM) from the original on
December 6, 2008.
152. Clark, Nicola (November 29, 2005). "Coca-Cola restructures in healthy drinks focus" (https://
web.archive.org/web/20110708090950/http://brandrepublic.com./News/530102/Coca-Cola-r
estructures-healthy-drinks-focus/). Brand Republic. Archived from the original (http://brandre
public.com./News/530102/Coca-Cola-restructures-healthy-drinks-focus/) on July 8, 2011.
153. "Coca-Cola launches its Diwali campaign " Best Media Info, News and Analysis on Indian
Advertising, Marketing and Media Industry" (http://www.bestmediainfo.com/2011/10/coca-col
a-launches-its-diwali-campaign/). Bestmediainfo.com. October 13, 2011. Archived (https://we
b.archive.org/web/20120522073503/http://www.bestmediainfo.com/2011/10/coca-cola-launc
hes-its-diwali-campaign/) from the original on May 22, 2012. Retrieved April 23, 2012.
154. "Coca-Cola Diwali!" (https://www.youtube.com/watch?v=mJeC_XTBSiQ). YouTube.
November 12, 2010. Archived (https://web.archive.org/web/20101120202637/https://www.yo
utube.com/watch?v=mJeC_XTBSiQ) from the original on November 20, 2010. Retrieved
April 23, 2012.
155. Heikkila, Pia (May 25, 2010). "From Bollywood to the world" (https://web.archive.org/web/20
120721134145/http://www.thenational.ae/thenationalconversation/industry-insights/media/fr
om-bollywood-to-the-world). The National. Archived from the original (http://www.thenational.
ae/thenationalconversation/industry-insights/media/from-bollywood-to-the-world) on July 21,
2012. Retrieved April 23, 2012.
156. "Coca-Cola" (http://www.olympic.org/sponsors/coca-cola). Olympic Movement. Archived (htt
ps://web.archive.org/web/20120821045818/http://www.olympic.org/sponsors/coca-cola) from
the original on August 21, 2012. Retrieved August 12, 2012.
157. "YouTube Post of Coca-Cola 2010 Olympic Hockey Commercial" (https://www.youtube.com/
watch?v=99msEwWpJBE). YouTube. Archived (https://web.archive.org/web/201306290519
32/http://www.youtube.com/watch?v=99msEwWpJBE) from the original on June 29, 2013.
Retrieved March 2, 2010.
158. FIFA.com. "FIFA Partners - FIFA.com" (https://web.archive.org/web/20170813010802/http://
www.fifa.com/about-fifa/marketing/sponsorship/partners/coca-cola.html). FIFA.com. Archived
from the original (https://www.fifa.com/about-fifa/marketing/sponsorship/partners/coca-cola.ht
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
www.fifa.com/about-fifa/marketing/sponsorship/partners/coca-cola.html). FIFA.com. Archived
from the original (https://www.fifa.com/about-fifa/marketing/sponsorship/partners/coca-cola.ht
ml) on August 13, 2017. Retrieved August 19, 2017.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
159. Brown, Maury (December 5, 2019). "Busch, Coca-Cola, GEICO, Xfinity Become Premier
Partners Of NASCAR Cup Series" (https://www.forbes.com/sites/maurybrown/2019/12/05/m
onster-energy-out-busch-coca-cola-geico-xfinity-become-premier-partners-of-nascar-cup-ser
ies/). Forbes. Archived (https://web.archive.org/web/20191206004234/https://www.forbes.co
m/sites/maurybrown/2019/12/05/monster-energy-out-busch-coca-cola-geico-xfinity-become-
premier-partners-of-nascar-cup-series/) from the original on December 6, 2019. Retrieved
December 5, 2019.
160. Wilson, Bill (September 18, 2018). "Premier League signs Coca-Cola as sponsor" (https://w
ww.bbc.com/news/business-45510553#:~:text=Drinks%20giant%20Coca%2DCola%20has,
Tag%20Heuer%20and%20EA%20Sports). BBC News. Archived (https://web.archive.org/we
b/20220321181205/https://www.bbc.com/news/business-45510553#:~:text=Drinks%20gian
t%20Coca%2DCola%20has,Tag%20Heuer%20and%20EA%20Sports) from the original on
March 21, 2022. Retrieved January 4, 2021.
161. "TOUR Championship by Coca-Cola" (http://www.pgatour.com/tournaments/tour-champions
hip-by-coca-cola.html). PGATour. Archived (https://web.archive.org/web/20160803233217/ht
tp://www.pgatour.com/tournaments/tour-championship-by-coca-cola.html) from the original
on August 3, 2016. Retrieved June 8, 2020.
162. "Coca-Cola to Release Gold Can Commemorating the 2010 Olympics" (http://bevwire.wordp
ress.com/2010/03/01/coca-cola-to-release-gold-can-commemorating-the-2010-olympics/).
BevWire. March 1, 2010. Archived (https://web.archive.org/web/20100312102638/http://bev
wire.wordpress.com/2010/03/01/coca-cola-to-release-gold-can-commemorating-the-2010-ol
ympics/) from the original on March 12, 2010. Retrieved March 22, 2010.
163. "Cristiano Ronaldo snub sees Coca-Cola market value fall by $4bn" (https://www.espn.com/
soccer/portugal-por/story/4410619/cristiano-ronaldo-snub-sees-coca-cola-share-price-fall-by
-$4bn). ESPN. June 16, 2021. Archived (https://web.archive.org/web/20220408070829/http
s://www.espn.com/soccer/portugal-por/story/4410619/cristiano-ronaldo-snub-sees-coca-cola
-share-price-fall-by-$4bn) from the original on April 8, 2022. Retrieved June 17, 2021.
164. "All Summer Long Lyrics – Beach Boys" (http://www.sing365.com/music/lyric.nsf/All-Summe
r-Long-lyrics-Beach-Boys/A1E9E6CD61DA8C5F482569820027FD26). Sing365.com.
Archived (https://web.archive.org/web/20120709051217/http://www.sing365.com/music/lyric.
nsf/All-Summer-Long-lyrics-Beach-Boys/A1E9E6CD61DA8C5F482569820027FD26) from
the original on July 9, 2012. Retrieved April 23, 2012.
165. "Best-selling solo artist" (https://www.guinnessworldrecords.com/world-records/best-selling-
solo-artist). Guinness World Records. Archived (https://web.archive.org/web/202206241656
49/https://www.guinnessworldrecords.com/world-records/best-selling-solo-artist) from the
original on June 24, 2022. Retrieved March 26, 2021.
166. "Elvis Presley" (https://www.youtube.com/watch?v=6mdJeY-r9To). YouTube. June 21, 1977.
Archived (https://web.archive.org/web/20140314135816/http://www.youtube.com/watch?v=6
mdJeY-r9To) from the original on March 14, 2014. Retrieved August 12, 2012.
167. "Coca Cola celebrates 125th anniversary with 'Elvis and Coke'" (https://archive.today/20120
425231553/http://rica.alfahosting.org/everythingelvis/index.php?option=com_content&view=
article&id=23196:coca-cola-celebrates-125th-anniversary-with-elvis-and-coke&catid=26:elvi
s-presley-news&Itemid=107). Rica.alfahosting.org. Archived from the original (http://rica.alfa
hosting.org/everythingelvis/index.php?option=com_content&view=article&id=23196:coca-co
la-celebrates-125th-anniversary-with-elvis-and-coke&catid=26:elvis-presley-news&Itemid=1
07) on April 25, 2012. Retrieved April 23, 2012.
168. "Elvis Music in Japanese Coca-Cola Commercial – Misc" (http://www.elvisnews.com/news.a
spx/elvis-music-in-japanese-coca-cola-commercial/13178). ElvisNews.com. Archived (http
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
168. "Elvis Music in Japanese Coca-Cola Commercial – Misc" (http://www.elvisnews.com/news.a
spx/elvis-music-in-japanese-coca-cola-commercial/13178). ElvisNews.com. Archived (http
s://web.archive.org/web/20120415053157/http://www.elvisnews.com/news.aspx/elvis-music
-in-japanese-coca-cola-commercial/13178) from the original on April 15, 2012. Retrieved
April 23, 2012.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
169. "David Bowie: Coca-Cola Planet Live (Rare Euro Promo) FLAC – Guitars101 – Guitar
Forums" (https://archive.today/20120906044352/http://www.guitars101.com/forums/f145/davi
d-bowie-coca-cola-planet-live-rare-euro-promo-flac-64418.html). Guitars101. Archived from
the original (http://www.guitars101.com/forums/f145/david-bowie-coca-cola-planet-live-rare-
euro-promo-flac-64418.html) on September 6, 2012. Retrieved April 23, 2012.
170. Diet Coke commercial (https://www.youtube.com/watch?v=gp5SioXLdXQ) on YouTube
171. "Coca Cola Light CM – Elton John" (https://www.youtube.com/watch?v=GfOepK2CgLc).
YouTube. Archived (https://web.archive.org/web/20130520213349/http://www.youtube.com/
watch?v=GfOepK2CgLc) from the original on May 20, 2013. Retrieved April 23, 2012.
172. "Whitney Houston – Diet Coke Commercial (1986)" (https://www.youtube.com/watch?v=DTg
9BQn3PVU). YouTube. June 14, 2010. Archived (https://web.archive.org/web/20130520150
658/http://www.youtube.com/watch?v=DTg9BQn3PVU) from the original on May 20, 2013.
Retrieved April 23, 2012.
173. "Banning songs not a rare occurrence for the BBC" (http://www.nzherald.co.nz/radio-industr
y/news/article.cfm?c_id=295&objectid=10483279&ref=rss). The New Zealand Herald.
December 19, 2007. Archived (https://web.archive.org/web/20110522195645/http://www.nzh
erald.co.nz/radio-industry/news/article.cfm?c_id=295&objectid=10483279&ref=rss) from the
original on May 22, 2011. Retrieved October 15, 2011.
174. Giles, Jeff. "45 Years Ago: Ray Davies Flies Across the Atlantic – Twice! – to Re-Record
Two Words in 'Lola'" (http://ultimateclassicrock.com/kinks-lola-lyric-changes/). Ultimate
Classic Rock. Archived (https://web.archive.org/web/20150607022039/http://ultimateclassicr
ock.com/kinks-lola-lyric-changes/) from the original on June 7, 2015. Retrieved June 6,
2015.
175. "And I Love New York" (http://rogallery.com/Kichka_Michel/kichka-new_york.html).
Rogallery.com. Archived (https://web.archive.org/web/20080804104428/http://rogallery.com/
Kichka_Michel/kichka-new_york.html) from the original on August 4, 2008. Retrieved
November 10, 2012.
176. Mark Pendergrast (August 15, 1993). "Viewpoints; A Brief History of Coca-Colonization" (htt
ps://www.nytimes.com/1993/08/15/business/viewpoints-a-brief-history-of-coca-colonization.
html). The New York Times. p. 256. Archived (https://web.archive.org/web/20121120082810/
http://www.nytimes.com/1993/08/15/business/viewpoints-a-brief-history-of-coca-colonizatio
n.html) from the original on November 20, 2012. Retrieved September 12, 2012.
177. Koetse, Manya (September 24, 2015). "Coca Cola in China" (http://www.whatsonweibo.com/
coca-cola-in-china/). Marketing. Netherlands: whatsonweibo.com. Archived (https://web.arch
ive.org/web/20160617165423/http://www.whatsonweibo.com/coca-cola-in-china/) from the
original on June 17, 2016. Retrieved May 19, 2016.
178. "Boycott Israel Campaign page on Coca-Cola" (http://www.inminds.co.uk/boycott-coca-cola.
html). Archived (https://web.archive.org/web/20070907035921/http://www.inminds.co.uk/boy
cott-coca-cola.html) from the original on September 7, 2007. Retrieved August 3, 2007.
179. Tagliabue, John (December 31, 2002). "They Choke on Coke, But Savor Mecca-Cola" (http
s://www.nytimes.com/2002/12/31/international/europe/31FRAN.html). The New York Times.
Archived (https://web.archive.org/web/20130616072000/http://www.nytimes.com/2002/12/3
1/international/europe/31FRAN.html) from the original on June 16, 2013. Retrieved July 26,
2013 – via NYTimes.com.
180. Pearlman, Robert. "Coke machines on-board the space shuttle" (http://www.collectspace.co
m/ubb/Forum14/HTML/000692.html). CollectSpace. Archived (https://web.archive.org/web/2
0181022055341/http://www.collectspace.com/ubb/Forum14/HTML/000692.html) from the
original on October 22, 2018. Retrieved June 8, 2020.
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.


> Entering new LLMChain chain...
Prompt after formatting:
Your job is to produce a final summary
We have provided an existing summary up to a certain point:

Coca-Cola is a carbonated soft drink manufactured by the Coca-Cola Company and sold in over 200 countries worldwide. It was invented in the late 19th century by John Stith Pemberton, a local pharmacist in Atlanta, Georgia. The drink's name refers to two of its original ingredients: coca leaves and kola nuts. The Coca-Cola Company produces concentrate, which is then sold to licensed Coca-Cola bottlers who produce the finished product in cans and bottles. The company also sells other cola drinks under the Coke name, such as Diet Coke, Caffeine-Free Coca-Cola, Coca-Cola Zero Sugar, Coca-Cola Vanilla, Coca-Cola Cherry, Coca-Cola Citra, Coca-Cola Lime, Coca-Cola Mango, Coca-Cola with Lemon, Coca-Cola Raspberry, Coca-Cola Citra, Coca-Cola Black Cherry Vanilla, Coca-Cola Blāk, Coca-Cola Orange, Coca-Cola Life, Coca-Cola Ginger, Coca-Cola Fiber+, Coca-Cola Energy, Coca-Cola Cinnamon, Coca-Cola with Coffee, Coca-Cola Cherry Vanilla, Coca-Cola Starlight, Coca-Cola Marshmello, Coca-Cola Dreamworld, and Coca
We have the opportunity to refine the existing summary(only if needed) with some more context below.
------------
181. Orloff, Richard W. (January 2001) [Press Kit May 1996]. "Space Shuttle Mission STS-77" (htt
p://www.jsc.nasa.gov/history/shuttle_pk/pk/Flight_077_STS-077_Press_Kit.pdf) (PDF).
National Aeronautics and Space Administration. Archived (https://web.archive.org/web/2003
0327212757/http://www.jsc.nasa.gov/history/shuttle_pk/pk/Flight_077_STS-077_Press_Kit.
pdf) (PDF) from the original on March 27, 2003. Retrieved June 13, 2009.
182. Iwamuro M.; Okada H.; Matsueda K.; Inaba T.; Kusumoto C.; Imagawa A.; Yamamoto K.
(2015). "Review of the diagnosis and management of gastrointestinal bezoars" (https://www.
ncbi.nlm.nih.gov/pmc/articles/PMC4400622). World Journal of Gastrointestinal Endoscopy.
7 (4): 336–345. doi:10.4253/wjge.v7.i4.336 (https://doi.org/10.4253%2Fwjge.v7.i4.336).
PMC 4400622 (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4400622). PMID 25901212
(https://pubmed.ncbi.nlm.nih.gov/25901212).
183. "Stomach, Definition and Patient Education" (http://www.healthline.com/health/stomach#Ov
erview1). Healthline. Archived (https://web.archive.org/web/20150714084951/http://www.he
althline.com/health/stomach#Overview1) from the original on July 14, 2015. Retrieved
July 10, 2015.
184. Benjamin, Ludy T.; Rogers, Anne M.; Rosenbaum, Angela (January 1, 1991). "Coca-Cola,
caffeine, and mental deficiency: Harry Hollingworth and the Chattanooga trial of 1911".
Journal of the History of the Behavioral Sciences. 27 (1): 42–55. doi:10.1002/1520-
6696(199101)27:1<42::AID-JHBS2300270105>3.0.CO;2-1 (https://doi.org/10.1002%2F1520
-6696%28199101%2927%3A1%3C42%3A%3AAID-JHBS2300270105%3E3.0.CO%3B2-
1). ISSN 1520-6696 (https://www.worldcat.org/issn/1520-6696). PMID 2010614 (https://pubm
ed.ncbi.nlm.nih.gov/2010614).
185. Martin, Douglas (May 6, 2007). "Edward F. Boyd Dies at 92; Marketed Pepsi to Blacks" (http
s://www.nytimes.com/2007/05/06/business/06boyd.html?_r=1&ref=obituaries&oref=slogin).
The New York Times. Archived (https://web.archive.org/web/20181214011657/https://www.n
ytimes.com/2007/05/06/business/06boyd.html?_r=1&ref=obituaries&oref=slogin) from the
original on December 14, 2018. Retrieved June 5, 2019.
186. Brian D. Behnken, Gregory D. Smithers (2015). "Racism in American Popular Media: From
Aunt Jemima to the Frito Bandito". p. 34. ABC-CLIO
187. Delshad, Irani (February 24, 2016). "Is Coca-Cola an easy target? Or are its critics right?" (ht
tps://economictimes.indiatimes.com/magazines/brand-equity/is-coca-cola-an-easy-target-or-
are-its-critics-right/articleshow/51106125.cms). The Economic Times. Archived (https://web.
archive.org/web/20180801034412/https://economictimes.indiatimes.com/magazines/brand-
equity/is-coca-cola-an-easy-target-or-are-its-critics-right/articleshow/51106125.cms) from the
original on August 1, 2018. Retrieved July 31, 2018.
188. Segran, Elizabeth (November 1, 2019). "Coca-Cola, Nestlé, and PepsiCo are the world's
biggest plastic polluters—again" (https://www.fastcompany.com/90425011/coca-cola-nestle-
and-pepsico-are-the-worlds-biggest-plastic-polluters-again). Fast Company. Archived (http
s://web.archive.org/web/20200208145659/https://www.fastcompany.com/90425011/coca-col
a-nestle-and-pepsico-are-the-worlds-biggest-plastic-polluters-again) from the original on
February 8, 2020. Retrieved February 17, 2020.
189. Thomas, Daniel (January 21, 2020). "People still want plastic bottles, says Coca-Cola" (http
s://www.bbc.com/news/business-51197463). BBC News. Archived (https://web.archive.org/
web/20200130025249/https://www.bbc.com/news/business-51197463) from the original on
January 30, 2020. Retrieved February 17, 2020.
190. "Coca-Cola Pledges 25% Reusable Packaging by 2030 - February 16, 2022" (https://dailyn
ewsbrief.com/2022/02/16/coca-cola-pledges-25-reusable-packaging-by-2030/). The Daily
NewsBrief. February 16, 2022. Archived (https://web.archive.org/web/20220319192200/http
s://dailynewsbrief.com/subscribe/monthly/?mepr-unauth-page=15342&redirect_to=%2F202
------------
Given the new context, refine the original summary
If the context isn't useful, return the original summary.

> Finished chain.
```
</details>
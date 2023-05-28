import tiktoken
from devtools import debug
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from pydantic import BaseModel, Field

################################
# Prepare texts for search
################################

loader = PyPDFLoader("../data/coca-cola-from-wikipedia.pdf")
pages = loader.load_and_split()

encoding = tiktoken.encoding_for_model("gpt-4")

token_count = 0
for p in pages:
    tokens = encoding.encode(p.page_content)
    token_count += len(tokens)

print(f"token: {token_count}")

################################
# Store embeddings in Vector DB
################################

# https://github.com/facebookresearch/faiss
embeddings = OpenAIEmbeddings()
# Return a vector store storeing text embeddings.
vector_db = FAISS.from_documents(pages, embeddings)
docsearch = vector_db.as_retriever()

################################
# Retrieve context from Vector DB
################################

product = "Coca Cola"
query = f"What is {product}?"
context = docsearch.get_relevant_documents(query)


################################
# Prepare Pydantic Output Parser
################################
class Product(BaseModel):
    name: str = Field(description=f"name of {product}")
    kind: str = Field(description=f"kind of {product}")
    inventor: str = Field(description=f"inventor of {product}")
    born_date: str = Field(description=f"born date of {product}")


# Set up a parser + inject instructions into the prompt template.
parser = PydanticOutputParser(pydantic_object=Product)

################################
# Prepare a prompt
################################
prompt = PromptTemplate(
    template="""Use the following pieces of context to answer the question at the end. If you don't know the answer,
    just say that you don't know, don't try to make up an answer.

    Context:
    ---------
    {context}
    ---------

    {format_instructions}

    Question: {query}
    """,
    input_variables=["query", "context"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
    output_parser=parser,
)

#################################
# Structured format output by LLM
#################################
# NOTE: gpt-3.5-turbo does not create expected JSON formatted answer.
# Use gpt 4 or later to use Pydantic Output Parser to output
# as JSON structured data.
chain = load_qa_chain(ChatOpenAI(temperature=0, model_name="gpt-4"), chain_type="stuff", prompt=prompt, verbose=True)
output = chain.run(
    input_documents=context,
    return_only_outputs=True,
    query=query,
)

print(f"# Question: {query}")
p: Product = parser.parse(output)
debug(p)

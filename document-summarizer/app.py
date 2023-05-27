import tiktoken
from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader

MAX_TOKEN_FOR_OPEN_API_GPT_3_5 = 4096

llm = OpenAI(temperature=0)
loader = PyPDFLoader("data/coca-cola-from-wikipedia.pdf")
# load_and_split returns List[Document]. So, we don't need text splitter.
pages = loader.load_and_split()

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

token_count = 0
for p in pages:
    tokens = encoding.encode(p.page_content)
    token_count += len(tokens)

print(f"token: {token_count}")

# Stuff summary Stuffing is the simplest method, whereby you simply stuff all the related data into the prompt as
# context to pass to the language model. This is implemented in LangChain as the StuffDocumentsChain.
# Pros: Only makes a single call to the LLM. When generating text, the LLM has access to all the data at once.
# Cons: Most LLMs have a context length, and for large documents (or many documents) this will not work as it will
# result in a prompt larger than the context length.
# The main downside of this method is that it only works on smaller pieces of data. Once you are working with many
# pieces of data, this approach is no longer feasible. The next two approaches are designed to help deal with that.
# NOTE: my expectation for this method is this does not work for wikipedia document summarization because its huge.
# if (token_count > MAX_TOKEN_FOR_OPEN_API_GPT_3_5):
#     raise Exception(f"stuff chain is not appropriate to summarize huge text data. The token for summarization is {token_count}")
# else:
#   chain = load_summarize_chain(llm, chain_type="stuff")
#   chain.run(pages)

# Refine This method involves running an initial prompt on the first chunk of data, generating some output. For the
# remaining documents, that output is passed in, along with the next document, asking the LLM to refine the output
# based on the new document.
# Pros: Can pull in more relevant context, and may be less lossy than MapReduceDocumentsChain.
# Cons: Requires many more calls to the LLM than StuffDocumentsChain. The calls are also NOT independent,
# meaning they cannot be paralleled like MapReduceDocumentsChain. There is also some potential dependencies on the
# ordering of the documents.
chain = load_summarize_chain(llm, chain_type="refine", verbose=True, return_intermediate_steps=True)
chain({"input_documents": pages}, return_only_outputs=True)

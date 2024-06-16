from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from core.config import OpenAIConfig

OPENAI_API_KEY = OpenAIConfig.OPENAI_API_KEY

# # load the document
loader = TextLoader("ai/text.txt")
document = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=2500, chunk_overlap=0)
text = text_splitter.split_documents(document)

# ---
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Chroma vector  store
docsearch = Chroma.from_documents(text, embeddings)
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(openai_api_key=OPENAI_API_KEY),
    chain_type="stuff",
    retriever=docsearch.as_retriever(),
)

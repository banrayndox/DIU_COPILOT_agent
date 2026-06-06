from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load PDF
loader = PyPDFLoader("pdfs/nothuman.pdf")
docs = loader.load()

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

# Embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store into ChromaDB
db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="./db"
)

db.persist()

print("Embedding Complete")
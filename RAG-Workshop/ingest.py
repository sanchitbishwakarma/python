from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from config import embeddings

print("Loading CSV...")

loader = CSVLoader(
    file_path="data/RAG-Registration.csv",
    encoding="utf-8"
)

documents = loader.load()

print(documents[:2])  # Preview first two rows
print(f"Loaded {len(documents)} rows")

print("Splitting document...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,   #1000 characters per chunk
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

print("Creating vector database...")

Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

print("Done!")
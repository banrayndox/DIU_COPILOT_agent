from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

memory_db = Chroma(
    collection_name="user_memory",
    persist_directory="./db/memory_db",
    embedding_function=embedding
)


def save_memory(user_id, memory_text):

    memory_db.add_texts(
        texts=[memory_text],
        metadatas=[
            {
                "user_id": user_id
            }
        ]
    )


def retrieve_memory(user_id, query):

    docs = memory_db.similarity_search(
        query=query,
        k=3,
        filter={
            "user_id": user_id
        }
    )

    return "\n".join(
        [doc.page_content for doc in docs]
    )
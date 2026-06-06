from typing import Generator
import os

from langchain_chroma import Chroma
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq

from memory.short_term import save_message, get_history
from memory.long_term import retrieve_memory, save_memory

load_dotenv()

# -----------------------------
# VECTOR DB (LOAD ONCE ONLY)
# -----------------------------
db = Chroma(
    persist_directory="./db"
)

retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

# -----------------------------
# AGENT
# -----------------------------
def build_agent():

    return Agent(
        model=Groq(
            id="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY")
        ),
        instructions="""
        You are a helpful assistant for students.
        Answer clearly and concisely.
        """,
        tools=[],
        tool_choice="none"
    )

# -----------------------------
# STREAM FUNCTION
# -----------------------------
def ask_question_stream(question: str, user_id: str) -> Generator[str, None, None]:

    agent = build_agent()

    # -----------------------------
    # HISTORY
    # -----------------------------
    history = get_history(user_id)

    formatted_history = "\n".join(
        f"{m['role']}: {m['content']}"
        for m in history
    )

    # -----------------------------
    # MEMORY
    # -----------------------------
    memory_context = retrieve_memory(user_id, question)

    # -----------------------------
    # RAG
    # -----------------------------
    docs = retriever.invoke(question)

    rag_context = "\n".join(
        d.page_content for d in docs
    )

    # -----------------------------
    # FINAL PROMPT
    # -----------------------------
    prompt = f"""
You are a helpful assistant.

Conversation:
{formatted_history}

Memory:
{memory_context}

Context:
{rag_context}

Question:
{question}
"""

    # -----------------------------
    # STREAM
    # -----------------------------
    stream = agent.run(prompt, stream=True)

    ai_message = ""

    for chunk in stream:

        token = chunk.content

        if token:
            ai_message += token
            yield token

    # -----------------------------
    # MEMORY SAVE (IMPORTANT ORDER)
    # -----------------------------
    save_message(user_id, "user", question)
    save_message(user_id, "assistant", ai_message)

    # -----------------------------
    # LONG TERM MEMORY CHECK
    # -----------------------------
    lower = question.lower()

    if any(
        k in lower
        for k in [
            "remember",
            "my name",
            "i like",
            "i study",
            "my goal",
            "i prefer"
        ]
    ):
        save_memory(user_id, question)
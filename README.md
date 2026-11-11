# DIU Copilot — Autonomous AI Agent & RAG Reasoning Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Orchestration-1C3C3C?style=flat-square)](https://www.langchain.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-FF6B6B?style=flat-square)](https://www.trychroma.com/)
[![Uvicorn](https://img.shields.io/badge/Server-Uvicorn-499848?style=flat-square&logo=gunicorn)](https://www.uvicorn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

> The autonomous AI agent reasoning engine powering DIU Copilot. Leverages Retrieval-Augmented Generation (RAG) and multi-step agent reasoning to answer Daffodil International University academic queries.

**Frontend Client:** [banrayndox/DIU_COPILOT_frontend](https://github.com/banrayndox/DIU_COPILOT_frontend)  
**Backend Gateway:** [banrayndox/DIU_COPILOT_backend](https://github.com/banrayndox/DIU_COPILOT_backend)

---

## 📌 Overview

**DIU Copilot Agent** is a specialized AI microservice engineered with Python, FastAPI, and LangChain/Agno. It ingests official Daffodil International University handbooks, grading policy guidelines, transportation schedules, and exam routines to provide accurate, hallucination-resistant answers grounded in factual campus documentation.

---

## 🚀 Key Features

* **Retrieval-Augmented Generation (RAG):** Dense vector similarity search over university documentation using [ChromaDB](https://www.trychroma.com/).
* **Document Ingestion Pipeline (`ingest.py`):** Automated text extraction, recursive chunking, and embedding generation for PDF documents located in `pdfs/`.
* **Multi-Step Agent Reasoning:** Integrated agent workflows with [Agno](https://github.com/agno-agi/agno) and [LangChain](https://www.langchain.com/) to analyze complex multi-part academic questions.
* **Session Memory Management:** Short-term and long-term dialogue context retention (`memory/` & `state.json`).
* **High-Throughput Asynchronous API:** Powered by [FastAPI](https://fastapi.tiangolo.com/) and [Uvicorn](https://www.uvicorn.org/) for fast, low-latency streaming inference.

---

## 🛠️ Technology Stack

* **Language:** [Python 3.10+](https://www.python.org/)
* **Web Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **ASGI Server:** [Uvicorn](https://www.uvicorn.org/)
* **Vector Database:** [ChromaDB](https://www.trychroma.com/)
* **Agent & LLM Tooling:** [Agno](https://github.com/agno-agi/agno), [LangChain](https://www.langchain.com/), [LangChain Community](https://pypi.org/project/langchain-community/)

---

## 📁 Repository Structure

```
DIU_COPILOT_agent/
├── db/                   # Persistent ChromaDB vector database index
├── memory/               # Context memory & persistent session storage
├── pdfs/                 # Source university document PDFs (handbooks, rules)
├── tools/                # Specialized agent tool functions & search utilities
├── ingest.py             # Document loading, chunking & vector indexing script
├── main.py               # FastAPI server application & API endpoints
├── query.py              # Semantic similarity search & RAG query runner
├── requirements.txt      # Python package dependencies
└── state.json            # Agent execution state configuration
```

---

## ⚙️ Getting Started

### Prerequisites
* **Python:** 3.10 or higher
* **pip:** Python package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/banrayndox/DIU_COPILOT_agent.git
   cd DIU_COPILOT_agent
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows:
   venv\Scripts\activate
   
   # Linux / macOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   OPENAI_API_KEY=your_openai_or_embedding_api_key
   CHROMA_DB_PATH=./db
   PORT=8000
   ```

5. **Index Document Knowledge Base:**
   Place any university PDF handbooks inside the `pdfs/` folder, then run:
   ```bash
   python ingest.py
   ```
   This will process the documents and create the vector embeddings inside `db/`.

6. **Start the Agent Service:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```
   The agent API will be available at `http://localhost:8000`. Interactive Swagger documentation can be viewed at `http://localhost:8000/docs`.

---

## 🔗 Related Repositories

* **Frontend Client:** [banrayndox/DIU_COPILOT_frontend](https://github.com/banrayndox/DIU_COPILOT_frontend)
* **Backend Gateway:** [banrayndox/DIU_COPILOT_backend](https://github.com/banrayndox/DIU_COPILOT_backend)

---

## 👨‍💻 Author

**Rakib B**
* GitHub: [@banrayndox](https://github.com/banrayndox)
* Website: [banrayndox.github.io](https://banrayndox.github.io/)
* Institution: Daffodil International University (DIU)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

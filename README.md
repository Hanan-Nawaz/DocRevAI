# DocRevAI

DocRevAI is an AI-powered document analysis and question-answering system that enables users to upload PDF documents and ask questions about their content. The application extracts text from PDFs, processes the content, retrieves relevant information using TF-IDF similarity search, and generates context-aware responses using local Large Language Models (LLMs) through Ollama.

## Features

* PDF document ingestion
* Text extraction and preprocessing
* Intelligent text chunking
* TF-IDF based document retrieval
* Context-aware question answering
* Local AI inference using Ollama
* Modular and scalable architecture
* Comprehensive logging and error handling

## Project Workflow

```text
PDF Upload
    ↓
Text Extraction
    ↓
Text Cleaning
    ↓
Chunk Creation
    ↓
TF-IDF Vectorization
    ↓
Similarity Search
    ↓
Context Retrieval
    ↓
Ollama LLM
    ↓
Generated Response
```

## Tech Stack

### Backend

* Python 3.12+
* Ollama
* Scikit-learn
* PyPDF2 / PDF Processing Libraries
* Logging Module

### AI & Retrieval

* TF-IDF Vectorization
* Cosine Similarity Search
* Local Language Models via Ollama

### Development Tools

- uv
- Git
- GitHub
- Jira
- Pytest

### Dependency Management

This project uses **uv** for package management and virtual environment handling, providing faster dependency resolution and installation compared to traditional pip-based workflows.

## Project Structure

```text
DocRevAI/
│
├── docrevai/
│   ├── scripts/
│   │   ├── clean_text.py
│   │   ├── create_chunks.py
│   │   ├── similarity_finder.py
│   │   ├── tf_idf.py
│   │   └── ...
│   │
│   ├── logging/
│   │   └── logger.py
│   │
│   └── ...
│
├── tests/
│
├── logs/
│
├── pyproject.toml
│
├── uv.lock
│
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/Hanan-Nawaz/DocRevAI
cd DocRevAI
```

### Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

or

```bash
pip3 install uv
```

### Create Virtual Environment

```bash
uv venv
```

Activate environment:

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
uv sync
```

## Running the Project

```bash
uv run main.py
```

## Testing

Run all tests:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov=docrevai
```

## Logging

DocRevAI includes centralized logging for:

* Error tracking
* Debugging
* System monitoring
* Runtime diagnostics

Logs are stored in the project's log directory.

## Project Management

The project follows Agile development practices and uses Jira for:

* Sprint planning
* Task management
* Issue tracking
* Feature development tracking

## Future Enhancements

* Semantic search using embeddings
* Vector databases (FAISS / ChromaDB)
* Multi-document support
* Web-based user interface
* Conversation memory
* Document summarization
* Citation and source highlighting
* Hybrid retrieval (TF-IDF + Embeddings)

## Author

Abdul Hanan Nawaz

## License

This project is intended for educational and portfolio purposes.

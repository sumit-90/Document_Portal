# Document Portal

A RAG (Retrieval-Augmented Generation) based document processing pipeline that enables intelligent ingestion, analysis, comparison, and conversational Q&A over documents. Built with FastAPI, LangChain, LlamaIndex, and multiple LLM providers.

## Features

- **RAG Pipeline** - End-to-end Retrieval-Augmented Generation pipeline for accurate, context-grounded answers
- **Document Ingestion** - Upload and preprocess documents (PDF, DOCX, PPTX, Excel, HTML, Markdown) with chunking and embedding
- **Document Analyzer** - Analyze document content using LLMs for summarization, key extraction, and insights
- **Document Compare** - Compare multiple documents to find similarities, differences, and overlaps
- **Document Chat** - Conversational Q&A interface powered by RAG over your document knowledge base
- **Multi-LLM Support** - Works with OpenAI, Anthropic Claude, Google Gemini, Cohere, Groq, and local models via Ollama
- **Multiple Vector Stores** - Store and retrieve embeddings with Pinecone, ChromaDB, Qdrant, Milvus, or FAISS
- **OCR Support** - Extract text from images and scanned documents using EasyOCR
- **Web Scraping** - Ingest content from web pages using Scrapy, Selenium, Playwright, or Firecrawl
- **RAG Evaluation** - Measure pipeline quality (faithfulness, relevancy, context precision) with DeepEval and RAGAS

## Folder Structure

```
Document_Portal/
├── api/                        # API endpoint definitions
├── config/
│   └── config.yaml             # Application configuration
├── exception/
│   └── custom_exception.py     # Custom exception classes
├── infrastructure/             # Infrastructure and deployment configs
├── logger/
│   └── custom_logger.py        # Centralized logging setup
├── model/
│   └── models.py               # Database and data models
├── notebook/
│   └── experiments.ipynb        # Jupyter notebooks for experimentation
├── prompt/
│   └── __init__.py             # Prompt templates and management
├── src/
│   ├── __init__.py
│   ├── document_ingestion/     # Document upload and preprocessing
│   ├── document_analyzer/      # LLM-based document analysis
│   ├── document_compare/       # Multi-document comparison
│   └── document_chat/          # Conversational Q&A over documents
├── static/
│   └── style.css               # Frontend stylesheets
├── templates/
│   └── index.html              # HTML templates (Jinja2)
├── tests/
│   └── __init__.py             # Test suite
├── utils/
│   └── LLM_utils.py            # LLM helper utilities
├── app.py                      # Application entry point
├── setup.py                    # Package setup
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker container definition
├── .env                        # Environment variables (not tracked)
└── README.md
```

## Installation

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- Git
- (Optional) Docker

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Document_Portal
```

### 2. Create a Virtual Environment

```bash
uv venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root with your API keys:

```env
# LLM Providers
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
COHERE_API_KEY=your_cohere_key
GROQ_API_KEY=your_groq_key

# Vector Databases
PINECONE_API_KEY=your_pinecone_key
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_key

# Cloud Providers (if using)
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_DEFAULT_REGION=your_aws_region

# Database
DATABASE_URL=your_database_url
```

> Only add the keys for the providers you plan to use.

### 5. Configure Application Settings

Edit `config/config.yaml` with your desired settings for LLM providers, vector stores, and document processing options.

## Usage

### Running the Application

```bash
# Start the FastAPI server
python app.py

# Or use uvicorn directly
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

The application will be available at `http://localhost:8000`.

### Running with Streamlit

```bash
streamlit run app.py
```

### Running with Docker

```bash
# Build the image
docker build -t document-portal .

# Run the container
docker run -p 8000:8000 --env-file .env document-portal
```

### Running Experiments

Open `notebook/experiments.ipynb` in Jupyter to explore and experiment with the document processing pipeline:

```bash
jupyter notebook notebook/experiments.ipynb
```

## API Documentation

Once the server is running, interactive API docs are available at:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Planned Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/ingest` | Upload and ingest a document |
| GET | `/api/documents` | List all ingested documents |
| GET | `/api/documents/{id}` | Get document details |
| POST | `/api/analyze` | Analyze a document |
| POST | `/api/compare` | Compare two or more documents |
| POST | `/api/chat` | Chat with your documents |
| GET | `/api/health` | Health check |

## Tech Stack

| Category | Technologies |
|----------|-------------|
| Web Framework | FastAPI, Streamlit, Uvicorn |
| LLM Orchestration | LangChain, LangGraph, LlamaIndex |
| LLM Providers | OpenAI, Anthropic, Google GenAI, Cohere, Groq, Ollama |
| Vector Databases | Pinecone, ChromaDB, Qdrant, Milvus, FAISS |
| Document Processing | Docling, Unstructured, PyPDF, PyMuPDF, python-docx, python-pptx |
| OCR | EasyOCR, OpenCV |
| Embeddings | Sentence Transformers, HuggingFace Transformers |
| Database | PostgreSQL, SQLAlchemy |
| ML / Deep Learning | PyTorch, scikit-learn |
| Web Scraping | Scrapy, Selenium, Playwright, Firecrawl |
| Evaluation | DeepEval, RAGAS |
| Observability | Sentry, OpenTelemetry, Opik |
| Testing | Pytest |
| Code Quality | Black, Ruff, Flake8, MyPy |
| Cloud | AWS (S3, Bedrock), Google Cloud |

## Testing

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run tests in parallel
pytest -n auto

# Run a specific test file
pytest tests/test_ingestion.py
```

## Code Quality

```bash
# Format code
black .

# Lint
ruff check .
flake8 .

# Type checking
mypy .
```

## Contributing

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make** your changes and write tests
4. **Run** linting and tests
   ```bash
   black .
   ruff check .
   pytest
   ```
5. **Commit** with a descriptive message
   ```bash
   git commit -m "Add: brief description of your change"
   ```
6. **Push** to your fork and open a **Pull Request**

### Commit Message Convention

| Prefix | Usage |
|--------|-------|
| `Add:` | New feature or file |
| `Fix:` | Bug fix |
| `Update:` | Enhancement to existing feature |
| `Refactor:` | Code restructuring without behavior change |
| `Docs:` | Documentation only |
| `Test:` | Adding or updating tests |

## License

This project is for private use. Contact the repository owner for licensing information.

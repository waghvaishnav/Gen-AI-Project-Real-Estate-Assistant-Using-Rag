# 🏠 Real Estate Assistant Using RAG

> **An AI-powered Real Estate Research Assistant that uses Retrieval-Augmented Generation (RAG) to analyze information from multiple web sources and provide research-based answers with references.**

---

## 📌 Overview

**Real Estate Assistant Using RAG** is a Generative AI application designed to simplify real estate market research using information collected from user-provided web sources.

Instead of relying only on an LLM's pretrained knowledge, the application:

**Collects → Processes → Embeds → Stores → Retrieves → Generates**

relevant information from research URLs and uses that context to generate grounded answers.

## Project Demo

![image]()

### ✨ What the application provides

- 🔗 URL-based real estate research
- 📚 Document loading and processing
- 🧩 Intelligent text chunking
- 🧠 Semantic search using embeddings
- 🗄️ ChromaDB vector storage
- 🔍 Top-K relevant document retrieval
- 🤖 LLM-powered answer generation
- 🔗 Source/reference information
- 🌡️ Adjustable LLM temperature
- 🖥️ Interactive Streamlit interface

---

## 🎯 Problem Statement

Real estate research often requires visiting multiple websites, reading large amounts of information, and manually comparing relevant data.

This project aims to make that process easier through a conversational RAG application.

### The user can:

1. 🔗 Provide one or more real estate research URLs.
2. ⚙️ Process the information automatically.
3. ❓ Ask questions related to the collected information.
4. 🔍 Retrieve the most relevant research content.
5. 🤖 Generate an AI-powered response.
6. 📎 Review the references used for the research.

---

## 🧠 How the Application Works

The application follows a standard **Retrieval-Augmented Generation (RAG)** architecture:

```text
                         👤 USER
                           │
                           ▼
                  🔗 Enter Research URLs
                           │
                           ▼
                ┌──────────────────────┐
                │  URL Document Loader │
                │ UnstructuredURLLoader│
                └──────────┬───────────┘
                           │
                           ▼
                    📄 Documents
                           │
                           ▼
              ┌────────────────────────┐
              │ Recursive Text Splitter│
              └───────────┬────────────┘
                          │
                          ▼
                    🧩 Text Chunks
                          │
                          ▼
              🧠 HuggingFace Embeddings
                          │
                          ▼
                    🗄️ ChromaDB
                          │
                          │
              ┌───────────▼───────────┐
              │      ❓ User Query     │
              └───────────┬───────────┘
                          │
                          ▼
                    🔍 Retriever
                          │
                          ▼
                 📚 Relevant Chunks
                          │
                          ▼
                    🤖 Groq LLM
                          │
                          ▼
                  💬 Generated Answer
                          │
                          ▼
                    🔗 References
```

---

## 🔑 Key Technologies

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Core programming language |
| 🔗 **LangChain** | RAG pipeline and LLM orchestration |
| ⚡ **ChatGroq** | LLM integration |
| 🤖 **GPT-OSS-120B** | Language model used for answer generation |
| 🗄️ **ChromaDB** | Vector database for semantic retrieval |
| 🧠 **HuggingFace Embeddings** | Converts text into vector representations |
| 🌐 **UnstructuredURLLoader** | Loads content from research URLs |
| ✂️ **RecursiveCharacterTextSplitter** | Splits documents into manageable chunks |
| 🎨 **Streamlit** | Interactive web application |
| 🔐 **python-dotenv** | Environment variable management |

---

# ⚙️ Core Features

## 🔗 1. Multi-URL Research

Users can provide multiple research URLs through the Streamlit interface.

```text
URL 1 ─┐
URL 2 ─┼──► Document Processing ──► ChromaDB
URL 3 ─┘
```

This allows the application to combine information from multiple sources for broader research coverage.

---

## 🧩 2. Intelligent Text Chunking

Large web documents are divided into smaller, meaningful chunks using:

```python
RecursiveCharacterTextSplitter
```

Example configuration:

```python
chunk_size = 200
chunk_overlap = 20
```

Chunking makes it easier for the retriever to identify the most relevant sections of the source material.

---

## 🧠 3. Semantic Embeddings

The application uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

to convert text chunks into numerical vector representations.

```text
Text
  ↓
Embedding Model
  ↓
Vector Representation
  ↓
ChromaDB
```

This enables semantic similarity search instead of relying only on exact keyword matching.

---

## 🗄️ 4. ChromaDB Vector Database

The generated embeddings are stored in **ChromaDB**.

The vector database allows the application to efficiently search for information that is semantically related to the user's question.

---

## 🔍 5. Retriever

When the user submits a query, the retriever searches ChromaDB and returns the most relevant chunks.

Example:

```python
retriever = vector_data.as_retriever(
    search_kwargs={"k": 2}
)
```

### Retrieval flow

```text
User Query
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Top-K Relevant Chunks
    ↓
LLM Context
```

---

## 🤖 6. AI-Powered Answer Generation

The retrieved information is passed to the LLM to generate an answer based on the available research context.

The project uses:

```python
ChatGroq(
    model="openai/gpt-oss-120b"
)
```

This allows the application to combine **retrieval + generation** into a complete RAG workflow.

---

## 🔗 7. Source References

Source metadata is preserved with the retrieved documents.

This allows the application to provide the original research URLs along with the generated response.

```text
Answer
   ↓
Relevant Source
   ↓
Original Research URL
```

This makes it easier for users to verify the information.

---

## 🌡️ 8. Temperature Control

The Streamlit interface provides a temperature slider for controlling the behavior of the LLM.

```text
Lower Temperature
       ↓
More focused
More deterministic
       │
       │
Higher Temperature
       ↓
More varied
More creative
```

For research-oriented questions, lower temperature values are generally preferred because they encourage more focused responses.

---

# 🖥️ Application Interface

The Streamlit interface provides a simple workflow for conducting research.

### Users can:

- 🔗 Enter research URLs
- ⚙️ Process URLs
- 🌡️ Adjust LLM temperature
- ❓ Enter questions
- 💬 View generated answers
- 🔗 Open source references
- 📖 View application usage instructions

---

# 📂 Project Structure

```text
Real-Estate-Assistant-RAG/
│
├── 📄 main.py
│   └── Streamlit application interface
│
├── 📄 rag.py
│   └── RAG pipeline
│       ├── LLM initialization
│       ├── URL processing
│       ├── Text splitting
│       ├── Embeddings
│       ├── ChromaDB
│       ├── Retrieval
│       └── Answer generation
│
├── 📄 requirements.txt
│   └── Project dependencies
│
├── 🔐 .env
│   └── API keys and environment variables
│
├── 🚫 .gitignore
│   └── Files excluded from Git
│
├── 📖 README.md
│   └── Project documentation
│
└── 📁 research_data/
    └── ChromaDB persistent vector data
```

---

# 🚀 Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
```

```bash
cd Real-Estate-Assistant-RAG
```

---

## 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
```

> ⚠️ **Never commit your `.env` file or API keys to GitHub.**

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
research_data/
```

---

# ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run main.py
```

The application will open in your default web browser.

---

# 📖 How to Use the Application

### 1. 🌐 Open the Application

Open the application and make sure you have a **stable internet connection** for fetching research information from the provided URLs.

### 2. 🔗 Add Research URLs

Enter **at least one valid research URL** in the URL input fields.

You can add multiple URLs to improve research coverage.

### 3. ⚙️ Process the URLs

Click:

```text
Process URLs
```

The application will:

```text
Load
  ↓
Split
  ↓
Embed
  ↓
Store in ChromaDB
```

### 4. ❓ Enter Your Query

Ask a specific question related to the information available on the provided URLs.

Example:

```text
Which cities had the highest retail demand?
```

### 5. 💬 Review the Answer

The RAG pipeline retrieves relevant information and generates an answer using the LLM.

### 6. 🔗 Verify the Sources

Review the provided source references to verify the information before making decisions.

### 7. 🏠 Make an Informed Decision

Use the generated research as an **informational aid** when evaluating real estate opportunities.

> 💡 **Tip:** Use reliable research sources and ask specific questions for better results.

---

# 🧪 Example

## Input URL

```text
https://www.cbre.co.in/insights/figures/india-market-monitor-q2-2026-retail
```

## Query

```text
Which cities had high demand?
```

## Example Response

```text
The high-demand activity was led by Delhi-NCR,
Hyderabad, and Mumbai, which together accounted
for more than 60% of total activity during the quarter.
```

## Source

```text
CBRE India Market Monitor Q2 2026 Retail
```

---

# 🏗️ RAG Components

### 1. 🌐 Document Loader

```python
UnstructuredURLLoader
```

Loads information from user-provided URLs.

### 2. ✂️ Text Splitter

```python
RecursiveCharacterTextSplitter
```

Divides large documents into smaller chunks.

### 3. 🧠 Embedding Model

```text
sentence-transformers/all-MiniLM-L6-v2
```

Converts text chunks into vector representations.

### 4. 🗄️ Vector Database

```text
ChromaDB
```

Stores embeddings and supports similarity-based retrieval.

### 5. 🔍 Retriever

Retrieves the most relevant document chunks based on the user's query.

### 6. 🤖 LLM

```text
GPT-OSS-120B through Groq
```

Generates the final response using the retrieved research context.

---

# 🔄 Complete RAG Workflow

```text
┌──────────────────────────────┐
│      User enters URLs        │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│   UnstructuredURLLoader      │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│   Recursive Text Splitting   │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ HuggingFace Embedding Model  │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│          ChromaDB            │
└───────────────┬──────────────┘
                │
                │
       User submits query
                │
                ↓
┌──────────────────────────────┐
│          Retriever           │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│    Relevant Research Data    │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│      GPT-OSS-120B / Groq     │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│      Generated Answer        │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│     Source References        │
└──────────────────────────────┘
```

---

# 🆚 Traditional LLM vs RAG

## Traditional LLM

```text
User Query
    ↓
   LLM
    ↓
 Answer
```

The model primarily relies on its pretrained knowledge and the context supplied directly in the prompt.

## This Project

```text
User Query
    ↓
Retriever
    ↓
Relevant Research Data
    ↓
LLM
    ↓
Grounded Answer
    ↓
Source References
```

The RAG approach allows the application to work with **user-provided and potentially more recent research information**.

---

# ⚠️ Limitations

- 🌐 Website accessibility depends on the target website.
- 🛡️ Some websites may block automated content extraction.
- 📊 Response quality depends on the quality of the source data.
- 🔎 Retrieved information may not represent the entire real estate market.
- 🤖 LLM responses can still contain errors.
- 💼 The application is a research assistant, not a replacement for professional financial or real estate advice.

---

# 🔮 Future Improvements

- [ ] 📄 PDF document support
- [ ] 🌐 More robust web scraping
- [ ] 🔗 Improved source citation and attribution
- [ ] 💬 Conversation memory
- [ ] 📝 Query history
- [ ] 🔀 Hybrid search
- [ ] 🎯 Document reranking
- [ ] 🏷️ Metadata filtering
- [ ] 🛡️ Document quality validation
- [ ] 🌍 Multi-language support
- [ ] 🔐 User authentication
- [ ] ☁️ Cloud deployment
- [ ] 🤖 Agentic research workflows
- [ ] 📈 Real-time real estate market data integration

---

# 📚 Concepts Demonstrated

This project demonstrates practical implementation of:

- 🧠 Large Language Models
- 🔎 Retrieval-Augmented Generation
- 💬 Prompt-based generation
- 🗄️ Vector databases
- 🧩 Text embeddings
- 🔍 Semantic similarity search
- 📄 Document loading
- ✂️ Text chunking
- 📚 Information retrieval
- 🔗 Source attribution
- 🔗 LangChain
- 🗄️ ChromaDB
- 🤗 HuggingFace
- ⚡ Groq
- 🎨 Streamlit
- 🌡️ LLM parameter tuning

---

# 💡 Key Learning Outcomes

Through this project, I explored how a real-world GenAI application can be built by combining multiple components:

```text
LLM
 +
Embeddings
 +
Vector Database
 +
Retriever
 +
Document Processing
 +
Web Data
 +
Streamlit
 =
Real-World RAG Application
```

The project provides practical experience with the complete lifecycle of a basic RAG application, from **data ingestion to retrieval and final answer generation**.

---

# 🔒 Security Notes

Do not expose API keys in source code.

Use environment variables:

```env
GROQ_API_KEY=your_api_key
HF_TOKEN=your_token
```

Keep `.env` excluded from Git:

```text
.env
```

---

# ⭐ Future Vision

The long-term goal is to evolve this project from a URL-based research assistant into a more comprehensive **AI-powered real estate research platform** capable of combining:

```text
Web Research
     +
Market Data
     +
Documents
     +
RAG
     +
Advanced Retrieval
     +
LLM Reasoning
     +
Agentic Workflows
```

to help users perform faster and more informed real estate research.

---

# 👨‍💻 Author

## Vaishnav Wagh

**Machine Learning Engineer | AI Engineer | Deep Learning Engineer**

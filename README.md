# PDF Interaction Q&A using RAG on Healthcare Data

## Overview

This project leverages Retrieval-Augmented Generation (RAG) for interacting with healthcare-related PDFs. The system uses the LLaMA LLM model to perform Question-Answering (Q&A) tasks, where users can extract information from PDF documents effectively. This tool is designed to make it easier for healthcare professionals, researchers, or developers to query and retrieve data from medical PDFs.

## Key Features

- **PDF Parsing**: Extracts text from PDF documents, focusing on healthcare data.
- **RAG-based Q&A**: Uses a RAG architecture that combines a retrieval system with a generative model (LLaMA LLM) for generating answers based on the context retrieved from the PDFs.
- **Healthcare Data Focus**: Optimized for querying healthcare-specific information, like medical records, research papers, and patient reports.

## Getting Started

To set up this project locally, follow the steps below.

### Prerequisites

- Python 3.7+
- Pip (Python package manager)
- LLaMA LLM Model (for Q&A generation)
- Libraries:
  - `PyPDF2` (for PDF extraction)
  - `langchain` and `langchain_community` (for LLaMA model integration)
  - `FAISS` (for efficient retrieval)

### Step 1: Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/LagisettyRavikiran/PDF-Interaction-Q-A.git
cd PDF-Interaction-Q-A
```

### Step 2: Install Requirements

Install the required Python libraries by running the following command:

```bash
pip install -r requirements.txt
```

This will ensure that all the dependencies, including `PyPDF2`, `langchain`, `FAISS`, and others, are properly installed.

### Step 3: Run the Application

Once the dependencies are installed, you can start using the application by executing the following command:

```bash
python main.py
```

> **Note:** Replace `main.py` with the actual name of the script that initializes the application if different.

The application will allow you to upload healthcare-related PDF documents and interact with them using the Q&A functionality powered by RAG and the LLaMA LLM model.

## Usage

- Upload healthcare-related PDFs to the system.
- Enter your queries in the provided input field.
- The application retrieves relevant information from the uploaded PDFs and generates answers using the RAG architecture.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
Feel free to contribute to the project or report any issues by opening a GitHub issue in this repository.

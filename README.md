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
  - `langchain` and 'langchain_community' (for LLaMA model integration)
  - `FAISS` (for efficient retrieval)
  
### Step 1: Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/LagisettyRavikiran/PDF-Interaction-Q-A.git
cd PDF-Interaction-Q-A

### Step 1: Clone the Repository

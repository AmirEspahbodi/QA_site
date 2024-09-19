# Question-Answer Website

This project is a fully functional question-answer web application that allows users to upload a file and ask questions about its contents. The system processes the file, extracts the text, and enables users to query the text for specific information.

## Features

- **File Upload:** Users can upload various document formats.
- **Natural Language Processing:** The system processes uploaded documents and answers user questions based on the content of the file.
- **Asynchronous Web Server:** FastAPI provides a fast, asynchronous backend to handle file uploads and question-answer logic.
- **ChromaDB:** Used to store and index text for efficient querying.
- **Document Parsing:** Utilizes PyPDF to handle PDF files and Python-magic to identify file types.
- **Language Processing:** Leverages LangChain and NLTK for NLP capabilities.

## Technology Stack

- **FastAPI:** Provides the web framework for handling requests and delivering responses asynchronously.
- **LangChain:** Chains together different language models to help answer complex queries.
- **ChromaDB:** Efficient vector database for text indexing and retrieval.
- **PyPDF:** Handles the parsing and extraction of text from PDF files.
- **Python-magic:** Identifies file types for proper handling.
- **NLTK:** Aids in text tokenization and processing for natural language queries.

## How It Works
- **Upload a File**: Users upload a file through the frontend interface.
- **File Parsing**: The backend parses the file to extract the text using PyPDF or another parser based on the file type identified by Python-magic.
- **Text Storage**: The extracted text is stored in ChromaDB, allowing for fast, efficient searches.
- **Ask a Question**: Users can ask questions related to the content of the uploaded file.
- **Answer Generation**: LangChain processes the user's query using NLP techniques, returning the most relevant answer from the document.
